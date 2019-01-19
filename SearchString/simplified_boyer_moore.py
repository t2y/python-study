"""
Implement simplified Boyer-Moore searching

Reference:
http://www.geocities.jp/m_hiroi/light/pyalgo11.html
"""
import logging
import sys
import timeit

from utils import log
from utils import parse_argument
from utils import find_current_line_end, find_previous_line_end


CSIZE = 256   # byte 単位で比較を行う

# 移動量テーブルの作成
def make_bm_table(pattern, size):
    bm_table = [size] * CSIZE
    size -= 1
    for i in xrange(size):
        bm_table[ord(pattern[i])] = size - i
    return bm_table

# BM 法による探索
def bm_search(buff, pattern):
    n = len(buff) - 1
    m = len(pattern)
    bm_table = make_bm_table(pattern, m)
    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0:
            if buff[i] != pattern[j]: break
            i -= 1
            j -= 1
        if j < 0:
            # 発見
            i = output_line(buff, i + 1) + m - 1
        else:
            i += max(bm_table[ord(buff[i])], m - j)


def make_table(word):
    size = len(word)
    table = [size] * 256
    for i in range(size):
        table[word[i]] = size - i
    return table


def match_word(blob, word, offset, m):
    i = 0
    j = m - 1
    while i < m:
        byte = word[j - i]
        if blob[offset - i] != byte:
            break
        i += 1
    return i == m, byte


def simplified_boyer_moore_search(blob, word, table):
    blob_view = memoryview(blob)
    word_view = memoryview(word)
    n, m = len(blob), len(word)
    end = n - m
    results = []
    i = 0
    cnt = 0
    while i <= end:
        match, byte = match_word(blob_view, word_view, i, m)
        if match:
            prev_line_end = find_previous_line_end(blob_view, i)
            cur_line_end = find_current_line_end(blob_view, i + m, n)
            line = blob_view[prev_line_end:cur_line_end].tobytes()
            results.append(line)
            i = cur_line_end + 1
        else:
            i += table[byte]
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
        results = simplified_boyer_moore_search(blob, byte_word, table)

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
