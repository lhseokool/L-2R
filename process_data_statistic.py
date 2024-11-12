import os
import collections
import json
import numpy as np


topics = ['lifestyle', 'recreation', 'science', 'technology', 'writing']

for topic in topics:
    print(f'======{topic}====')
    len_passages = []
    len_questions = []
    len_qrels = []
    with open(f'./data/lotte/{topic}.collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            len_passages.append(len(data['text'].split(' ')))
    with open(f'./data/lotte/{topic}.questions.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            len_questions.append(len(data['query'].split(' ')))
    with open(f'./data/lotte/{topic}.qrels.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            len_qrels.append(len(data['answer_pids']))
    print(np.mean(len_passages), np.mean(len_questions), np.sum(len_qrels))
