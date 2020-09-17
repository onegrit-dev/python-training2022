import random


def draw_fortune():
    return random.choice(['大吉', '吉', '小吉', '末吉', '凶'])


def draw_fortune2():
    x = random.randint(0, 9)
    print(x)
    if x == 9:
        # 9
        return '大吉'
    elif x >= 6:
        # 6, 7, 8
        return '吉'
    elif x >= 4:
        # 4, 5
        return '小吉'
    elif x >= 2:
        # 2, 3
        return '末吉'
    else:
        # 1
        return '凶'


print(draw_fortune())
print(draw_fortune2())

"""
【実行結果】（例）

凶
1
凶
"""
