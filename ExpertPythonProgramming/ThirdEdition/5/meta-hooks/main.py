import sys
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_loader


class OtherModuleLoader(Loader):

    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        print(f'{spec=}')
        return None

    def exec_module(self, module):
        print(f'{module=}')

        with open(self.filename) as f:
            data = f.read()

        _globals = vars(module)
        _globals['__file__'] = self.filename
        exec(data, _globals)


class MyOSModuleLoader(Loader):

    def create_module(self, spec):
        print(f'{spec=}')
        return None

    def exec_module(self, module):
        print(f'{module=}')
        import os


class MyMetaPathFinder(MetaPathFinder):

    def find_spec(self, fullname, path, target=None):
        print(f'{fullname=}')
        print(f'{path=}')
        print(f'{target=}')
        if fullname == 'sub':
            name = 'other'
            other_module_loader = OtherModuleLoader('other.py')
            return spec_from_loader(name, loader=other_module_loader)
        elif fullname == 'os':
            return spec_from_loader('os', loader=MyOSModuleLoader())

        return None


def main():
    print('start')
    sys.meta_path.insert(0, MyMetaPathFinder())

    print('===== import sub module')
    import sub
    print(sub.__file__)
    print()

    print('===== import os module')
    import os  # already sys.modules has os module
    print(sys.modules['os'])

    del sys.modules['os']
    import os
    print(sys.modules['os'])

    print('end')


if __name__ == '__main__':
    main()
