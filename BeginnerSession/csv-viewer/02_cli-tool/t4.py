# -*- coding: utf-8 -*-
"""
CLI ツールとして CSV ビューアを使えるようにする
"""

import csv


COLUMNS = [
    '全国地方公共団体コード',
    '（旧）郵便番号',
    '郵便番号',
    '都道府県名（カナ）',
    '市区町村名（カナ）',
    '町域名（カナ）',
    '都道府県名（漢字）',
    '市区町村名（漢字）',
    '町域名（漢字）'
    '一町域が二以上の郵便番号',
    '小字毎に番地が起番されている町域',
    '丁目を有する町域',
    '一つの郵便番号で二以上の町域を表す',
    '更新',
    '変更理由',
]

COLUMN_WIDTH = 40


def main():
    with open('../00_preparation/13TOKYO.CSV', encoding='cp932') as f:
        for line_num, data in enumerate(csv.reader(f), 1):
            print('line number: {0}'.format(line_num))

            for i, column in enumerate(COLUMNS):
                length = COLUMN_WIDTH - len(column)
                print('{0:{length}}: {1}'.format(
                    column, data[i], length=length))

            control_code = input('\nq: quit, Enter: next\n: ')
            if control_code == 'q':
                break
            print()


if __name__ == '__main__':
    main()
