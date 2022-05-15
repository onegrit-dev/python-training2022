a = 1
b = '2'
print(a + b)

"""
【備考】

print(a + int(b))
あるいは
print(str(a) + b)
とすれば、加算または連結が可能
"""

"""
【実行結果】

Traceback (most recent call last):
  File "C:/Users/akiyoko/PycharmProjects/training2022/day1/exercise_3_7.py", line 3, in <module>
    print(a + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

