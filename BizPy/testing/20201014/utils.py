"""
ここがモジュールレベルの docstring です。
このモジュールはユーティリティ関数を提供します。
"""

import calendar
import re
from datetime import date, timedelta

RE_ENTITIES = re.compile(r'\[\[(.*?)\]\]', re.MULTILINE)


def get_entities(contents):
    """
    ここが関数の docstring です。
    [[エントリ]] のように二重角括弧で囲まれた文字列を取り出します。

    >>> get_entities("")
    []
    >>> get_entities("括弧でくくられた[[エントリ]]を取り出す")
    ['エントリ']
    >>> get_entities("[[カッコ|括弧]]でくくられた[[エントリ]]を取り出す")
    ['カッコ', 'エントリ']
    >>> get_entities("テストが[[失敗 ]]する例を書く")
    ['失敗']
    """
    entities = []
    matches = RE_ENTITIES.findall(contents)
    if matches is not None:
        for entity in matches:
            if '|' in entity:
                entity = entity.split('|')[0]
            entities.append(entity)
    return entities



def get_last_day_of_month1(year, month):
    """
    >>> get_last_day_of_month1(2020, 2)
    datetime.date(2020, 2, 29)
    >>> get_last_day_of_month1(2019, 2)
    datetime.date(2019, 2, 28)
    >>> get_last_day_of_month1(2020, 4)
    datetime.date(2020, 4, 30)
    >>> get_last_day_of_month1(2020, 12)
    datetime.date(2020, 12, 31)
    """
    current_month = date(year, month, 1)
    if month == 12:
        return current_month.replace(day=31)

    next_month = current_month.replace(month=current_month.month + 1)
    last_day =  next_month - timedelta(days=1)
    return last_day


def get_last_day_of_month2(year, month):
    """
    >>> get_last_day_of_month2(2020, 2)
    datetime.date(2020, 2, 29)
    >>> get_last_day_of_month2(2019, 2)
    datetime.date(2019, 2, 28)
    >>> get_last_day_of_month2(2020, 4)
    datetime.date(2020, 4, 30)
    >>> get_last_day_of_month2(2020, 12)
    datetime.date(2020, 12, 31)
    """
    month_range = calendar.monthrange(year, month)
    last_day = month_range[1]
    return date(year, month, last_day)


def create_sequence(num):
    """
    引数で渡された値から連番のリストを返します。

    >>> create_sequence(3)
    [0, 1, 2]

    >>> create_sequence(3)  # 単なる文字列のパターンマッチなのでこれはエラー
    [0,1,2]

    >>> create_sequence(100)  # doctest: +ELLIPSIS
    [0, 1, 2, ..., 99]
    """
    return list(range(num))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
