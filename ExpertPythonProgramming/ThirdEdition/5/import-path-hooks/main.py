import sys
from importlib.abc import Loader
from importlib.abc import PathEntryFinder
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


class OtherPathEntryFinder(PathEntryFinder):

    def __init__(self, path_entry):
        print(f'{path_entry=}')
        self.path_entry = path_entry

    def find_spec(self, fullname, path, target=None):
        print(f'{fullname=}')
        print(f'{path=}')
        print(f'{target=}')

        path = path or self.path_entry
        if fullname == path:
            name = fullname
            other_module_loader = OtherModuleLoader('other.py')
            return spec_from_loader(name, loader=other_module_loader)


def main():
    print('start')

    print(f'{sys.path_hooks=}')
    sys.path_hooks.append(OtherPathEntryFinder)
    sys.path.insert(0, 'trigger')

    print('===== import trigger module')

    import trigger
    print(trigger.__file__)

    print('end')


if __name__ == '__main__':
    main()
