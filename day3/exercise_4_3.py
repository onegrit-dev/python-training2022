import os.path

if not os.path.exists('sample.txt'):
    raise Exception('ファイルが存在しません。')

# あるいは pathlib を使って

from pathlib import Path

if not Path.exists(Path('sample.txt')):
    raise Exception('ファイルが存在しません。')
