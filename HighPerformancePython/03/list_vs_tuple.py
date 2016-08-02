# -*- coding: utf-8 -*-
"""
リストとタプルの比較
"""


def create_list(n):
    """
    >>> create_list(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return list(range(n))


def create_tuple(n):
    """
    >>> create_tuple(10)
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    """
    return tuple(range(n))


def append_list(n):
    """
    >>> append_list(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    s = []
    for i in range(n):
        s.append(i)
    return s


def append_list_comprehension(n):
    """
    >>> append_list_comprehension(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return [i for i in range(n)]


def concatenate_sequence(s1, s2):
    """
    >>> l1, l2 = list(range(10)), list(range(10, 20))
    >>> concatenate_sequence(l1, l2)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    >>> t1, t2 = tuple(range(10)), tuple(range(10, 20))
    >>> concatenate_sequence(t1, t2)
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    """
    return s1 + s2
