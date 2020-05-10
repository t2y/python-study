import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

wb = Workbook()
ws = wb.active

df = pd.read_csv('population.csv')
ws.append(df.columns.tolist())
for row in df.values:
    ws.append(list(row))

row_length = 1 + len(df.values)
data = Reference(ws, min_col=2, max_col=2, min_row=2, max_row=row_length)
categories = Reference(ws, min_col=1, max_col=1, min_row=2, max_row=row_length)

pie = PieChart()
pie.add_data(data, titles_from_data=True)
pie.set_categories(categories)
pie.title = '都道府県別の人口'

ws.add_chart(pie, 'A9')
wb.save('population_pie.xlsx')
