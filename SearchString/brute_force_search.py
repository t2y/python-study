"""
Implement Brute-Force searching

Reference:
http://www.geocities.jp/m_hiroi/light/pyalgo11.html
"""
import logging
import sys
import timeit
from utils import log
from utils import parse_argument
from utils import read_until_line_end


def brute_force_search(line, word, n, m):
    i = 0
    end = n - m
    while i < end:
        if line[i:i+m].tobytes() == word:
            return True
        i += 1
    return False


def search(blob, word):
    view = memoryview(blob)
    n, m = len(blob), len(word)
    end = n - 1
    results = []
    while end > 0:
        offset, line = read_until_line_end(view)
        match = brute_force_search(line, word, offset, m)
        if match:
            results.append(line.tobytes())
        view = view[offset:]
        end -= offset
    return results


def main():
    args = parse_argument()
    byte_word = args.word.encode('utf-8')
    log.info('検索語: %s' % args.word)
    log.info('検索語のバイト長: %d' % len(byte_word))

    if args.measure:
        log.setLevel(logging.ERROR)

    with args.data() as blob:
        results = search(blob, byte_word)

    for result in results:
        log.info(result.decode('utf-8').strip())
    log.info('検索結果: %d 件' % len(results))


if __name__ == '__main__':
    args = parse_argument()
    if args.measure:
        setup = 'from __main__ import main'
        sec = timeit.timeit('main()', setup=setup, number=10)
        log.setLevel(logging.INFO)
        log.info('実行時間: %f sec' % sec)
    else:
        main()
