# -*- coding: utf-8 -*-
"""
sqlite を使って CSV データを永続化する
"""

import argparse
import csv
import logging
import os
import sqlite3


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
        '-m', '--mode', choices=['viewer', 'batch', 'store'],
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


_DB_FILE = 'test.db'
_TABLE_NAME = 'zipcode'
_CREATE_TABLE = """
CREATE TABLE %s (
    common_code integer,
    old_zip_code text,
    zip_code text,
    prefecture_kana_name text,
    city_kana_name text,
    town_area_kana_name text,
    prefecture_kanji_name text,
    city_kanji_name text,
    town_area_kanji_name text,
    extra_code1 integer,
    extra_code2 integer,
    extra_code3 integer,
    extra_code4 integer,
    update_type integer,
    update_reason integer
)
""" % (_TABLE_NAME)

_INSERT_DATA = """
INSERT INTO %s VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""" % (_TABLE_NAME)


def convert_data(data):
    return [
        int(data[0]),
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6],
        data[7],
        data[8],
        int(data[9]),
        int(data[10]),
        int(data[11]),
        int(data[12]),
        int(data[13]),
        int(data[14]),
    ]


def store_csv_data(reader):
    if os.path.exists(_DB_FILE):
        os.remove(_DB_FILE)

    conn = sqlite3.connect(_DB_FILE)
    try:
        with conn:
            conn.execute(_CREATE_TABLE)
            for data in reader:
                insert_data = convert_data(data)
                conn.execute(_INSERT_DATA, insert_data)
            # with statement invokes conn.commit() as context manager
    finally:
        conn.close()


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
        elif args.mode == 'store':
            store_csv_data(reader)


if __name__ == '__main__':
    main()
