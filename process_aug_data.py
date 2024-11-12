import json
import collections
import glob


int_pid = 5247957

topics = ['lifestyle', 'recreation', 'science', 'technology', 'writing']

qid2topic = {}
for topic in topics:
    query_path = f'./data/lotte/{topic}.questions.json'
    with open(query_path, 'r') as f:
        for line in f:
            data = json.loads(line)
            qid2topic[data['query_id']] = topic

topic2data = collections.defaultdict(list)
generated_files = glob.glob('../chatgpt/generated_for_train_query_*_*.txt')
for file in generated_files:
    print(file)
    with open(file, 'r') as f:
        for line in f:
            data = json.loads(line)
            topic = qid2topic[data['query_id']]
            for doc in data['generated_passages']:
                doc_text = doc['text']
                if len(doc_text) > 0:
                    dict_ = dict(docid=int_pid, text=doc_text)
                    topic2data[topic].append(dict_)
                    int_pid += 1
print(int_pid)

for topic, data in topic2data.items():
    with open(f'./data/lotte/{topic}.aug_collection.json', 'w') as w:
        for doc in data:
            json_dict = json.dumps(doc)
            w.write(json_dict + "\n")
