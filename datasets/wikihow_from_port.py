import json
import tensorflow_datasets as tfds

def write_split(split_name, out_file):
    dataset = tfds.load(
        "wikihow",
        split=split_name,
        shuffle_files=False
    )

    with open(out_file, "w") as fw:
        for example in tfds.as_numpy(dataset):
            article = example["article"].decode("utf-8")
            summary = example["summary"].decode("utf-8")

            if not summary:
                continue

            src_length = len(article.split())
            tgt_length = len(summary.split())

            if tgt_length == 0:
                continue

            ratio = int(src_length / tgt_length)
            if ratio == 0 or ratio == 1:
                continue

            content = {
                "src": article,
                "tgt": summary,
                "idx": "wikihow"
            }

            json.dump(content, fw)
            fw.write("\n")


# Train
write_split("train", "wikihow_train.jsonl")

# Validation
write_split("validation", "wikihow_validation.jsonl")

# Test
write_split("test", "wikihow_test.jsonl")
