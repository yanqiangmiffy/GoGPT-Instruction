import json

of=open('data/GoWrite/write_train_dataset.jsonl','w',encoding='utf-8')
valid_of=open('data/GoWrite/write_valid_dataset.jsonl','w',encoding='utf-8')

with open('data/GoWrite/write_functions.json','r',encoding='utf-8') as f:
    fun_examples=json.load(f)

with open('data/alpaca/alpaca_gpt4_data_zh.json','r',encoding='utf-8') as f:
    alpaca_examples=json.load(f)

with open('data/GoWrite/writer_instruction.json', 'r', encoding='utf-8') as f:
    ins_examples = json.load(f)



with open('data/GoWrite/new_task.jsonl', 'r', encoding='utf-8') as f:
    gpt4_examples = [json.loads(example.strip()) for example in f.readlines()]

for example in fun_examples:
    of.write(json.dumps(example,ensure_ascii=False)+"\n")


for example in ins_examples:
    of.write(json.dumps(example,ensure_ascii=False)+"\n")


for example in alpaca_examples:
    of.write(json.dumps(example,ensure_ascii=False)+"\n")


for example in gpt4_examples:
    new_example={"instruction":example["real_prompt"],"input":"","output":example["answer"]["choices"][0]["message"]["content"]}
    of.write(json.dumps(new_example,ensure_ascii=False)+"\n")

for example in gpt4_examples[:1000]:
    new_example={"instruction":example["real_prompt"],"input":"","output":example["answer"]["choices"][0]["message"]["content"]}
    valid_of.write(json.dumps(new_example,ensure_ascii=False)+"\n")