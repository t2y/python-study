# -*- coding: utf-8 -*-
"""
関数を小さく整理してテストを書きやすくする
"""

import argparse
import csv
import logging


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

log_format = '%(asctime)s %(levelname)s %(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)
log = logging.getLogger(__name__)


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        csv=None,
        mode='viewer',
    )

    parser.add_argument(
        '-c', '--csv', required=True,
        help='set csv file',
    )
    parser.add_argument(
        '-m', '--mode', choices=['viewer', 'batch'],
        help='set mode to handle csv data',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode'
    )

    args = parser.parse_args()
    return args


def get_csv_data(reader):
    """
    >>> reader = [['abc', 'def'], ['ghi', 'jkf']]
    >>> expected = [(1, reader[0]), (2, reader[1])]

    >>> actual = list(get_csv_data(reader))
    >>> actual == expected
    True
    """
    for line_num, data in enumerate(reader, 1):
        yield line_num, data


def make_column_text(columns, column_width):
    """
    >>> columns = ['テスト', 'カラムデータ']
    >>> column_width = 10

    >>> expected = [(columns[0], 7), (columns[1], 4)]
    >>> actual = list(make_column_text(columns, column_width))
    >>> actual == expected
    True
    """
    for column in columns:
        length = column_width - len(column)
        yield column, length


def show_csv_data(reader):
    for line_num, data in enumerate(reader, 1):
        log.info('line number: {0}'.format(line_num))

        g = make_column_text(COLUMNS, COLUMN_WIDTH)
        for i, (column, length) in enumerate(g):
            print('{0:{length}}: {1}'.format(
                column, data[i], length=length))

        control_code = input('\nq: quit, Enter: next\n: ')
        log.debug('control code: {0}'.format(control_code))
        if control_code == 'q':
            break
        print()


def main():
    args = parse_argument()
    if args.verbose:
        log.setLevel(logging.DEBUG)
    log.debug(args)

    with open(args.csv, encoding='cp932') as f:
        reader = csv.reader(f)
        if args.mode == 'viewer':
            show_csv_data(reader)
        elif args.mode == 'batch':
            for line_num, data in get_csv_data(reader):
                # something to do
                print(data)


if __name__ == '__main__':
    main()
