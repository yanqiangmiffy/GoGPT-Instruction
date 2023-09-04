import json

sing_data = open('single_session_single_pairs.jsonl', 'r', encoding='utf-8').readlines()

multi_data = open('multi_session_single_pairs.jsonl', 'r', encoding='utf-8').readlines()

all_data = []
with open('query_rewrite.jsonl', 'w', encoding='utf-8') as f:
    instruction = {}
    for data in sing_data:
        sample = json.loads(data.strip())
        # print(sample)
        instruction = {'instruction': sample['prefix'] + '，' + sample['query'], 'input': '', 'output': sample['output']}
        print(instruction)
        all_data.append(instruction)
        f.write(json.dumps(instruction, ensure_ascii=False) + '\n')
    for data in multi_data:
        sample = json.loads(data.strip())
        instruction = {'instruction': sample['prefix'], 'input': sample['context'], 'output': sample['output']}
        print(instruction)
        f.write(json.dumps(instruction, ensure_ascii=False) + '\n')
        all_data.append(instruction)

all_data = []
with open('query_rewrite.jsonl', 'w', encoding='utf-8') as f:
    instruction = {}
    for data in sing_data:
        sample = json.loads(data.strip())
        # print(sample)
        instruction = {'instruction': sample['prefix'] + '，' + sample['query'], 'input': '', 'output': sample['output']}
        print(instruction)
        all_data.append(instruction)
        f.write(json.dumps(instruction, ensure_ascii=False) + '\n')
    for data in multi_data:
        sample = json.loads(data.strip())
        instruction = {'instruction': sample['prefix'], 'input': sample['context'], 'output': sample['output']}
        print(instruction)
        f.write(json.dumps(instruction, ensure_ascii=False) + '\n')
        all_data.append(instruction)

with open('query_rewrite.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)
