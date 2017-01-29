# -*- coding: utf-8 -*-

"""
yield from 構文

* https://www.python.org/dev/peps/pep-0380/
"""

def g1(n):
    v = None
    for i in range(n):
        v = 0 if v is None else v
        v = yield i + v
 

def g2_delegate(n):
    """
    send() メソッドはこのジェネレーターに値を送るため、
    ここで値を受け渡すような実装にしないといけない => g2_delegate_kai を参照
    """
    for i in g1(n):
        yield i


def g2_delegate_kai(n):
    """
    途端にジェネレーターの委譲が難しくなった！
    """
    g = g1(n)
    v = yield next(g)
    while True:
        v = yield g.send(v)


def g2_new_syntax(n):
    yield from g1(n)


def main():
    gd = g2_delegate(3)
    print(next(gd))
    print(gd.send(2))
    print(gd.send(4))

    print('-' * 72)

    gn = g2_new_syntax(3)
    print(next(gn))
    print(gn.send(2))
    print(gn.send(4))

    print('-' * 72)

    gdk = g2_delegate_kai(3)
    print(next(gdk))
    print(gdk.send(2))
    print(gdk.send(4))


if __name__ == '__main__':
    main()
