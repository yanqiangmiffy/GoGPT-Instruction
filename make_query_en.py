import json

from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel

with open('query_rewrite.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)

tokenizer = AutoTokenizer.from_pretrained("/mnt/nfs/pretrained_models/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("/mnt/nfs/pretrained_models/chatglm2-6b", trust_remote_code=True).cuda()
# 多显卡支持，使用下面两行代替上面一行，将num_gpus改为你实际的显卡数量
# from utils import load_model_on_gpus
# model = load_model_on_gpus("THUDM/chatglm2-6b", num_gpus=2)
model = model.eval()


def translate(query):
    query = f'请将下面句子翻译成英文：{query}'
    response, history = model.chat(tokenizer, query, history=[])
    return response


all_data = []

for sample in tqdm(data):
    en_sample = sample
    instruction = sample['instruction']
    en_sample['instruction'] = translate(instruction)

    input = sample['input']
    if input.strip() and len(input.strip())>0:
        en_sample['input'] = translate(input)
    else:
        en_sample['input'] = input

    output = sample['output']
    en_sample['output'] = translate(output)
    print(en_sample)
    all_data.append(en_sample)
with open('data/query/query_rewrite_en.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)
