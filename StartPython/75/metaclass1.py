
class MyMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        print(f'{mcs}, called __new__')
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(f'{mcs}, called __prepare__')
        return {'🐙🐙🐙': 'たこ'}

class MyClass(metaclass=MyMeta):
    pass

def test():
    print(vars(MyClass))

if __name__ == '__main__':
    test()
