while True:
    input_value = input("""1から3の数字を選択してください。
1: グー
2: チョキ
3: パー
> """)

    if input_value == '1':
        print('あなたはグーを選択しました。')
    elif input_value == '2':
        print('あなたはチョキを選択しました。')
    elif input_value == '3':
        print('あなたはパーを選択しました。')
    else:
        print('正しい数字を選択してください。')
