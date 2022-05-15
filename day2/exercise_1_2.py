age = 20
is_student = True

price = 1900
if is_student:
    if age >= 19:
        price = 1500
    else:
        price = 1000

print('価格は{:,}円です。'.format(price))

"""
【実行結果】

価格は1,500円です。
"""
