# -*- coding: utf-8 -*-
"""
CLI ツールとしてコマンドライン引数を処理できるようにする
"""

import argparse
import csv
import logging


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

COLUMN_WIDTH = 36

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


def show_csv_data(args):
    with open(args.csv, encoding='cp932') as f:
        for line_num, data in enumerate(csv.reader(f), 1):
            log.info('line number: {0}'.format(line_num))

            for i, column in enumerate(COLUMNS):
                length = COLUMN_WIDTH - len(column)
                print('{0:{length}}: {1}'.format(
                    column, data[i], length=length))

            if args.mode == 'viewer':
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

    show_csv_data(args)


if __name__ == '__main__':
    main()
