# -*- coding: utf-8 -*-
import pytest


def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_raise():
    with pytest.raises(ZeroDivisionError):
        1 / 1
