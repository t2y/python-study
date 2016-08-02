# -*- coding: utf-8 -*-
"""
名前空間の検索
"""

import math
from math import sin


def test1(x):
    """
    >>> test1(3)
    0.1411200080598672

    >>> import dis
    >>> dis.dis(test1)
     23           0 LOAD_GLOBAL              0 (math)
                  3 LOAD_ATTR                1 (sin)
                  6 LOAD_FAST                0 (x)
                  9 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                 12 RETURN_VALUE
    """
    return math.sin(x)


def test2(x):
    """
    >>> test2(3)
    0.1411200080598672

    >>> import dis
    >>> dis.dis(test2)
     38           0 LOAD_GLOBAL              0 (sin)
                  3 LOAD_FAST                0 (x)
                  6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                  9 RETURN_VALUE
    """
    return sin(x)


def test3(x, sin=math.sin):
    """
    >>> test3(3)
    0.1411200080598672

    >>> import dis
    >>> dis.dis(test3)
     53           0 LOAD_FAST                1 (sin)
                  3 LOAD_FAST                0 (x)
                  6 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
                  9 RETURN_VALUE
    """
    return sin(x)


def use_global_sin(n):
    for _ in range(n):
        sin(3)


def use_local_sin(n):
    sin = math.sin
    for _ in range(n):
        sin(3)
