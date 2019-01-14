from contextlib import contextmanager

LINE_SEPARATOR = ord('\n')

PATH_HYOGO = 'data/28HYOGO.CSV'
PATH_KEN_ALL = 'data/KEN_ALL.CSV'


@contextmanager
def read_hyogo():
    with open(PATH_HYOGO, mode='rb') as f:
        yield f.read()


@contextmanager
def read_ken_all():
    with open(PATH_KEN_ALL, mode='rb') as f:
        yield f.read()


def read_until_line_end(byte):
    i = 0
    while byte[i] != LINE_SEPARATOR:
        i += 1
    offset = i + 1
    return offset, byte[0:offset]
