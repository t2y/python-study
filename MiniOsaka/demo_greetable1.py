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

def main() -> None:
    morimoto = Person('もりもと')
    tama = Cat('たま')
    greet_each_other(morimoto, tama)

    anonymous = Anonymous()
    greet_each_other(morimoto, anonymous)
    # error: Argument 2 to "greet_each_other" has incompatible type "Anonymous"; expected "Greetable"
    # note: 'Anonymous' is missing following 'Greetable' protocol member:
    # note:     name

if __name__ == '__main__':
    main()
