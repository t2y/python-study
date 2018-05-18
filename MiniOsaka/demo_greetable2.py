from typing import List
from typing_extensions import Protocol

class Greetable(Protocol):
    name: str

    def greet(self, other: str) -> None: ...

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self, other: str) -> None:
        print('こんにちはー {}'.format(other))

class Cat:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self, other: str) -> None:
        print('にゃあー {}'.format(other))

class Anonymous:
    def greet(self, other: str) -> None:
        print('やあ {}'.format(other))

def greet_each_other(x: Greetable, y: Greetable) -> None:
    x.greet(y.name)
    y.greet(x.name)

def greet(animals: List[Greetable]) -> None:
    for i, animal in enumerate(animals[:-1]):
        print('=' * 32)
        greet_each_other(animal, animals[i+1])

def main() -> None:
    animals: List[Greetable] = [Person('もりもと'), Cat('たま'), Anonymous()]
    # error: List item 2 has incompatible type "Anonymous"; expected "Greetable"
    # note: 'Anonymous' is missing following 'Greetable' protocol member:
    # note:     name
    greet(animals)

if __name__ == '__main__':
    main()
