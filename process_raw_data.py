import os
import collections
import json


topics = ['lifestyle', 'recreation', 'science', 'technology', 'writing']

num_passage = 0
num_question = 0
for topic in topics:
    output_query_path = f'./data/lotte/{topic}.questions.json'
    output_passage_path = f'./data/lotte/{topic}.collection.json'
    output_qrel_path = f'./data/lotte/{topic}.qrels.json'

    pid_str2int = {}
    p_int2content = {}

    qid_str2int = {}
    q_int2content = {}

    qrel_intq2intp = {}

    for split in ['dev', 'test']:
        input = f'./data/lotte/{topic}/{split}'
        with open(os.path.join(input, 'collection.tsv'), 'r') as f:
            for line in f:
                pid, content = line.rstrip().split('\t')
                intp = len(pid_str2int) + num_passage
                pid_str2int[f'{topic}_{split}_{pid}'] = intp
                p_int2content[intp] = content
        for name in ['forum', 'search']:
            with open(os.path.join(input, f'questions.{name}.tsv'), 'r') as f:
                for line in f:
                    qid, content = line.rstrip().split('\t')
                    intq = len(qid_str2int) + num_question
                    qid_str2int[f'{topic}_{split}_{name}_{qid}'] = intq
                    q_int2content[intq] = content
            with open(os.path.join(input, f'qas.{name}.jsonl'), 'r') as f:
                for line in f:
                    data = json.loads(line)
                    qid, pids = data['qid'], data['answer_pids']
                    int_qid = qid_str2int[f'{topic}_{split}_{name}_{qid}']
                    int_pids = [pid_str2int[f'{topic}_{split}_{pid}'] for pid in pids]
                    qrel_intq2intp[int_qid] = int_pids
    
    with open(output_query_path, 'w') as w:
        for int_qid, content in q_int2content.items():
            dict_ = dict(query_id=int_qid, query=content)
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    with open(output_passage_path, 'w') as w:
        for int_pid, content in p_int2content.items():
            dict_ = dict(docid=int_pid, text=content)
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")
    with open(output_qrel_path, 'w') as w:
        for int_qid, int_pids in qrel_intq2intp.items():
            dict_ = dict(qid=int_qid, answer_pids=int_pids)
            json_dict = json.dumps(dict_)
            w.write(json_dict + "\n")

    num_passage += len(pid_str2int)
    num_question += len(qid_str2int)
