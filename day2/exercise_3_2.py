def calculate_bmi(height, weight):
    bmi = weight / (height / 100) ** 2
    return bmi


print(calculate_bmi(175, 60))

"""
【実行結果】

19.591836734693878
"""
