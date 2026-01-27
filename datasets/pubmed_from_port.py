import json
import re

input_file = "pubmed/pubmed-dataset/test.txt"          # your original file (JSONL)
output_file = "pubmed_test.jsonl" # output like cnndm / wikihow

def clean_abstract(text):
    # remove <S> and </S> tags
    text = re.sub(r"</?S>", "", text)
    return text.strip()

with open(input_file) as fin, open(output_file, "w") as fout:
    for line in fin:
        example = json.loads(line)

        # Join article sentences
        ARTICLE = " ".join(example["article_text"]).strip()

        # Join and clean abstract sentences
        ABSTRACT = " ".join(example["abstract_text"])
        ABSTRACT = clean_abstract(ABSTRACT)

        if not ARTICLE or not ABSTRACT:
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

        json.dump(content, fout)
        fout.write("\n")
