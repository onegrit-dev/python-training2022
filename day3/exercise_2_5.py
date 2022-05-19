import openpyxl

# Workbookオブジェクトを新規作成
wb = openpyxl.Workbook()
# 1つ目のシートをWorksheetオブジェクトとして取得
ws = wb.worksheets[0]
# セルA1に値を書き込む
ws['A1'] = 'パイソン'

# Excelファイルを保存
wb.save('Book2.xlsx')
