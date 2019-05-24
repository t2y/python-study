# -*- coding: utf-8 -*-
from typing import Dict, List


def f(x: float, y: float) -> Dict[str, int]:
    d = {
        'x': x,
        'y': y,
    }
    return d


def g() -> List[int]:
    numbers = []  # type: List[str]
    for i in range(10):
        numbers.append(i)
    numbers.append('test')
    return numbers


def main() -> None:
    print(f(0.1, 0.2))
    print(g())


if __name__ == '__main__':
    main()
