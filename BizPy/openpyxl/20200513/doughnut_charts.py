from copy import deepcopy
from openpyxl import Workbook
from openpyxl.chart import DoughnutChart, Reference, Series
from openpyxl.chart.series import DataPoint

sales_data = [
    ['年間売上', 2017, 2018, 2019],
    ['書籍', 65, 55, 45],
    ['文具', 5, 10, 15],
    ['雑貨', 30, 35, 40],
]

def create_data_points():        #←データ要素の作成と書式設定
    book = DataPoint(0)
    book.graphicalProperties.solidFill = '9370DB'        #←MediumPurple

    stationery = DataPoint(1)
    stationery.graphicalProperties.solidFill = 'FFFFE0'        #←LightYellow

    misc = DataPoint(2)
    misc.graphicalProperties.solidFill = 'D2691E'        #←Chocolate
    misc.explosion = 10        #←「要素の切り出し」を10%に設定

    return [book, stationery, misc]

def create_new_chart(base_chart, data, data_points, categories):
            #←作成済みのチャートをコピーしてデータのみ書き換える
    series = Series(data, title_from_data=True)
    series.data_points = data_points
    chart = deepcopy(base_chart)
    chart.title = None
    chart.series.append(series)
    chart.set_categories(categories)
    return chart

def main():
    wb = Workbook()
    ws = wb.active

    for row in sales_data:
        ws.append(row)

    data_points = create_data_points()        #←データ系列を作成
    categories = Reference(ws, min_col=1, min_row=2, max_row=4)        #←判例の範囲指定

    chart_2017 = DoughnutChart()        #←ドーナツグラフ
    data = Reference(ws, min_col=2, min_row=1, max_row=4) #←2017年売上データの範囲指定
    chart_2017.add_data(data, titles_from_data=True)
    chart_2017.set_categories(categories)
    chart_2017.title = 'カテゴリ別年間売上'
    chart_2017.style = 26
    chart_2017.series[0].data_points = data_points        #←データ系列を設定
    ws.add_chart(chart_2017, 'E1')        #←2017年グラフをE列1行目に追加

    data = Reference(ws, min_col=3, min_row=1, max_row=4) #←2018年売上データの範囲指定
    chart_2018 = create_new_chart(chart_2017, data, data_points, categories)
    ws.add_chart(chart_2018, 'E17')        #←2018年グラフをE列17行目に追加

    data = Reference(ws, min_col=4, min_row=1, max_row=4)        #←2019年売上データの範囲指定
    chart_2019 = create_new_chart(chart_2018, data, data_points, categories)
    ws.add_chart(chart_2019, 'E33')        #←2018年グラフをE列33行目に追加
    wb.save('sales_doughnut.xlsx')

if __name__ == '__main__':
    main()
