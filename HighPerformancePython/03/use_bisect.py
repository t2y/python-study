# -*- coding: utf-8 -*-
"""
bisect モジュールの紹介

* http://docs.python.jp/3.5/library/bisect.html
"""

import bisect


def index(seq, n):
    """
    >>> l = [0, 1, 2, 3, 3, 3, 4, 5, 6, 7]
    >>> index(l, 3)
    (3, 6)
    """
    return bisect.bisect_left(seq, n), bisect.bisect(seq, n)


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    http://docs.python.jp/3.5/library/bisect.html#other-examplesa

    >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    ['F', 'A', 'C', 'C', 'B', 'A', 'A']
    """
    i = bisect.bisect(breakpoints, score)
    return grades[i]
