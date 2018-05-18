from abc import ABCMeta, abstractmethod

class InterfaceGreet(metaclass=ABCMeta):
    """
    Interface like in Python
    """
    @abstractmethod
    def greet(self, other): ...

class Person(InterfaceGreet):
    pass

p = Person() # error: Cannot instantiate abstract class
             # 'Person' with abstract attribute 'greet'
