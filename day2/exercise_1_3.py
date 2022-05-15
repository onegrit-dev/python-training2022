age = 2  # 年齢
is_student = False  # 学生かどうか

price = 1900  # 価格
if age < 3:
    price = 0
elif is_student:
    if age >= 19:
        price = 1500
    else:
        price = 1000

print('価格は{:,}円です。'.format(price))

"""
【実行結果】

価格は0円です。
"""
