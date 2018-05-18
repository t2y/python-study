from abc import ABCMeta, abstractmethod

class InterfaceGreet(metaclass=ABCMeta):
    """
    Interface like in Python
    """
    @property
    @abstractmethod
    def name(self): ...

    @abstractmethod
    def greet(self, other): ...

class Person(InterfaceGreet):
    name = ''

p = Person() # error: Cannot instantiate abstract class
             # 'Person' with abstract attribute 'greet'
