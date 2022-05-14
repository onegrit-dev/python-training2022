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
  File "/Users/akiyoko/PycharmProjects/training1906/day1/exercise_3_7.py", line 7, in <module>
    print(c + d)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

