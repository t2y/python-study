import json
from datetime import date

import pytest

from utils import get_entities
from utils import get_last_day_of_month1


def test_single_entry():
    expected = ['エントリ']
    actual = get_entities("括弧でくくられた[[エントリ]]を取り出す")
    assert expected == actual


@pytest.fixture
def contents():
    with open('./contents.json') as f:
        data = json.load(f)
    for key in data['query']['pages']:
        revision = data['query']['pages'][key]['revisions'][0]
        contents = revision['*']
        return contents


def test_actual_contents(contents):
    actual = get_entities(contents)
    assert 223 == len(actual)
    assert 'File:Prog_one.png' == actual[0]
    assert 'Category:ソフトウェア開発工程' == actual[-1]


@pytest.mark.parametrize('year, month, expected', [
    (2019, 12, date(2019, 12, 31)),
    (2020, 1, date(2020, 1, 31)),
    (2020, 2, date(2020, 2, 29)),
    (2020, 3, date(2020, 3, 31)),
    (2020, 4, date(2020, 4, 30)),
    (2020, 5, date(2020, 5, 31)),
    (2020, 6, date(2020, 6, 30)),
    (2020, 7, date(2020, 7, 31)),
    (2020, 8, date(2020, 8, 31)),
    (2020, 9, date(2020, 9, 30)),
    (2020, 10, date(2020, 10, 31)),
    (2020, 11, date(2020, 11, 30)),
    (2020, 12, date(2020, 12, 31)),
    (2021, 1, date(2021, 1, 31)),
])
def test_last_day_of_month(year, month, expected):
    assert expected == get_last_day_of_month1(year, month)
