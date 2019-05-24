# -*- coding: utf-8 -*-
from typing import Callable, Iterable, Union, Optional, List

# This is how you annotate a function definition.
def stringify(num: int) -> str:
    return str(num)

# And here's how you specify multiple arguments.
def plus(num1: int, num2: int) -> int:
    return num1 + num2

# Add type annotations for kwargs as though they were positional args.
def f1(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

# This is how you annotate a function value.
x = f1 # type: Callable[[int, float], float]

# A generator function that yields ints is secretly just a function that
# returns an iterable (see below) of ints, so that's how we annotate it.
def f2(n: int) -> Iterable[int]:
    i = 0
    while i < n:
        yield i
        i += 1

# For a function with many arguments, you can of course split it over multiple lines
def send_email(address: Union[str, List[str]],
               sender: str,
               cc: Optional[List[str]],
               bcc: Optional[List[str]],
               subject='',
               body: List[str] = None
               ) -> bool:
    return True
