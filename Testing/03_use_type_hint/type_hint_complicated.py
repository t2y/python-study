# -*- coding: utf-8 -*-
from typing import Union, Any, List, cast

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type.  Mypy will print an error
# message with the type; remove it again before running the code.
reveal_type(1)  # -> error: Revealed type is 'builtins.int'

# Use Union when something could be one of a few types.
x1 = [3, 5, "test", "fun"]  # type: List[Union[int, str]]

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for.
x2 = mystery_function()  # type: Any

# Use `ignore` to suppress type-checking on a given line, when your
# code confuses mypy or runs into an outright bug in mypy.
# Good practice is to comment every `ignore` with a bug link
# (in mypy, typeshed, or your own code) or an explanation of the issue.
x3 = confusing_function()  # type: ignore # https://github.com/python/mypy/issues/1167

# cast is a helper function for mypy that allows for guidance of how to convert types.
# it does not cast at runtime
a = [4]
b = cast(List[int], a)  # passes fine
c = cast(List[str], a)  # passes fine (no runtime check)
reveal_type(c)  # -> error: Revealed type is 'builtins.list[builtins.str]'
print(c)  # -> [4] the object is not cast

# TODO: explain "Need type annotation for variable" when
# initializing with None or an empty container
