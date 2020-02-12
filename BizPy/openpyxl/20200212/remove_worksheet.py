from openpyxl import load_workbook

wb = load_workbook('copied_worksheets.xlsx')
for ws in wb.worksheets:
    print(f'ワークシート名: {ws.title}')
    if ws.title.endswith('Copy'):
        print(f'{ws.title} を削除します')
        wb.remove(ws)

wb.save('copied_worksheets.xlsx')
