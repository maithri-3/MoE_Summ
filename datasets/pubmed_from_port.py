from datasets import load_dataset
import json

# Load PubMed summarization dataset
dataset = load_dataset(
    "scientific_papers",
    "pubmed",
    download_mode="reuse_cache_if_exists"
)

train_dataset = dataset["train"]

with open("pubmed_train.jsonl", "w") as fw:
    for case in train_dataset:
        ARTICLE = case["article"]
        ABSTRACT = case["abstract"]

        if not ABSTRACT:
            continue

        src_length = len(ARTICLE.split())
        tgt_length = len(ABSTRACT.split())

        if tgt_length == 0:
            continue

        ratio = int(src_length / tgt_length)
        if ratio == 0 or ratio == 1:
            continue

        content = {
            "src": ARTICLE,
            "tgt": ABSTRACT,
            "idx": "pubmed"
        }

        json.dump(content, fw)
        fw.write("\n")
