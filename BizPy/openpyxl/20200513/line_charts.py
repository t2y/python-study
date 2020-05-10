import pandas as pd
from copy import deepcopy
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

wb = Workbook()
ws = wb.active

df = pd.read_csv('monthly_sales.csv')
ws.append(df.columns.tolist())
for row in df.values:
    ws.append(list(row))

row_length = 1 + len(df.values)
data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=row_length)
categories = Reference(ws, min_col=1, min_row=2, max_row=row_length)

chart = LineChart()
chart.grouping = 'stacked'
chart.overlap = 100
chart.title = '月別売り上げ'
chart.y_axis.title = '売上'
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

percent_stacked = deepcopy(chart)
percent_stacked.grouping = 'percentStacked'
percent_stacked.title = '月別売り上げ (100%積み上げ)'

ws.add_chart(chart, 'A9')
ws.add_chart(percent_stacked, 'A25')
wb.save('monthly_sales_line.xlsx')
