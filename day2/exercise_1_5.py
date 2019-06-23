import random

for _ in range(30):
    x = random.randint(0, 9)
    print(x)
    if x == 0:
        print('ハイ、終了〜！')
        break
else:
    print('ラッキー！0が出ませんでした。')

"""
【実行結果】（例）

1
6
8
2
9
2
4
9
3
9
2
6
5
7
5
5
4
2
8
3
7
8
9
3
6
5
1
1
9
7
ラッキー！0が出ませんでした。
"""
