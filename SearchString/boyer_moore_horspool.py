"""
Implement Boyer-Moore Horspool searching

Reference:
http://www.geocities.jp/m_hiroi/light/pyalgo11.html
"""
import logging
import sys
import timeit

from utils import log
from utils import parse_argument
from utils import find_current_line_end, find_previous_line_end
from utils import make_table


def match_word(blob, word, offset, m):
    j = m - 1
    while j >= 0:
        if blob[offset + j] != word[j]:
            break
        j -= 1
    return j < 0


def boyer_moore_horspool_search(blob, word, table):
    blob_view = memoryview(blob)
    word_view = memoryview(word)
    n, m = len(blob), len(word)
    end = n - m
    results = []
    i = 0
    cnt = 0
    while i <= end:
        if match_word(blob_view, word_view, i, m):
            prev_line_end = find_previous_line_end(blob_view, i)
            cur_line_end = find_current_line_end(blob_view, i + m, n)
            line = blob_view[prev_line_end:cur_line_end].tobytes()
            results.append(line)
            i = cur_line_end + 1
        else:
            i += table[blob_view[i + m]]
        cnt += 1
    log.info('ループ回数: %d' % cnt)
    return results


def main():
    args = parse_argument()
    byte_word = args.word.encode('utf-8')
    log.info('検索語: %s' % args.word)
    log.info('検索語のバイト長: %d' % len(byte_word))

    if args.measure:
        log.setLevel(logging.ERROR)

    with args.data() as blob:
        table = make_table(byte_word)
        results = boyer_moore_horspool_search(blob, byte_word, table)

    for result in results:
        log.debug(result.decode('utf-8').strip())
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
