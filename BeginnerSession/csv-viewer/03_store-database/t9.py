# -*- coding: utf-8 -*-
"""
CSV データをオブジェクトとして扱う
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


class CsvData:

    def __init__(self, common_code, old_zip_code, zip_code,
                 prefecture_kana_name, city_kana_name, town_area_kana_name,
                 prefecture_kanji_name, city_kanji_name, town_area_kanji_name,
                 extra_code1, extra_code2, extra_code3, extra_code4,
                 update_type, update_reason):

        self.common_code = int(common_code)
        self.old_zip_code = old_zip_code
        self.zip_code = zip_code
        self.prefecture_kana_name = prefecture_kana_name
        self.city_kana_name = city_kana_name
        self.town_area_kana_name = town_area_kana_name
        self.prefecture_kanji_name = prefecture_kanji_name
        self.city_kanji_name = city_kanji_name
        self.town_area_kanji_name = town_area_kanji_name
        self.extra_code1 = int(extra_code1)
        self.extra_code2 = int(extra_code2)
        self.extra_code3 = int(extra_code3)
        self.extra_code4 = int(extra_code4)
        self.update_type = int(update_type)
        self.update_reason = int(update_reason)

    def get_row(self):
        return [
            self.common_code,               # 0
            self.old_zip_code.strip(),      # 1
            self.zip_code,                  # 2
            self.prefecture_kana_name,      # 3
            self.city_kana_name,            # 4
            self.town_area_kana_name,       # 5
            self.prefecture_kanji_name,     # 6
            self.city_kanji_name,           # 7
            self.town_area_kanji_name,      # 8
            self.extra_code1,               # 9
            self.extra_code2,               # 10
            self.extra_code3,               # 11
            self.extra_code4,               # 12
            self.update_type,               # 13
            self.update_reason,             # 14
        ]

    def get_row_with_comment(self):
        row = self.get_row()
        return zip(row, COLUMNS)


def store_csv_data(reader):
    if os.path.exists(_DB_FILE):
        os.remove(_DB_FILE)

    conn = sqlite3.connect(_DB_FILE)
    try:
        with conn:
            conn.execute(_CREATE_TABLE)
            for raw_data in reader:
                data = CsvData(*raw_data)
                conn.execute(_INSERT_DATA, data.get_row())
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
