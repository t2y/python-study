from openpyxl import Workbook

wb = Workbook()
ws0 = wb.active
ws0.title = 'ワークシート0'        #←「ワークシート0」はワークブックと一緒に作成される
ws1 = wb.create_sheet('ワークシート1')        #←「ワークシート1」を作成
ws2 = wb.create_sheet('ワークシート2')        #←「ワークシート2」を作成
print(f'ワークシート: {wb.sheetnames}')        #←すべてのワークシート名を表示

wb.active = 2        #←「ワークシート2」を選択されている状態に変更
wb.save('new_worksheets.xlsx')
