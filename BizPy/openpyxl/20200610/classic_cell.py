import random
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule

wb = Workbook()
ws = wb.active

values = random.sample(range(100), k=10)
for i, value in enumerate(values, 1):
    column_a = ws.cell(i, 1)
    column_a.value = value

row_length = len(values)
sky_blue_fill = PatternFill('solid', start_color='87CEEB', end_color='87CEEB')
less_than_rule = CellIsRule(        #←セルに対する設定
    operator='lessThan',
    formula=[50],
    stopIfTrue=True,
    fill=sky_blue_fill
)
ws.conditional_formatting.add(f'A1:A{row_length}', less_than_rule)

ws.title = 'クラシック(セル)'
wb.save('classic_cell.xlsx')
