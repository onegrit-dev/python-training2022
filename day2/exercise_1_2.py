import random

x = random.randint(0, 99)
if x % 6 == 0:
    print('6の倍数です。値は{}です。'.format(x))
elif x % 3 == 0:
    print('3の倍数です。値は{}です。'.format(x))
else:
    print('値は{}です。'.format(x))

"""
【実行結果】（例）

3の倍数です。値は15です。
"""
