from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import FormulaRule

wb = Workbook()
ws = wb.active
ws.cell(2, 1).value = '空白ではない'
ws.cell(4, 1).value = 5.3529

orange_fill = PatternFill('solid', start_color='FFA500', end_color='FFA500')
is_blank_rule = FormulaRule(        #←Excelの数式を用いた設定
    formula=['ISBLANK(INDIRECT(ADDRESS(ROW(), COLUMN())))'],
    stopIfTrue=True,
    fill=orange_fill
)
ws.conditional_formatting.add(f'A1:A5', is_blank_rule)

ws.title = 'クラシック(数式)'
wb.save('classic_formula.xlsx')
