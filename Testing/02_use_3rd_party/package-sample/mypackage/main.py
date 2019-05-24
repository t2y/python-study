# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import sys
from os.path import basename

from enum import Enum


__version__ = '0.1.0'


class Color(Enum):
    red = 1
    green = 2
    blue = 3


def get_color(value_or_attribute):
    if value_or_attribute in Color.__members__:
        return getattr(Color, value_or_attribute)

    return Color(int(value_or_attribute))


def main():
    print('I am mypackage.main')
    if len(sys.argv) < 2:
        print('Usage: %s red' % basename(sys.argv[0]))
        return

    value = get_color(sys.argv[1])
    print(value)


if __name__ == '__main__':
    main()
