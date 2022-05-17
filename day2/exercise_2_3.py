while True:
    input_value = input("""次のいずれかの数字を選択してください。
1: グー
2: チョキ
3: パー
9: 終了
> """)

    if input_value == '1':
        print('あなたはグーを選択しました。')
    elif input_value == '2':
        print('あなたはチョキを選択しました。')
    elif input_value == '3':
        print('あなたはパーを選択しました。')
    elif input_value == '9':
        break
    else:
        print('正しい数字を選択してください。')
