import os
import collections
import json
import numpy as np
from tqdm import tqdm

np.random.seed(42)
topics = ['lifestyle', 'recreation', 'science', 'technology', 'writing']

all_pid2passage = {}
all_qid2question = {}

sessions_pid = [set(), set(), set(), set()]
sessions_train_qid = [set(), set(), set(), set()]
sessions_train_qid2pid = [{}, {}, {}, {}]
sessions_dev_qid = [set(), set(), set(), set()]
sessions_dev_qid2pid = [{}, {}, {}, {}]
sessions_test_qid = [set(), set(), set(), set()]
sessions_test_qid2pid = [{}, {}, {}, {}]

for topic in ['technology', 'writing']:
    pid2passage = {}
    with open(f'../data/lotte/{topic}.collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)
    qid2question = {}
    with open(f'../data/lotte/{topic}.questions.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2question[data['query_id']] = data['query']
    all_qid2question.update(qid2question)
    qid2pids = {}
    with open(f'../data/lotte/{topic}.qrels.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2pids[data['qid']] = data['answer_pids']

    # 划分train/dev/test query
    all_qid = list(qid2pids.keys())
    all_qid.sort()
    np.random.shuffle(all_qid)
    num_qid = len(all_qid)
    train_qid, dev_qid, test_qid = all_qid[:int(num_qid*0.7)], all_qid[int(num_qid*0.7):int(num_qid*0.85)], all_qid[int(num_qid*0.85):]
    
    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*0.7)])
    sessions_pid[1].update(all_pid[int(num_pid*0.7):int(num_pid*0.8)])
    sessions_pid[2].update(all_pid[int(num_pid*0.8):int(num_pid*0.9)])
    sessions_pid[3].update(all_pid[int(num_pid*0.9):])
    # for pid in sessions_pid:
    #     print(list(pid)[:3])

    for qid, pids in tqdm(qid2pids.items(), total=len(qid2pids)):
        pids = set(pids)
        for i, session_pid in enumerate(sessions_pid):
            inter_pids = pids.intersection(session_pid)
            if len(inter_pids) > 0:
                if qid in set(train_qid):
                    sessions_train_qid[i].add(qid)
                    sessions_train_qid2pid[i][qid] = inter_pids
                elif qid in set(dev_qid):
                    sessions_dev_qid[i].add(qid)
                    sessions_dev_qid2pid[i][qid] = inter_pids
                elif qid in set(test_qid):
                    sessions_test_qid[i].add(qid)
                    sessions_test_qid2pid[i][qid] = inter_pids
    print(f'{topic} ....')
    print([len(pid) for pid in sessions_pid])
    print([len(qid) for qid in sessions_train_qid])
    print([len(qid) for qid in sessions_dev_qid])
    print([len(qid) for qid in sessions_test_qid])
for topic in ['lifestyle']:
    pid2passage = {}
    with open(f'../data/lotte/{topic}.collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)
    qid2question = {}
    with open(f'../data/lotte/{topic}.questions.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2question[data['query_id']] = data['query']
    all_qid2question.update(qid2question)
    qid2pids = {}
    with open(f'../data/lotte/{topic}.qrels.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2pids[data['qid']] = data['answer_pids']
    
    # 划分train/test query
    all_qid = list(qid2pids.keys())
    all_qid.sort()
    np.random.shuffle(all_qid)
    num_qid = len(all_qid)
    train_qid, dev_qid, test_qid = all_qid[:int(num_qid*0.7)], all_qid[int(num_qid*0.7):int(num_qid*0.85)], all_qid[int(num_qid*0.85):]
    
    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*0.4)])
    sessions_pid[1].update(all_pid[int(num_pid*0.4):int(num_pid*0.9)])
    sessions_pid[2].update(all_pid[int(num_pid*0.9):int(num_pid*0.95)])
    sessions_pid[3].update(all_pid[int(num_pid*0.95):])
    # for pid in sessions_pid:
    #     print(list(pid)[:3])

    for qid, pids in tqdm(qid2pids.items(), total=len(qid2pids)):
        pids = set(pids)
        for i, session_pid in enumerate(sessions_pid):
            inter_pids = pids.intersection(session_pid)
            if len(inter_pids) > 0:
                if qid in set(train_qid):
                    sessions_train_qid[i].add(qid)
                    sessions_train_qid2pid[i][qid] = inter_pids
                elif qid in set(dev_qid):
                    sessions_dev_qid[i].add(qid)
                    sessions_dev_qid2pid[i][qid] = inter_pids
                elif qid in set(test_qid):
                    sessions_test_qid[i].add(qid)
                    sessions_test_qid2pid[i][qid] = inter_pids
    print(f'{topic} ....')
    print([len(pid) for pid in sessions_pid])
    print([len(qid) for qid in sessions_train_qid])
    print([len(qid) for qid in sessions_dev_qid])
    print([len(qid) for qid in sessions_test_qid])
