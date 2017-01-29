# -*- coding: utf-8 -*-

"""
yield from 構文

* https://www.python.org/dev/peps/pep-0380/
"""

def g1(n):
    for i in range(n):
        yield i


def g2_wrong(n):
    yield g1(n)


def g2_delegate(n):
    """
    値を返すだけならこのコーディングも yield from も同じ
    """
    for i in g1(n):
        yield i


def g2_new_syntax(n):
    yield from g1(n)


def main():
    for i in g2_wrong(3):
        print(i)

    for i in g2_delegate(3):
        print(i)

    for i in g2_new_syntax(3):
        print(i)


if __name__ == '__main__':
    main()
