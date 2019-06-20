fruits = {'apple': 200, 'banana': 100, 'melon': 2000}
fruits['watermelon'] = 500
print(fruits)
print(fruits.keys())

"""
【備考】

全てのキー（果物の名前）を取得するための dict のメソッドは keys()
全ての値（果物の値段）を取得するための dict のメソッドは values()
"""

"""
【実行結果】

{'apple': 200, 'banana': 100, 'melon': 2000, 'watermelon': 500}
dict_keys(['apple', 'banana', 'melon', 'watermelon'])
"""
