from typing_extensions import Protocol

class Greetable(Protocol):
    name: str

    def greet(self, other: str) -> None: ...

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

p: Greetable = Person('もりもと')
# error: Incompatible types in assignment (expression has type "Person", variable has type "Greetable")
# note: 'Person' is missing following 'Greetable' protocol member:
# note:     greet
