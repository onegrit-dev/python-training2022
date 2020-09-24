from datetime import datetime

now = datetime.now()
print(now)

print(now.strftime('%Y/%m/%d %H:%M:%S'))

"""
【実行結果】（例）

2019-09-24 13:50:03.675601
2019/09/24 13:51:09
"""
