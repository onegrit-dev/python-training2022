import random


def draw_fortune():
    return random.choice(['大吉', '吉', '小吉', '末吉', '凶'])


print(draw_fortune())

"""
【実行結果】（例）

凶
"""
