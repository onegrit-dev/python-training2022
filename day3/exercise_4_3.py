from pathlib import Path

if not Path.exists(Path('sample.txt')):
    raise Exception('ファイルが存在しません。')
