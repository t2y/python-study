import sys

import pytest

from brute_force_search import brute_force_search
from simplified_boyer_moore import simplified_boyer_moore_search, make_table
from utils import read_hyogo

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


def test_simplified_boyer_moore_search():
    byte_word = '八幡町'.encode('utf-8')
    with read_hyogo() as blob:
        table = make_table(byte_word)
        actual = simplified_boyer_moore_search(blob, byte_word, table)
    assert expected == actual
