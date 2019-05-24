# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (1, 2, 3),
    (3, 4, 7),
    (5, 6, 11),
])
def test_parameter(x, y, expected):
    assert x + y == expected
