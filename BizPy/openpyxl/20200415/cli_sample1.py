import openpyxl
import glob
import pandas as pd
import os
import numpy as np

import pathlib
import sys
#－－－－－－－－－－－－－－－－－－－－－－－
# https://sabopy.com/py/pandas_1/
#datafile_list  = glob.glob(r'*.xlsx')
#print(datafile_list)

# sortしている
# datafile_list.sort()
# print(datafile_list)
#-------------------------------------------------------------------


def get_xlsx_files(path):
    for po in path.iterdir():
        if po.is_dir():
            print(f'sub dir: {po}')
            yield from get_xlsx_files(po)
        elif po.match('*.xlsx'):
            print(f' - found!: {po}')
            yield po
        else:
            print(f' - what?: {po}')


#エクセルの読み込みと書き込み、そして保存する関数
#エクセルファイルを開く
def openFile(dir_name):
    global sheet
    global wb
    #fileType = [("excel", "*.xlsx")]
    #iDir = "/Users/Desktop/"
    #filePath = tkinter.filedialog.askopenfilename(filetypes = fileType, initialdir = iDir)
    print(f'directory: {dir_name}')
    path = pathlib.Path(dir_name)
    for path in get_xlsx_files(path):
        print(f'{path}')
        wb = openpyxl.load_workbook(str(path))
        sheet1 = wb.active
        print(sheet1)
        getData()
#-------------------------------------------------------------------

#ExcelファイルのDataを取得
def getData ():
    global u
    global sheet2
    
#データを入れるためのシートを作る
    wb.create_sheet(index=2, title="Copy Data")
    sheet2 = wb["Copy Data"]
    print(sheet2)
#-------------------------------------------------------------------

#入れ物の作成
    sheet1 = wb.active
    u = np.zeros((sheet1.max_column, sheet1.max_row)).reshape(sheet1.max_column, sheet1.max_row)
  #  u = np.array(sheet)


#-------------------------------------------------------------------

#データを入れるためのシートを作る
#Excelファイルを名前をつけて保存する
def saveFile():
    wb.create_sheet(index=3, title="Copy Data")
    sheet2 = wb["Copy Data"]
#-------------------------------------------------------------------

# シートにデータを貼り付ける
    sheet1 = wb.active
    for i in range(1, sheet1.max_column+1):
        for j in range(1, sheet1.max_row+1):
            sheet2.cell(row=j, column=i).value = u[i-1][j-1]

# セルへ書き込む
# シート変数[セル記号] = 書き込む値
# シート変数.cell(row=行,column=列).value = 書き込む値
    for i in range(13,19):
        sheet2.cell(column=1,row=i-12).value=sheet1["C3"].value
        sheet2.cell(column=2,row=i-12).value=sheet1["E3"].value
        sheet2.cell(column=6,row=i-12).value='=C6*(C7+C8)'
          
        # 縦データを横向きに出力(15は横にとばす、１００は縦にとばす)
        for j in range(1,43):
            if sheet1.cell(column=i, row=j).value is None:
                sheet1.cell(column=i, row=j).value=0
            sheet2.cell(column=15+j,row=i-12).value=sheet1.cell(column=i, row=j).value

            
#新しいExcelファイルを名前をつけて保存する
    closePath = tkinter.filedialog.asksaveasfilename()
    wb.save(closePath+".xlsx")

if len(sys.argv) < 2:
    print(f'引数にディレクトリを指定してください')
    sys.exit(0)

openFile(sys.argv[1])
