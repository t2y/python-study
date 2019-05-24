# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import pytest

from mypackage.main import Color, get_color


@pytest.mark.parametrize(("argument", "expected"), [
    # attributes
    ('red', Color.red),
    ('green', Color.green),
    ('blue', Color.blue),

    # values
    ('1', Color.red),
    ('2', Color.green),
    ('3', Color.blue),

], ids=[
    'red is specified as argument',
    'blue is specified as argument',
    'green is specified as argument',

    '1 is specified as argument',
    '2 is specified as argument',
    '3 is specified as argument',
])
def test_get_color_normal(argument, expected):
    actual = get_color(argument)
    assert actual is expected


@pytest.mark.parametrize("argument", [
    'yellow',
    '5',
])
def test_get_color_exception(argument):
    with pytest.raises(ValueError):
        get_color(argument)
