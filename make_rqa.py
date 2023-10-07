import json
import os
with open('data/GoMate/demo.txt', 'r', encoding='utf-8') as f:
    print(r"\n".join(f.read().split('\n')))
print("================================")
# with open('data/GoMate/demo.json', 'r', encoding='utf-8') as f:
#     data = json.loads(f.read().strip())
#
#     print("{}{}{}".format(data["instruction"], data["input"], data["output"]))

# with open('data/GoMate/searchgpt_retrieval_qa.json', 'r', encoding='utf-8') as f:
#     sing_data = json.load(f)
#
# with open('data/GoMate/searchgpt_retrieval_qa.jsonl', 'w', encoding='utf-8') as f:
#     instruction = {}
#     for sample in sing_data:
#         print(sample)
#         f.write(json.dumps(sample, ensure_ascii=False) + '\n')

# data=[]
# for idx,file in enumerate(os.listdir('data/GoMate/questions')):
#     if idx>20:
#         data.append(open(f'data/GoMate/questions/{file}','r',encoding='utf-8').read())
# print(data)