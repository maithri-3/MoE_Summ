import json
from datasets import load_dataset

# Load WikiHow dataset
dataset = load_dataset(
    "wikihow",
    "all",
    download_mode="reuse_cache_if_exists"
)

def write_split(split, out_file):
    with open(out_file, "w") as fw:
        for case in split:
            ARTICLE = case["article"]
            SUMMARY = case["summary"]

            if not SUMMARY:
                continue

            src_length = len(ARTICLE.split())
            tgt_length = len(SUMMARY.split())

            if tgt_length == 0:
                continue

            ratio = int(src_length / tgt_length)
            if ratio == 0 or ratio == 1:
                continue

            content = {
                "src": ARTICLE,
                "tgt": SUMMARY,
                "idx": "wikihow"
            }

            json.dump(content, fw)
            fw.write("\n")


# Train
write_split(dataset["train"], "wikihow_train.jsonl")

# Validation
write_split(dataset["validation"], "wikihow_validation.jsonl")

# Test
write_split(dataset["test"], "wikihow_test.jsonl")
