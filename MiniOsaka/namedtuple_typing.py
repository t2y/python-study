from typing import NamedTuple

Point = NamedTuple('Point', [('x', int),
                             ('y', int)])
p = Point(x=1, y='x')  # Argument has incompatible type "str"; expected "int"
print(p)
