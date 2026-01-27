import pdb
import random
from datasets import load_dataset
# from datasets import load_metric
import json

dataset = load_dataset(
    "abisee/cnn_dailymail",
    "3.0.0",
    revision="main",
    download_mode="reuse_cache_if_exists"
)


test_dataset = dataset['test']
fw=open('cnndm_test.json','w')
for case in test_dataset:
    ARTICLE = case['article']
    highlights = case['highlights']
    content={}

    content['src']=ARTICLE
    src_length=len(ARTICLE.split())
    content['tgt']=highlights
    tgt_length=len(highlights.split())
    if tgt_length!=0:
        ratio=int(src_length/tgt_length)
        if ratio==0 or ratio==1:
            continue
        content['idx']='cnndm'
        json.dump(content,fw)
        fw.write('\n')


