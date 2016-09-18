# -*- coding: utf-8 -*-
"""
CSV ファイルを読み込んで1行ずつ表示する
"""


with open('../00_preparation/13TOKYO.CSV', encoding='cp932') as f:
    for line in f:
        print(line.strip())