for topic in ['recreation']:
    pid2passage = {}
    with open(f'../data/lotte/{topic}.collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)
    qid2question = {}
    with open(f'../data/lotte/{topic}.questions.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2question[data['query_id']] = data['query']
    all_qid2question.update(qid2question)
    qid2pids = {}
    with open(f'../data/lotte/{topic}.qrels.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2pids[data['qid']] = data['answer_pids']

    # 划分train/test query
    all_qid = list(qid2pids.keys())
    all_qid.sort()
    np.random.shuffle(all_qid)
    num_qid = len(all_qid)
    train_qid, dev_qid, test_qid = all_qid[:int(num_qid*0.7)], all_qid[int(num_qid*0.7):int(num_qid*0.85)], all_qid[int(num_qid*0.85):]
    
    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*0.4)])
    sessions_pid[1].update(all_pid[int(num_pid*0.4):int(num_pid*0.45)])
    sessions_pid[2].update(all_pid[int(num_pid*0.45):int(num_pid*0.95)])
    sessions_pid[3].update(all_pid[int(num_pid*0.95):])
    # for pid in sessions_pid:
    #     print(list(pid)[:3])

    for qid, pids in tqdm(qid2pids.items(), total=len(qid2pids)):
        pids = set(pids)
        for i, session_pid in enumerate(sessions_pid):
            inter_pids = pids.intersection(session_pid)
            if len(inter_pids) > 0:
                if qid in set(train_qid):
                    sessions_train_qid[i].add(qid)
                    sessions_train_qid2pid[i][qid] = inter_pids
                elif qid in set(dev_qid):
                    sessions_dev_qid[i].add(qid)
                    sessions_dev_qid2pid[i][qid] = inter_pids
                elif qid in set(test_qid):
                    sessions_test_qid[i].add(qid)
                    sessions_test_qid2pid[i][qid] = inter_pids
    print(f'{topic} ....')
    print([len(pid) for pid in sessions_pid])
    print([len(qid) for qid in sessions_train_qid])
    print([len(qid) for qid in sessions_dev_qid])
    print([len(qid) for qid in sessions_test_qid])
