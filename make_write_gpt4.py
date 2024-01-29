import json

import requests
from tqdm import tqdm

class ChatAPI():
    def __init__(self):
        self.headers = {
            # 'Authorization': 'Bearer sk-Yxobfc1wQO7zdnNY0dB0932e79C040859e55Dd25E445D898',
            'Authorization': 'Bearer sk-hxUsLEGFQHNHAfstD6930a85402846E1A042430c13F5A44b',
            'Content-Type': 'application/json',
        }

    def chat(self, query):
        json_data = {
            'model': 'gpt-4',
            'messages': [
                {
                    'role': 'user',
                    'content': query,
                },
            ],
            'stream': False,
        }
        # response = requests.post('https://apejhvxcd.cloud.sealos.io/v1/chat/completions', headers=self.headers,
        response = requests.post('https://wdapi7.61798.cn/v1/chat/completions', headers=self.headers,
                                 json=json_data)
        result = response.json()
        return result


if __name__ == '__main__':
    oneapi = ChatAPI()

    with open('data/GoWrite/new_task.json', 'r', encoding="utf-8") as f:
        data = json.load(f)

    with open('data/GoWrite/exist.txt', 'r', encoding='utf-8') as exif:
        existed = [line.strip() for line in exif.readlines()]

    with open('data/GoWrite/exist.txt', 'a',encoding='utf-8') as exif:
        with open('data/GoWrite/new_task.jsonl','a',encoding="utf-8") as off:
            for subset in data['result']:
                    for sample in tqdm(subset['detail']):
                        if sample["id"] not in existed:
                            # print(sample)
                            prompt = sample["real_prompt"]
                            if '画' not in prompt:
                                try:
                                    result = oneapi.chat(prompt)
                                    print(result)
                                    sample['answer'] = result
                                    exif.write(sample["id"] + "\n")
                                    off.write(json.dumps(sample, ensure_ascii=False) + '\n')
                                except Exception as e:
                                    print(e)
