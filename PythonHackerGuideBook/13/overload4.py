import inspect

class Overload:

    def __init__(self):
        self.namespace = {}

    def __call__(self, func):
        spec = inspect.getfullargspec(func)
        self.namespace[len(spec.args)] = func
        def wrapped(*args):
            f = self.namespace.get(len(args))
            if f is None:
                raise NotImplementedError(f'Not defined for {len(args)}')
            return f(*args)
        return wrapped


overload = Overload()

@overload
def add(x, y):
    print(f'{x=} + {y=} = {x + y}')


@overload
def add(x, y, z):
    print(f'{x=} + {y=} + {z=} = {x + y + z}')


@overload
def add(a, b, c, d, e, f, g):
    print(f'{a + b + c + d + e + f + g}')


add(1, 2, 3)
add(1, 2)
add(1, 2, 3, 4, 5, 6, 7)
add(1, 2, 3, 4)
