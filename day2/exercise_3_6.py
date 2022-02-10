from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# CSVファイルのパス
file_path = Path('N225.csv')

if not Path.exists(file_path):
    raise Exception('ファイルが存在しません。')

# CSVファイルを読み込んでデータフレームに変換
df = pd.read_csv(file_path, index_col='Date', parse_dates=True)

# グラフを表示
plt.plot(df['Close'])
plt.show()
