from openpyxl import load_workbook

filename = 'various_worksheets.xlsx'
wb = load_workbook(filename, read_only=True)
print(f'{filename} のワークシート情報を読み込みます')

ws0 = wb.worksheets[0]
print(f'{ws0.title} の特定のセルを指定して表示します')

b1 = ws0['b1']        #←B1のセルを読み込む
print(f'B1 ({b1.column}列, {b1.row}行): {b1.value}')

c3 = ws0['c3']        #←C3のセルを読み込む
print(f'C3 ({c3.column}列, {c3.row}行): {c3.value}')

f6 = ws0['f6']        #←F6のセルを読み込む
print(f'F6 ({f6.column}列, {f6.row}行): {f6.value}')
