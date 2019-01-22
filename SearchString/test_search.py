import sys

import pytest

from boyer_moore_horspool import boyer_moore_horspool_search
from brute_force_search import brute_force_search
from simplified_boyer_moore import simplified_boyer_moore_search
from boyer_moore_sunday import boyer_moore_sunday_search, make_qs_table
from utils import read_hyogo, make_table

expected = list(map(lambda s: s.encode('utf-8'), [
    '28102,"657  ","6570051","ヒョウゴケン","コウベシナダク","ヤハタチョウ","兵庫県","神戸市灘区","八幡町",0,0,1,0,0,0\n',
    '28203,"673  ","6730871","ヒョウゴケン","アカシシ","オオクラハチマンチョウ","兵庫県","明石市","大蔵八幡町",0,0,0,0,0,0\n',
    '28210,"67512","6751204","ヒョウゴケン","カコガワシ","ヤハタチョウカミサイジョウ","兵庫県","加古川市","八幡町上西条",0,0,0,0,0,0\n',
    '28210,"67512","6751203","ヒョウゴケン","カコガワシ","ヤハタチョウシモムラ","兵庫県","加古川市","八幡町下村",0,0,0,0,0,0\n',
    '28210,"67512","6751201","ヒョウゴケン","カコガワシ","ヤハタチョウソウサ","兵庫県","加古川市","八幡町宗佐",0,0,0,0,0,0\n',
    '28210,"67512","6751205","ヒョウゴケン","カコガワシ","ヤハタチョウナカサイジョウ","兵庫県","加古川市","八幡町中西条",0,0,0,0,0,0\n',
    '28210,"67512","6751202","ヒョウゴケン","カコガワシ","ヤハタチョウノムラ","兵庫県","加古川市","八幡町野村",0,0,0,0,0,0\n',
    '28210,"67512","6751206","ヒョウゴケン","カコガワシ","ヤハタチョウフナマチ","兵庫県","加古川市","八幡町船町",0,0,0,0,0,0\n',
]))


def test_brute_force_search():
    byte_word = '八幡町'.encode('utf-8')
    with read_hyogo() as blob:
        actual = brute_force_search(blob, byte_word)
    assert expected == actual


def _boyer_moore_search(search_func, table_func):
    byte_word = '八幡町'.encode('utf-8')
    with read_hyogo() as blob:
        actual = search_func(blob, byte_word, table_func(byte_word))
    assert expected == actual


def test_simplified_boyer_moore_search():
    _boyer_moore_search(simplified_boyer_moore_search, make_table)


def test_boyer_moore_horspool_search():
    _boyer_moore_search(boyer_moore_horspool_search, make_table)


def test_boyer_moore_sunday_search():
    _boyer_moore_search(boyer_moore_sunday_search, make_qs_table)


@pytest.mark.parametrize('word, num', [
    ('八', 104),
    ('八幡', 11),
    ('チョウ', 3229),
    ('65606', 4),
    ('28224', 110),
    ('0', 5223),
    (',', 5223),
])
def test_search_results(word, num):
    byte_word = word.encode('utf-8')
    table = make_table(byte_word)
    qs_table = make_qs_table(byte_word)
    with read_hyogo() as blob:
        bfs = brute_force_search(blob, byte_word)
        sbm = simplified_boyer_moore_search(blob, byte_word, table)
        bmh = boyer_moore_horspool_search(blob, byte_word, table)
        bms = boyer_moore_sunday_search(blob, byte_word, qs_table)
        assert num == len(bfs) == len(sbm) == len(bmh) == len(bms)
        assert bfs == sbm == bmh == bms
