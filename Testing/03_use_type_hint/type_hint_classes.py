# -*- coding: utf-8 -*-

class MyClass:
   # The __init__ method doesn't return anything, so it gets return
   # type None just like any other method that doesn't return anything.
   def __init__(self) -> None:
       ...
   # For instance methods, omit `self`.
   def my_class_method(self, num: int, str1: str) -> str:
       return num * str1

# User-defined classes are written with just their own names.
x = MyClass() # type: MyClass
