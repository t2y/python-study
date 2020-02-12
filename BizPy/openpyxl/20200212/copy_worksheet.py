from openpyxl import load_workbook

wb = load_workbook('various_worksheets.xlsx')
for ws in wb.worksheets:
    print(f'{ws.title} をコピーします')
    wb.copy_worksheet(ws)
wb.save('copied_worksheets.xlsx')
