# -*- coding: utf-8 -*-
"""
ジェネレーターの利用例
"""


def tuggle():
    """
    >>> g = tuggle()
    >>> next(g)
    True
    >>> next(g)
    False
    >>> next(g)
    True
    """
    r = False
    while True:
        r = not r
        yield r


def file_read(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip('\n')


def modern_style_file_read_with_block(file_name, n):
    with open(file_name) as f:
        for block in iter(lambda: f.read(n), ''):
            yield block


def old_style_file_read_with_block(file_name, n):
    with open(file_name) as f:
        while True:
            block = f.read(n)
            yield block
            if block == '':
                break
