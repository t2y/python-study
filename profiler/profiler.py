import inspect
import sys


def add(x, y):
    return x + y


def print_trace(frame, event, arg):
    print('=' * 72)
    print('frame.f_code.co_name:', frame.f_code.co_name)
    print('event:', event)
    print('arg:', arg)
    print('inspect.getargvalues(arg):', inspect.getargvalues(frame))


def main():
    add(3, 2)


if __name__ == '__main__':
    sys.setprofile(print_trace)
    main()
    sys.setprofile(None)
