# -*- coding: utf-8 -*-

"""
ベクトル化

* https://en.wikipedia.org/wiki/Automatic_vectorization
* https://ja.wikipedia.org/wiki/ベクトル化


そうだ！ EuroPython 2011へ行こう
#2　CPythonについてのハンズオン，講演

* http://gihyo.jp/news/report/01/europython2011/0002


Python List Comprehension Vs. Map

* http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map
"""

import string


def use_list_comprehension(letters):
    """
    >>> import string
    >>> use_list_comprehension(string.ascii_letters)  # doctest: +ELLIPSIS
    [97, 98, 99, ..., 88, 89, 90]
    """
    return [ord(i) for i in letters]


def use_map(letters):
    """
    >>> import string
    >>> list(use_map(string.ascii_letters))  # doctest: +ELLIPSIS
    [97, 98, 99, ..., 88, 89, 90]
    """
    return map(ord, letters)
