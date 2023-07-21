#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:quincy qiang
@license: Apache Licence
@file: make_searchgpt.py
@time: 2023/07/18
@contact: yanqiangmiffy@gamil.com
@software: PyCharm
@description: coding..
"""
import json

from tqdm import tqdm

cnt=0

with open('data/searchgpt/dureader_instruction.json','w',encoding='utf-8') as in_f:
    with open('data/dureader/search.dev.json', 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines()):
            # print(line)
            sample = json.loads(line.strip())
            # print(sample['answers'],sample['fake_answers'])
            output=','.join(sample['answers'])
            if len(output)>400:
                # print(len(output))
                cnt+=1
                data = {'instruction': '', 'input': '', 'output': ''}
                instruction=f"问题：{sample['question']}\n请结合如下支撑信息，回答上述问题：\n"
                input_docs="支撑信息：\n"
                selected_documents=[]
                for document in sample['documents']:
                    if document['is_selected']:
                        selected_documents.append(document['title']+"\n".join(document['paragraphs']))
                for idx,document_text in enumerate(selected_documents):
                    input_docs=input_docs+f'[{idx}]'+document_text+'\n'
                input_text=input_docs
                data['instruction']=instruction
                data['input']=input_text
                data['output']=output

                in_f.write(json.dumps(data,ensure_ascii=False) + '\n')
    print(cnt)
    with open('data/dureader/zhidao.dev.json', 'r', encoding='utf-8') as f:
        for line in tqdm(f.readlines()):
            # print(line)
            sample = json.loads(line.strip())
            # print(sample['answers'],sample['fake_answers'])
            output=','.join(sample['answers'])
            if len(output)>400:
                # print(len(output))
                cnt+=1
                data = {'instruction': '', 'input': '', 'output': ''}
                instruction=f"问题：{sample['question']}\n请结合如下支撑信息，回答上述问题：\n"
                input_docs="支撑信息：\n"
                selected_documents=[]
                for document in sample['documents']:
                    if document['is_selected']:
                        selected_documents.append(document['title']+"\n".join(document['paragraphs']))
                for idx,document_text in enumerate(selected_documents):
                    input_docs=input_docs+f'[{idx}]'+document_text+'\n'
                input_text=input_docs
                data['instruction']=instruction
                data['input']=input_text
                data['output']=output

                in_f.write(json.dumps(data,ensure_ascii=False) + '\n')
print(cnt)