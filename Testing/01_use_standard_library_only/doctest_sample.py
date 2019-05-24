"""
doctest のサンプルコード

* http://docs.python.jp/3/library/doctest.html
"""

def add(x, y):
    """
    引数に渡したパラメーターを加算した結果を返す

    >>> add(1, 2)
    3
    >>> add(-3, 3)
    0
    """
    return x + y


def get_twenty_list():
    """
    0-19 までの20個の値をもつリストを返す

    >>> len(get_twenty_list())
    20

    >>> get_twenty_list()  # doctest: +ELLIPSIS
    [0, 1, ..., 18, 19]

    >>> get_twenty_list()  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    [0, 1,
     ...,
    18, 19]
    """
    return list(range(20))


if __name__ == '__main__':
    import doctest
    import sys

    flags = doctest.REPORT_NDIFF | doctest.FAIL_FAST
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in globals():
            obj = globals()[name]
        else:
            obj = __test__[name]
        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)
        print("{} failures out of {} tests".format(fail, total))
