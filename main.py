import json
import os

import pandas as pd

multi_choice_instruct = 'Please choose the best answer from the following four options based on the given question.' \
                        ' Note that each option may contain part of the correct answer, but not all. ' \
                        'Please read each option carefully and make a judgment based on the text content.'


def make_instruct_ARC(input_path, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        with open(input_path, 'r', encoding='utf-8') as raw_f:
            for line in raw_f.readlines():
                sample = json.loads(line.strip())
                # print(sample)
                data = {'instruction': '', 'input': '', 'output': ''}
                data['instruction'] = multi_choice_instruct + f'\nquestion:{sample["question"]["stem"]}'
                option_texts = [option['label'] + '.' + option['text'] for option in sample['question']['choices']]
                option_text = '\n'.join(option_texts)
                # data['instruction']=data['instruction']+f'\noptions:\n{option_text}'
                data['input'] = f'\noptions:\n{option_text}'
                data['output'] = sample['answerKey']
                # print(data)
                f.write(json.dumps(data) + '\n')


# make_instruct_ARC(input_path='data/ARC/ARC-c/ARC-Challenge-Dev.jsonl',
#                   output_path='data/ARC/ARC-c/ARC-Challenge-Dev-Instruction.json')
# make_instruct_ARC(input_path='data/ARC/ARC-e/ARC-Easy-Dev.jsonl',
#                   output_path='data/ARC/ARC-e/ARC-Easy-Dev-Instruction.json')

def make_instruct_BBH():
    for file in os.listdir('data/BBH/data'):
        if file.endswith('.json'):
            # print(file)
            filename = file.split('.json')[0]
            print(filename)
            instruct = open(f'data/BBH/lib_prompt/{filename}.txt', 'r', encoding='utf-8').readlines()[0]
            print(instruct)

            with open(f'data/BBH/instruction/{filename}.json', 'w', encoding='utf-8') as in_f:
                with open('data/BBH/data/' + file, 'r', encoding='utf-8') as f:
                    data = {'instruction': '', 'input': '', 'output': ''}
                    examples = json.load(f)['examples']
                    for example in examples:
                        data['instruction'] = instruct
                        data['input'] = example['input']
                        data['output'] = example['target']
                        in_f.write(json.dumps(data) + '\n')


# make_instruct_BBH()

def make_instruct_ceval(base_dir='data/ceval/formal_ceval/dev', output_dir='data/ceval/formal_ceval/instruction'):
    instruct_template = '请根据给定的文本，从以下四个选项中选择最佳答案。\n请注意，每个选项都可能包含正确答案的一部分信息，但并非全部。\n请仔细阅读每个选项，并结合文本内容进行判断。\n'
    for csv_file in os.listdir(base_dir):
        df = pd.read_csv(f'{base_dir}/{csv_file}')
        print(df.columns)

        with open(f'{output_dir}/{csv_file.split(".csv")[0]}.json', 'w', encoding='utf-8') as in_f:
            data = {'instruction': '', 'input': '', 'output': ''}
            for idx, row in df.iterrows():
                data['instruction'] = instruct_template + '问题：' + row['question'] + '\n'
                data['input'] = 'A.' + row['A'] + '\n' + 'B.' + row['B'] + '\n' + 'C.' + row['C'] + '\n' + 'D.' + row[
                    'D'] + '\n'
                if 'explanation' in row:
                    data['output'] = row['answer'] + '\n' + row['explanation']
                else:
                    data['output'] = row['answer']
                in_f.write(json.dumps(data, ensure_ascii=False) + '\n')


# make_instruct_ceval(base_dir='data/ceval/formal_ceval/dev', output_dir='data/ceval/formal_ceval/instruction')
# make_instruct_ceval(base_dir='data/ceval/formal_ceval/val', output_dir='data/ceval/formal_ceval/instruction')


def make_instruct_CLUE():
    instruct_template = '请判断给定两个句子之间的关系，两个句子可能存在的关系是neutral、entailment、contradiction，给出正确的关系'
    with open('data/CLUE/instruction/OCNLI_dev_instruction.json','w',encoding='utf-8') as in_f:
        df=pd.read_json('data/CLUE/OCNLI/dev.json',lines=True)
        print(df)
        print(df['label'].value_counts())
        data = {'instruction': '', 'input': '', 'output': ''}
        for idx, row in df.iterrows():
            data['instruction'] = instruct_template
            data['input'] = '句子1：'+row['sentence1']+',句子2：'+row['sentence2']
            data['output'] = row['label']
            in_f.write(json.dumps(data, ensure_ascii=False) + '\n')



# make_instruct_CLUE()


def make_instruct_FewCLUE():
    # =====tnews==
    label_df=pd.read_json('data/FewCLUE/tnews/label_index2en2zh.json',lines=True)
    print(label_df)
    label_df_map=dict(zip(label_df['label_desc'],label_df['label_zh']))
    instruct_template = '请判断下列新闻标题所属类别'
    with open('data/FewCLUE/instruction/tnews.json', 'w', encoding='utf-8') as in_f:
        df = pd.read_json('data/FewCLUE/tnews/train_few_all.json', lines=True)
        # print(df)
        # print(df['label'].value_counts())
        data = {'instruction': '', 'input': '', 'output': ''}
        for idx, row in df.iterrows():
            data['instruction'] = instruct_template+f'\n新闻标题：{row["sentence"]}\n'
            data['input'] = row['keywords']
            data['output'] = label_df_map[row['label_desc']]
            in_f.write(json.dumps(data, ensure_ascii=False) + '\n')
    # =====tnews==

    instruct_template = '请判断下列句子的情感极性'
    with open('data/FewCLUE/instruction/eprstmt.json', 'w', encoding='utf-8') as in_f:
        df = pd.read_json('data/FewCLUE/eprstmt/train_few_all.json', lines=True)
        # print(df)
        # print(df['label'].value_counts())
        data = {'instruction': '', 'input': '', 'output': ''}
        for idx, row in df.iterrows():
            data['instruction'] = instruct_template + f'\n{row["sentence"]}\n'
            data['output'] = row['label']
            in_f.write(json.dumps(data, ensure_ascii=False) + '\n')

    instruct_template = '请根据给定的文本，判断其所属的学科专业类别。请仔细阅读文本内容，并结合上下文进行判断。'
    with open('data/FewCLUE/instruction/csldcp.json', 'w', encoding='utf-8') as in_f:
        df = pd.read_json('data/FewCLUE/csldcp/train_few_all.json', lines=True)
        # print(df)
        # print(df['label'].value_counts())
        data = {'instruction': '', 'input': '', 'output': ''}
        for idx, row in df.iterrows():
            data['instruction'] = instruct_template + f'\n{row["content"]}\n'
            data['output'] = row['label']
            in_f.write(json.dumps(data, ensure_ascii=False) + '\n')
# make_instruct_FewCLUE()

def make_instruct_mbpp():
    instruct_template = '请根据给定的文本，判断其所属的学科专业类别。请仔细阅读文本内容，并结合上下文进行判断。'
    with open('data/mbpp/instruction/mbpp.json', 'w', encoding='utf-8') as in_f:
        df = pd.read_json('data/mbpp/mbpp.jsonl', lines=True)
        # print(df)
        # print(df['label'].value_counts())
        data = {'instruction': '', 'input': '', 'output': ''}
        for idx, row in df.iterrows():
            data['instruction'] =row["text"]
            data['output'] = row['code']
            in_f.write(json.dumps(data, ensure_ascii=False) + '\n')

# make_instruct_mbpp()

import random

def make_instruct_mmlu(base_dir='data/mmlu/auxiliary_train', output_dir='data/mmlu/instruction'):
    instruct_templates =[
        multi_choice_instruct,
                         'Please choose the best answer from the following four options based on the given text.',
                         'Please choose the best answer from one of the options below based on the given text.']
    for csv_file in os.listdir(base_dir):
        df = pd.read_csv(f'{base_dir}/{csv_file}',header=None)
        df.columns=['question','A','B','C','D','answer']
        print(df.columns)

        with open(f'{output_dir}/{csv_file.split(".csv")[0]}.json', 'w', encoding='utf-8') as in_f:
            data = {'instruction': '', 'input': '', 'output': ''}
            for idx, row in df.iterrows():
                data['instruction'] = random.choice(instruct_templates) + '\nquestion：' + row['question'] + '\n'
                data['input'] = 'A.' + row['A'] + '\n' + 'B.' + row['B'] + '\n' + 'C.' + row['C'] + '\n' + 'D.' + row[
                    'D'] + '\n'
                if 'explanation' in row:
                    data['output'] = row['answer'] + '\n' + row['explanation']
                else:
                    data['output'] = row['answer']
                in_f.write(json.dumps(data, ensure_ascii=False) + '\n')
make_instruct_mmlu()