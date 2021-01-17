# -*- coding: utf-8 -*-
"""
Python 2.x から 3.x へなるべく移行しやすくするための
__future__ インポートの機能

* http://docs.python.jp/2/library/__future__.html
* http://methane.hatenablog.jp/entry/2014/01/18/Python_2/3_%E4%B8%A1%E5%AF%BE%E5%BF%9C%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AB_%60unicode_literals%60_%E3%82%92%E4%BD%BF%E3%81%86%E3%81%B9%E3%81%8D%E3%81%8B
"""


def main():
    # print statement 
    print 'statement'
    print('statement')

    # division
    print('10 / 3 =', 10 / 3)

    # str/unicode string
    s = 'abc'
    u = u'あいうえお'
    print s, type(s)
    print u, type(u)


if __name__ == '__main__':
    main()
