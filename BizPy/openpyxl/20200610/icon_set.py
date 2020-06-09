import random
from openpyxl import Workbook
from openpyxl.formatting.rule import IconSetRule

wb = Workbook()
ws = wb.active

values = random.sample(range(100), k=20)
for i, value in enumerate(values, 1):
    column_a = ws.cell(i, 1)
    column_a.value = value

row_length = len(values)
rule = IconSetRule(        #←アイコンセットの設定
    '5Arrows', 'percent', [0, 20, 40, 60, 80],
    showValue=None, percent=None, reverse=None
)
ws.conditional_formatting.add(f'A1:A{row_length}', rule)

ws.title = 'アイコンセット'
wb.save('icon_set.xlsx')
