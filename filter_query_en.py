import json


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


with open('query_rewrite_en.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # print(data)

all_data = []

with open('query_rewrite_en_filter.jsonl','w',encoding='utf-8') as f:
    for sample in data:
        output = sample['output']
        if not is_contain_chinese(output) and  'transla' not in output:
            # print('#'.join(output.split('\n\n')))
            # print("=========")
            new_output = '#'.join(output.split('\n\n'))
            new_output = '#'.join(new_output.split('\n'))
            new_output = '#'.join(new_output.split('.'))
            if 'transla' in new_output:
                new_output = new_output.split(':')[-1]
                print(new_output)

            en_sample = sample
            en_sample['instruction'] = sample['instruction']
            en_sample['input'] = sample['input']
            en_sample['output'] = new_output.strip('#')
            f.write(json.dumps(en_sample,ensure_ascii=False)+'\n')
            all_data.append(en_sample)
print(len(all_data))
with open('query_rewrite_en_filter.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False)
