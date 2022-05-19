from pathlib import Path

file_path = Path('exercise_2_4.py')
# このファイル自身は「__file__」とも書ける
# file_path = Path(__file__)

print(Path.exists(file_path))

"""
【実行結果】

True
"""
