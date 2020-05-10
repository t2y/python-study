import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import Series, Reference, BubbleChart

wb = Workbook()
ws = wb.active

df = pd.read_csv('store_sales_share.csv')
ws.append(df.columns.tolist())
for row in df.values:
    ws.append(list(row))

chart = BubbleChart()
chart.style = 18

i = 0
for store in df['店名'].unique():
    min_row = i + 2
    max_row = i + 4
    x = Reference(ws, min_col=3, max_col=3, min_row=min_row, max_row=max_row)
    y = Reference(ws, min_col=4, max_col=4, min_row=min_row, max_row=max_row)
    z = Reference(ws, min_col=5, max_col=5, min_row=min_row, max_row=max_row)
    series = Series(values=y, xvalues=x, zvalues=z, title=store)
    chart.series.append(series)
    i += 3

ws.add_chart(chart, 'A13')
wb.save('store_sales_share_bubble.xlsx')
