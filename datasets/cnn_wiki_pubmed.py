import json
import random

data_name = "validation"

def load_and_tag(path, tag):
    lines = []
    with open(path) as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                content = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Skipping bad JSON in {path} at line {lineno}: {e}")
                continue

            content["idx"] = tag
            lines.append(json.dumps(content))
    return lines


cnndm_lines  = load_and_tag(f"cnndm_{data_name}.json",  "cnndm")
wikihow_lines = load_and_tag(f"wikihow_{data_name}.jsonl", "wiki")
pubmed_lines = load_and_tag(f"pubmed_{data_name}.jsonl", "pubmed")

all_lines = cnndm_lines + wikihow_lines + pubmed_lines
random.shuffle(all_lines)

with open(f"cnndm_wiki_pubmed_{data_name}.jsonl", "w") as fw:
    fw.write("\n".join(all_lines))
