import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active

df = pd.read_csv('population.csv')        #←CSVファイルを読み込む
ws.append(df.columns.tolist())        #←ワークシートにヘッダーを追加する
for row in df.values:
    ws.append(list(row))        #←ワークシートに行データを追加する

row_length = 1 + len(df.values)        #←1行目はヘッダーなので行数に1を加算
data = Reference(ws, min_col=2, max_col=2, min_row=1, max_row=row_length)
categories = Reference(ws, min_col=1, max_col=1, min_row=2, max_row=row_length)

chart = BarChart()        #←棒グラフ
chart.type = 'col'
chart.style = 10
chart.shape = 4
chart.title = '都道府県別の人口'        #←グラフのタイトル
chart.x_axis.title = '都道府県'        #←X軸ラベル
chart.y_axis.title = '人口'        #←Y軸ラベル
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'A9')        #←グラフをA列9行目に追加する
wb.save('population_vertical.xlsx')
