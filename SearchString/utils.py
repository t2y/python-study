import logging
from contextlib import contextmanager

LINE_SEPARATOR = ord('\n')

PATH_HYOGO = 'data/28HYOGO.CSV'
PATH_KEN_ALL = 'data/KEN_ALL.CSV'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


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


def parse_argument():
    def data_reader_type(typ):
        if typ == 'large':
            return read_ken_all
        return read_hyogo

    import argparse
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        data=read_hyogo,
        measure=False,
        verbose=False,
        word=None,
    )

    parser.add_argument(
        '--data', type=data_reader_type, help='set data type',
    )
    parser.add_argument(
        '--measure', action='store_true',
        help='measure running time by timeit',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode',
    )
    parser.add_argument(
        'word', help='word to search'
    )

    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    return args
