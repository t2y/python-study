from datetime import datetime
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 'セル1'        #←ワークシートのA1のセルに直接書き込む

b1 = ws['B1']        #←ワークシートからB1のセルを取得する
b1.value = 3.1        #←B1のセルへ値を書き込む

c1 = ws['C1']
c1.value = datetime.now()        #←現在日時を書き込む

ws.title = 'セル書き込みワークシート'
wb.save('write_cell.xlsx')
