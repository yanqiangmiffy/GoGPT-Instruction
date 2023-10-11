# -*- coding: utf-8 -*-
import json

import gradio as gr

title = "搜索生成标注助手"

description = "输入上下文、问题与标注答案，点击submit按钮，可以自动生成面向搜索生成场景的指令数据！"

examples = [
    [
        "普希金从那里学习人民的语言，`吸取了许多有益的养料`，这一切对普希金后来的创作产生了很大的影响。这两年里，普希金创作了不少优秀的作品，如《囚徒》、《致大海》、《致凯恩》和《假如生活欺骗了你》等几十首抒情诗，叙事诗《努林伯爵》，历史剧《鲍里斯·戈都诺夫》，以及《叶甫盖尼·奥涅金》前六章。",
        "著名诗歌《假如生活欺骗了你》的作者是"],
    [
        "普希金从那里学习人民的语言，吸取了许多有益的养料，这一切对普希金后来的创作产生了很大的影响。这两年里，普希金创作了不少优秀的作品，如《囚徒》、《致大海》、《致凯恩》和《假如生活欺骗了你》等几十首抒情诗，叙事诗《努林伯爵》，历史剧《鲍里斯·戈都诺夫》，以及《叶甫盖尼·奥涅金》前六章。",
        "普希金创作的叙事诗叫什么"]
]

answer_example = {
    "instruction": "请基于所提供的支撑信息和对话历史，对给定的问题撰写一个全面且有条理的答复。如果支撑信息或对话历史与当前问题无关或者提供信息不充分，请尝试自己回答问题或者无法回答问题。\n\n",
    "input": "问题：\n\n回答：",
    "output": ""
}

fname = 'data/GoWrite/writer_instruction.json'


def custom_predict(instruction, context, history, question, output):
    input = f"问题：{question}\n\n回答："
    answer_example['instruction'] = input
    answer_example['input'] = ''
    answer_example['output'] = output
    with open(fname, 'r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)

    feeds.append(answer_example)
    with open(fname, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(feeds, ensure_ascii=False,indent=2))
    return answer_example


# 清除输入输出
def clear_input():
    return "", "", "", "", "", "", ""


instructions = [
    "请基于所提供的支撑信息和对话历史，对给定的问题撰写一个全面且有条理的答复。如果支撑信息或对话历史与当前问题无关或者提供信息不充分，请尝试自己回答问题或者无法回答问题。\n\n"
]
# 构建Blocks上下文
with gr.Blocks(theme="Soft") as demo:
    gr.Markdown("# 搜索生成标注助手")
    gr.Markdown("输入上下文与问题后，点击submit按钮，可从上下文中抽取出答案，赶快试试吧！")
    with gr.Column():  # 列排列
        instruction = gr.Dropdown(label="instruction", choices=instructions, value=instructions[0], interactive=True)
        history = gr.Textbox(label="history",value='', interactive=True)
        context = gr.Textbox(label="context", value='',interactive=True)
        question = gr.Textbox(label="question", interactive=True)
        output = gr.Textbox(label="output", interactive=True)
    with gr.Row():  # 行排列
        clear = gr.Button("clear")
        submit = gr.Button("submit")
    with gr.Column():  # 列排列
        answer = gr.Textbox(label="answer")
        # score = gr.Label(label="score")
    # 绑定submit点击函数
    submit.click(fn=custom_predict, inputs=[instruction, context, history, question, output], outputs=[answer])
    # 绑定clear点击函数
    clear.click(fn=clear_input, inputs=[], outputs=[instruction, context, history, question, output])
    # gr.Examples(examples, inputs=[context, question])
    gr.Markdown("感兴趣的小伙伴可以阅读[GoGPT-Instruction](https://github.com/yanqiangmiffy/GoGPT-Instruction)")

demo.launch()
