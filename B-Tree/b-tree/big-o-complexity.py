"""
Understand Logarithmic time

https://en.wikipedia.org/wiki/Time_complexity#Logarithmic_time
"""
import argparse
import logging
import math
import sys

import matplotlib.pyplot as plt

from utils import handle_keyboard_interrupt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


class Notation:

    def name(self, complexity):
        return '%s: %s' % (self.__class__.__name__, complexity)


class Constant(Notation):

    def __init__(self, color='blue'):
        self.color = color

    def __str__(self):
        return self.name('O(1)')

    def show(self, numbers):
        y = [1] * len(numbers)
        plt.plot(numbers, y, label=self, color=self.color)


class Linear(Notation):

    def __init__(self, color='green'):
        self.color = color

    def __str__(self):
        return self.name('O(n)')

    def show(self, numbers):
        plt.plot(numbers, numbers, label=self, color=self.color)


class Quadratic(Notation):

    def __init__(self, color='orange'):
        self.color = color

    def __str__(self):
        return self.name('O(n^2)')

    def show(self, numbers):
        y = [pow(n, 2) for n in numbers]
        plt.plot(numbers, y, label=self, color=self.color)


class Logarithmic(Notation):

    def __init__(self, base=2, color='red'):
        self.base = base
        self.color = color

    def __str__(self):
        return self.name('O(log n)')

    def compute(self, n):
        if n == 0:
            return 0
        return math.log(n, self.base)

    def show(self, numbers):
        x = numbers
        y = list(map(self.compute, numbers))
        plt.plot(x, y, label=self, color=self.color)


class Linearithmic(Logarithmic):

    def __init__(self, base=2, color='purple'):
        super().__init__(base, color)

    def __str__(self):
        return self.name('O(n log n)')

    def show(self, numbers):
        x = numbers
        y = [n * self.compute(n) for n in numbers]
        plt.plot(x, y, label=self, color=self.color)


Notations = [
    Constant,
    Linear,
    Quadratic,
    Logarithmic,
    Linearithmic,
]

notation_names = [i.__name__ for i in Notations]


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        excludes=[],
        max_num=8,
        verbose=False,
    )

    parser.add_argument(
        '--max-num', dest='max_num', type=int, required=True,
        help='set number of scale',
    )

    parser.add_argument(
        '--exclude', dest='excludes', nargs='*', choices=notation_names,
        help='exclude graphs',
    )

    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode',
    )

    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    return args


def main():
    args = parse_argument()
    log.debug(args)

    numbers = list(range(0, args.max_num + 1))
    notations = filter(lambda n: n.__name__ not in args.excludes, Notations)

    for notation in notations:
        notation().show(numbers)

    plt.title('Big-O Complexity')
    plt.xlabel('Growth of Input')
    plt.ylabel('Complexity')
    plt.legend(loc=2)

    plt.draw()
    plt.pause(1)
    handle_keyboard_interrupt()


if __name__ == '__main__':
    main()
