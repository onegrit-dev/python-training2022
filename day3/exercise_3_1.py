hands = {1: 'グー', 2: 'チョキ', 3: 'パー'}
your_hand = None

while True:
    input_value = input("""1から3の数字を選択してください。
1: グー
2: チョキ
3: パー
> """)
    try:
        input_value = int(input_value)
        your_hand = hands[input_value]
        break
    except (ValueError, KeyError):
        continue

print('あなたは{}を選択しました。'.format(your_hand))

"""
【実行結果】（例）

1から3の数字を選択してください。
1: グー
2: チョキ
3: パー
> 1
あなたはグーを選択しました。
"""