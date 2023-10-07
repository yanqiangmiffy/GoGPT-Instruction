#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:quincy qiang
@license: Apache Licence
@file: llm_eval.py
@time: 2023/10/07
@contact: yanqiangmiffy@gamil.com
@software: PyCharm
@description: coding..
"""
import requests

headers = {
    'Authorization': 'Bearer sk-kbT4TxgLiPddxOqpBf687d96237b46F08eC0Fb3c849b42A1',
    'Content-Type': 'application/json',
}

question='日本排放核废水有什么最新消息？'
answer='根据提供的支撑信息和对话历史，以下是关于日本排放核废水的最新消息：\n\n日本于2023年8月24日开始向太平洋排放经过过滤和稀释的核废料冷却水5。这一决定引起了国际社会的广泛关注和质疑67。\n\n日本政府声称该排放的核废水已经经过多核素处理设备（ALPS）处理，并且已经不会再对生态环境和公众健康造成影响6。然而，一些专业人士对此表示质疑，认为核污水中包括氚、锶-90、碳-14在内的多种放射性元素是无法完全消除的6。\n\n一些国家对日本的行为表示强烈谴责，并呼吁国际社会采取行动防止该排放对环境和人类健康产生潜在影响。联合国在这个问题上的不作为以及一些国家的沉默也引发了质疑7。\n\n日本的核废水排放计划引发了关于核能治理机制的争议14。联合国在核能治理中的干预权是有限的，一些专家认为这可能导致国际社会无法有效干预此事件。同时，美国作为日本主要的支持者在该问题上没有站出来反对，这可能涉及到两国的经济关系和美国对维护自身经济利益的考虑23。？'
json_data = {
    'model': 'gpt-4',
    'messages': [
        {
            'role': 'user',
            'content': f'你需要研究评价标准来对模型回答给出分数，满分为1分，最低分为0分。请按照"得分:"这样的形式输出分数。评价标准要求模型回答语句通顺，符合问题要求，同时是真实且没有恶意的。问题是：{question}，模型回答是：{answer}',
        },
    ],
    'stream': False,
}

response = requests.post('https://apejevrp.cloud.sealos.io/v1/chat/completions', headers=headers, json=json_data)

print(response.text)