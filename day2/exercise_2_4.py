import random


def roll():
    return random.randint(1, 6)


dice_1 = 0
dice_2 = 0
dice_3 = 0
dice_4 = 0
dice_5 = 0
dice_6 = 0
for _ in range(10000):
    x = roll()
    if x == 1:
        dice_1 += 1
    elif x == 2:
        dice_2 += 1
    elif x == 3:
        dice_3 += 1
    elif x == 4:
        dice_4 += 1
    elif x == 5:
        dice_5 += 1
    elif x == 6:
        dice_6 += 1

print('1が出たのは{}回です。'.format(dice_1))
print('2が出たのは{}回です。'.format(dice_2))
print('3が出たのは{}回です。'.format(dice_3))
print('4が出たのは{}回です。'.format(dice_4))
print('5が出たのは{}回です。'.format(dice_5))
print('6が出たのは{}回です。'.format(dice_6))

"""
【実行結果】

1が出たのは1377回です。
2が出たのは1433回です。
3が出たのは1502回です。
4が出たのは1388回です。
5が出たのは1490回です。
6が出たのは1410回です。
"""
