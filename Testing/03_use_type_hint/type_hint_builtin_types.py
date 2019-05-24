# -*- coding: utf-8 -*-
from typing import List, Set, Dict, Tuple, Text, Optional

# For simple built-in types, just use the name of the type.
i = 1 # type: int
f = 1.0 # type: float
b = True # type: bool
s = "test" # type: str
by = b"test" # type: bytes

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets.
l = [1] # type: List[int]
si = set([6, 7]) # type: Set[int]

# For mappings, we need the types of both keys and values.
d = dict(field=2.0) # type: Dict[str, float]

# For tuples, we specify the types of all the elements.
t = (3, "yes", 7.5) # type: Tuple[int, str, float]

def func(n: int) -> Optional[str]:
    if n == 0:
        return None
    return 'not zero'

# Use Optional for values that could be None.
input_str = func(0)  # type: Optional[str]
if input_str is not None:
   print(input_str)
