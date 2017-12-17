"""
Understand B-tree

https://en.wikipedia.org/wiki/B-tree
"""
import argparse
import logging
import math
import sys
import time

import matplotlib.pyplot as plt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


class BinaryTree:

    def _height(self, n):
        if n == 0:
            return 0
        return math.log(n, 2)

    def height(self, numbers):
        x = numbers
        y = list(map(self._height, numbers))
        plt.plot(x, y, label='binary-tree', color='blue')


class BTree:

    def __init__(self, m=3):
        self.m = m

    def label(self, complexity):
        return '%s: %s' % (self.__class__.__name__, complexity)

    def height_best(self, n):
        if n == 0:
            return 0
        return math.log(n, self.m)

    def height_worst(self, n):
        if n == 0:
            return 0

        return math.log(n, (self.m / 2.0))

    def height(self, numbers):
        x = numbers

        best = list(map(self.height_best, numbers))
        plt.plot(x, best, label='best', color='red')

        worst = list(map(self.height_worst, numbers))
        plt.plot(x, worst, label='worst', color='orange')


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        btree_order=3,
        max_num=8,
        verbose=False,
    )

    parser.add_argument(
        '--btree-order', dest='btree_order', type=int, required=True,
        help='set order of b-tree',
    )

    parser.add_argument(
        '--max-num', dest='max_num', type=int, required=True,
        help='set number of scale',
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

    binary_tree = BinaryTree()
    binary_tree.height(numbers)

    btree = BTree(args.btree_order)
    btree.height(numbers)

    plt.title('B-Tree Height')
    plt.xlabel('Growth of Input')
    plt.ylabel('Height')
    plt.legend(loc=2)

    plt.show()


if __name__ == '__main__':
    main()
