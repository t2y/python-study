# -*- coding: utf-8 -*-
"""
CSV ファイルを読み込んで1行ずつカラム単位に縦に表示する
"""

import csv 


COLUMNS = [
    '全国地方公共団体コード',
    '（旧）郵便番号',
    '郵便番号',
    '都道府県名',
    '市区町村名',
    '町域名',
    '都道府県名',
    '市区町村名',
    '町域名',
    '一町域が二以上の郵便番号',
    '小字毎に番地が起番されている町域',
    '丁目を有する町域',
    '一つの郵便番号で二以上の町域を表す',
    '更新',
    '変更理由',
]


with open('../00_preparation/13TOKYO.CSV', encoding='cp932') as f:
    for line_num, data in enumerate(csv.reader(f), 1):
        print('line number: {0}'.format(line_num))
        for i, column in enumerate(COLUMNS):
            value = data[i]
            length = 36 - len(column)
            print('{0:{length}}: {1}'.format(column, data[i], length=length))
        control_code = input('\nq: quit, Enter: next\n: ')
        if control_code == 'q':
            break
        print()
