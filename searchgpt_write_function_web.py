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
    "input": "对话历史：\n\n支撑信息：\n\n问题：\n\n回答：",
    "output": ""
}

fname = 'data/GoWrite/write_functions.json'


def custom_predict(instruction, context, history, question, output):
    input = f"结合上文内容：{context}，{instruction}原文如下：{question}\n\n答案：\n\n"
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
    "请续写以下文本，延续其情节、主题或故事。您可以继续发展现有情节，添加新内容，但请保持与原文的一致性,只输出答案，不用回复额外信息。",
    "请帮我扩展以下文本，使其更详细、更具信息量，或者提供更多相关背景信息。\n\n您可以加入例子、细节、引用或解释来扩展原文,只输出答案，不用回复额外信息。",
    "请帮我为以下文本写一段总结\n\n总结应该以简明扼要的方式呈现，并传达原文的主旨，字数不超过50字,只输出答案，不用回复额外信息。",
    "请帮我润色以下文本，使其更流畅、更自然，并确保语法和拼写错误得到纠正。\n\n例如更改句子结构、修改措辞，替换词语、使用高级句法等,只输出答案，不用回复额外信息。",
    "请帮我纠正以下文本中的拼写和语法错误。\n\n请特别关注拼写错误、标点符号问题、主谓一致性等方面的错误，不用提供改正建议,只输出答案，不用回复额外信息,没有错误直接输出原文。"
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
