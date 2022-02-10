from pathlib import Path

# CSVファイルのパス
file_path = Path('N225.csv')

if not Path.exists(file_path):
    raise Exception('ファイルが存在しません。')

lines = []
with open(file_path) as f:
    for line in f.readlines():
        line = line.rstrip()
        lines.append(line.split(','))

# あるいはリスト内法表記を使って

with open(file_path) as f:
    lines = [line.rstrip().split(',') for line in f.readlines()]

print(lines)
print(type(lines))
print(type(lines[0]))
