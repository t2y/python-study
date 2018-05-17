class MetaSubscript(type):

    def __new__(cls, name, bases, namespace, **kwds):
        print('__new__ called')
        return super().__new__(cls, name, bases, dict(namespace))

    def __getitem__(cls, params):
        print('__getitem__ called')
        cls.params = params
        return cls.__class__(cls.__name__, cls.__bases__, cls.__dict__)

class MyGeneric(metaclass=MetaSubscript):
    pass

g = MyGeneric()
kg = MyGeneric[str]()
kprint(MyGeneric.params)  # <class 'str'>
