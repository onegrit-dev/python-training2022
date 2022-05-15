import csv
from pathlib import Path

# CSVファイルのパス
file_path = Path('N225.csv')

if not Path.exists(file_path):
    raise Exception('ファイルが存在しません。')

lines = []
with open(file_path) as f:
    reader = csv.reader(f)
    for line in reader:
        lines.append(line)

# あるいはリスト内法表記を使って

with open(file_path) as f:
    reader = csv.reader(f)
    lines = [line for line in reader]

print(lines)
print(type(lines))
print(type(lines[0]))
