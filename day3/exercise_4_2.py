from pathlib import Path

file_path = Path('sample2.txt')

if not Path.exists(file_path):
    raise Exception('ファイルが存在しません。')

with open(file_path) as f:
    for line in f:
        print(line.rstrip())
