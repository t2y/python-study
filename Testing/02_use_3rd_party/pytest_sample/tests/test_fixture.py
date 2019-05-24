# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def my_args():
    return [1, 2, 3]


def test_fixture(my_args):
    assert len(my_args) == 3
    assert my_args[0] == 1


def test_use_tmpdir(tmpdir):
    print(tmpdir)
    assert True
