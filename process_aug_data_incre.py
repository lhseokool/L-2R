import os
import collections
import json
import numpy as np
from tqdm import tqdm

np.random.seed(42)
topics = ['lifestyle', 'recreation', 'science', 'technology', 'writing']

all_pid2passage = {}
sessions_pid = [set(), set(), set()]

for topic in ['technology', 'writing']:
    pid2passage = {}
    with open(f'./data/lotte/{topic}.aug_collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)

    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*(0.1/0.3))])
    sessions_pid[1].update(all_pid[int(num_pid*(0.1/0.3)):int(num_pid*(0.2/0.3))])
    sessions_pid[2].update(all_pid[int(num_pid*(0.2/0.3)):])
for topic in ['lifestyle']:
    pid2passage = {}
    with open(f'./data/lotte/{topic}.aug_collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)

    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*(0.5/0.6))])
    sessions_pid[1].update(all_pid[int(num_pid*(0.5/0.6)):int(num_pid*(0.55/0.6))])
    sessions_pid[2].update(all_pid[int(num_pid*(0.55/0.6)):])
for topic in ['recreation']:
    pid2passage = {}
    with open(f'./data/lotte/{topic}.aug_collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)

    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*(0.05/0.6))])
    sessions_pid[1].update(all_pid[int(num_pid*(0.05/0.6)):int(num_pid*(0.55/0.6))])
    sessions_pid[2].update(all_pid[int(num_pid*(0.55/0.6)):])
for topic in ['science']:
    pid2passage = {}
    with open(f'./data/lotte/{topic}.aug_collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)

    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*(0.05/0.6))])
    sessions_pid[1].update(all_pid[int(num_pid*(0.05/0.6)):int(num_pid*(0.1/0.6))])
    sessions_pid[2].update(all_pid[int(num_pid*(0.1/0.6)):])
print('total ....')
print([len(pid) for pid in sessions_pid])


for i in [0, 1, 2]:
    data_dir = f'./data_incre_aug/session_{i+2}/corpus_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'w') as w:
        for pid in sessions_pid[i]:
            dict_ = dict(docid=pid, text=all_pid2passage[pid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

    data_dir = f'./data_incre_aug/session_{i+2}/collection_jsonl'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'w') as w:
        for pid in sessions_pid[i]:
            dict_ = dict(id=pid, contents=all_pid2passage[pid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

for i in [0, 1, 2]:
    data_dir = f'./data_incre_aug/session_all{i+2}/corpus_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'w') as w:
        for j in range(0, i+1):
            for pid in sessions_pid[j]:
                dict_ = dict(docid=pid, text=all_pid2passage[pid])
                json_dict = json.dumps(dict_)
                w.write(json_dict + "\n")

    data_dir = f'./data_incre_aug/session_all{i+2}/collection_jsonl'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'w') as w:
        for j in range(0, i+1):
            for pid in sessions_pid[j]:
                dict_ = dict(id=pid, contents=all_pid2passage[pid])
                json_dict = json.dumps(dict_)
                w.write(json_dict + "\n")


for i in [2, 3, 4]:
    for name in ['corpus_dir', 'collection_jsonl']:
        data_dir = f'./data_incre_aug/session_{i}/{name}'
        with open(os.path.join(data_dir, 'all_corpus.jsonl'), 'w') as w:
            with open(os.path.join(data_dir, 'corpus.jsonl'), 'r') as f:
                for line in f:
                    w.write(line)
            with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'r') as f:
                for line in f:
                    w.write(line)

    for name in ['corpus_dir', 'collection_jsonl']:
        data_dir = f'./data_incre_aug/session_all{i}/{name}'
        with open(os.path.join(data_dir, 'all_corpus.jsonl'), 'w') as w:
            with open(os.path.join(data_dir, 'corpus.jsonl'), 'r') as f:
                for line in f:
                    w.write(line)
            with open(os.path.join(data_dir, 'aug_corpus.jsonl'), 'r') as f:
                for line in f:
                    w.write(line)