for topic in ['science']:
    pid2passage = {}
    with open(f'../data/lotte/{topic}.collection.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            pid2passage[data['docid']] = data['text']
    all_pid2passage.update(pid2passage)
    qid2question = {}
    with open(f'../data/lotte/{topic}.questions.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2question[data['query_id']] = data['query']
    all_qid2question.update(qid2question)
    qid2pids = {}
    with open(f'../data/lotte/{topic}.qrels.json', 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2pids[data['qid']] = data['answer_pids']

    # 划分train/test query
    all_qid = list(qid2pids.keys())
    all_qid.sort()
    np.random.shuffle(all_qid)
    num_qid = len(all_qid)
    train_qid, dev_qid, test_qid = all_qid[:int(num_qid*0.7)], all_qid[int(num_qid*0.7):int(num_qid*0.85)], all_qid[int(num_qid*0.85):]
    
    # 划分collection
    all_pid = list(pid2passage.keys())
    all_pid.sort()
    np.random.shuffle(all_pid)
    num_pid = len(all_pid)
    sessions_pid[0].update(all_pid[:int(num_pid*0.4)])
    sessions_pid[1].update(all_pid[int(num_pid*0.4):int(num_pid*0.45)])
    sessions_pid[2].update(all_pid[int(num_pid*0.45):int(num_pid*0.5)])
    sessions_pid[3].update(all_pid[int(num_pid*0.5):])
    # for pid in sessions_pid:
    #     print(list(pid)[:3])

    for qid, pids in tqdm(qid2pids.items(), total=len(qid2pids)):
        pids = set(pids)
        for i, session_pid in enumerate(sessions_pid):
            inter_pids = pids.intersection(session_pid)
            if len(inter_pids) > 0:
                if qid in set(train_qid):
                    sessions_train_qid[i].add(qid)
                    sessions_train_qid2pid[i][qid] = inter_pids
                elif qid in set(dev_qid):
                    sessions_dev_qid[i].add(qid)
                    sessions_dev_qid2pid[i][qid] = inter_pids
                elif qid in set(test_qid):
                    sessions_test_qid[i].add(qid)
                    sessions_test_qid2pid[i][qid] = inter_pids
    print(f'{topic} ....')
    print([len(pid) for pid in sessions_pid])
    print([len(qid) for qid in sessions_train_qid])
    print([len(qid) for qid in sessions_dev_qid])
    print([len(qid) for qid in sessions_test_qid])
print('total ....')
print([len(pid) for pid in sessions_pid])
print([len(qid) for qid in sessions_train_qid])
print([len(qid) for qid in sessions_dev_qid])
print([len(qid) for qid in sessions_test_qid])
for qid2pid in sessions_train_qid2pid:
    print(np.sum([len(pid) for pid in qid2pid.values()]))
for qid2pid in sessions_dev_qid2pid:
    print(np.sum([len(pid) for pid in qid2pid.values()]))
for qid2pid in sessions_test_qid2pid:
    print(np.sum([len(pid) for pid in qid2pid.values()]))

# 写入数据
with open('train_query.tsv', 'w') as w:
    for qid in sessions_train_qid[0]:
        w.write(f'{qid}\t{all_qid2question[qid]}\n')

data_dir = './train_dir'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
with open(os.path.join(data_dir, 'train.jsonl'), 'w') as w:
    for qid, pids in sessions_train_qid2pid[0].items():
        positive_passages = []
        for pid in pids:
            dict_ = dict(docid=pid, text=all_pid2passage[pid])
            positive_passages.append(dict_)
        dict_ = dict(query_id=qid, query=all_qid2question[qid], positive_passages=positive_passages)
        json_dict = json.dumps(dict_)
        w.write(json_dict + "\n")

for i in [0, 1, 2, 3]:
    data_dir = f'./session_{i+1}/corpus_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'corpus.jsonl'), 'w') as w:
        for pid in sessions_pid[i]:
            dict_ = dict(docid=pid, text=all_pid2passage[pid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

    data_dir = f'./session_{i+1}/collection_jsonl'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'corpus.jsonl'), 'w') as w:
        for pid in sessions_pid[i]:
            dict_ = dict(id=pid, contents=all_pid2passage[pid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    
    data_dir = f'./session_{i+1}/dev_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'dev.jsonl'), 'w') as w:
        for qid in sessions_dev_qid[i]:
            dict_ = dict(query_id=qid, query=all_qid2question[qid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    
    data_dir = f'./session_{i+1}/test_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'test.jsonl'), 'w') as w:
        for qid in sessions_test_qid[i]:
            dict_ = dict(query_id=qid, query=all_qid2question[qid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    
    with open(f'./session_{i+1}/dev_query.tsv', 'w') as w:
        for qid in sessions_dev_qid[i]:
            w.write(f'{qid}\t{all_qid2question[qid]}\n')
    
    with open(f'./session_{i+1}/test_query.tsv', 'w') as w:
        for qid in sessions_test_qid[i]:
            w.write(f'{qid}\t{all_qid2question[qid]}\n')
    
    with open(f'./session_{i+1}/dev_qrel.jsonl', 'w') as w:
        for qid, pids in sessions_dev_qid2pid[i].items():
            dict_ = dict(qid=qid, answer_pids=list(pids))
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

    with open(f'./session_{i+1}/test_qrel.jsonl', 'w') as w:
        for qid, pids in sessions_test_qid2pid[i].items():
            dict_ = dict(qid=qid, answer_pids=list(pids))
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

for i in [1, 2, 3]:
    data_dir = f'./session_all{i+1}/corpus_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'corpus.jsonl'), 'w') as w:
        for j in range(0, i+1):
            for pid in sessions_pid[j]:
                dict_ = dict(docid=pid, text=all_pid2passage[pid])
                json_dict = json.dumps(dict_)
                w.write(json_dict + "\n")

    data_dir = f'./session_all{i+1}/collection_jsonl'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'corpus.jsonl'), 'w') as w:
        for j in range(0, i+1):
            for pid in sessions_pid[j]:
                dict_ = dict(id=pid, contents=all_pid2passage[pid])
                json_dict = json.dumps(dict_)
                w.write(json_dict + "\n")
    
    data_dir = f'./session_all{i+1}/dev_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'dev.jsonl'), 'w') as w:
        dev_qid = sessions_dev_qid[0]
        for j in range(1, i+1):
            dev_qid.update(sessions_dev_qid[j])
        for qid in dev_qid:
            dict_ = dict(query_id=qid, query=all_qid2question[qid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    
    data_dir = f'./session_all{i+1}/test_dir'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, 'test.jsonl'), 'w') as w:
        test_qid = sessions_test_qid[0]
        for j in range(1, i+1):
            test_qid.update(sessions_test_qid[j])
        for qid in test_qid:
            dict_ = dict(query_id=qid, query=all_qid2question[qid])
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    
    with open(f'./session_all{i+1}/dev_query.tsv', 'w') as w:
        dev_qid = sessions_dev_qid[0]
        for j in range(1, i+1):
            dev_qid.update(sessions_dev_qid[j])
        for qid in dev_qid:
            w.write(f'{qid}\t{all_qid2question[qid]}\n')
    
    with open(f'./session_all{i+1}/test_query.tsv', 'w') as w:
        test_qid = sessions_test_qid[0]
        for j in range(1, i+1):
            test_qid.update(sessions_test_qid[j])
        for qid in test_qid:
            w.write(f'{qid}\t{all_qid2question[qid]}\n')

    with open(f'./session_all{i+1}/dev_qrel.jsonl', 'w') as w:
        dev_qid2pid = sessions_dev_qid2pid[0]
        for j in range(1, i+1):
            dev_qid2pid.update(sessions_dev_qid2pid[j])
        for qid, pids in dev_qid2pid.items():
            dict_ = dict(qid=qid, answer_pids=list(pids))
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

    with open(f'./session_all{i+1}/test_qrel.jsonl', 'w') as w:
        test_qid2pid = sessions_test_qid2pid[0]
        for j in range(1, i+1):
            test_qid2pid.update(sessions_test_qid2pid[j])
        for qid, pids in test_qid2pid.items():
            dict_ = dict(qid=qid, answer_pids=list(pids))
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
