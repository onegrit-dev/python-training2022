import random

x = random.randint(1, 7)
if x % 2 == 0:
    print('偶数です。値は{}です。'.format(x))
else:
    print('奇数です。値は{}です。'.format(x))


"""
【実行結果】（例）

奇数です。値は3です。
"""
