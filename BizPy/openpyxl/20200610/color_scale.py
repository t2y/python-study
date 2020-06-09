import random
from openpyxl import Workbook
from openpyxl.formatting.rule import ColorScaleRule

wb = Workbook()
ws = wb.active

values = random.sample(range(100), k=20) #←100までの数字のうち、20個をランダムに取得
for i, value in enumerate(values, 1):
    column_a = ws.cell(i, 1)
    column_a.value = value        #←A列に値をセット
    column_b = ws.cell(i, 2)
    column_b.value = value        #←B列に値をセット

row_length = len(values)
two_color_scale = ColorScaleRule(        #←2色スケールの設定
    start_type='min', start_color='FFFFCC',
    end_type='max', end_color='FF8000'
)
ws.conditional_formatting.add(
    f'A1:A{row_length}', two_color_scale
)        #←A列に2色スケールを設定

three_color_scale = ColorScaleRule(        #←3色スケールの設定
    start_type='percentile', start_value=10, start_color='FFFFCC',
    mid_type='percentile', mid_value=50, mid_color='FF8000',
    end_type='percentile', end_value=90, end_color='FF0000'
)
ws.conditional_formatting.add(
    f'B1:B{row_length}', three_color_scale
)        #←B列に3色スケールを設定

ws.title = 'カラースケール'
wb.save('color_scale.xlsx')
