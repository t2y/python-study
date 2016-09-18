# -*- coding: utf-8 -*-
"""
csv モジュールを使って csv データとして読み込んで表示する
"""

import csv


with open('../00_preparation/13TOKYO.CSV', encoding='cp932') as f:
    for line_num, data in enumerate(csv.reader(f), 1):
        print('line number: {0}'.format(line_num))
        print(data)
        control_code = input('\nq: quit, Enter: next\n: ')
        if control_code == 'q':
            break
        print()
