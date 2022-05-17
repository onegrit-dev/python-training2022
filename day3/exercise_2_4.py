from datetime import datetime

now = datetime.now()
print(now)

print(now.strftime('%Y/%m/%d %H:%M:%S'))

"""
【実行結果】（例）

2022-05-20 13:50:03.675601
2022/05/20 13:51:09
"""
