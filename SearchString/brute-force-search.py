"""
Implement Brute-Force searching

Reference:
http://www.geocities.jp/m_hiroi/light/pyalgo11.html
"""
import sys

from utils import LINE_SEPARATOR
from utils import read_ken_all, read_hyogo
from utils import read_until_line_end

read_data = read_hyogo
# read_data = read_ken_all


def brute_force_search(line, word, n, m):
    i = 0
    end = n - m
    while i < end:
        if line[i:i+m].tobytes() == word:
            return True
        i += 1
    return False


def search(text, word):
    view = memoryview(text)
    n, m = len(text), len(word)
    end = n - 1
    results = []
    while end > 0:
        offset, line = read_until_line_end(view)
        match = brute_force_search(line, word, offset, m)
        if match:
            results.append(line.tobytes())
        view = view[offset:]
        end = end - offset
    return results


def main():
    if len(sys.argv) < 2:
        print('Usage: %s 八幡町' % sys.argv[0])
        sys.exit(0)

    word = sys.argv[1]
    print('検索語: %s' % word)
    with read_data() as text:
        byte_word = word.encode('utf-8')
        print('検索語のバイト長: %d' % len(byte_word))
        results = search(text, byte_word)

    print('検索結果: %d 件' % len(results))
    for result in results:
        print(result.decode('utf-8'), end='')


if __name__ == '__main__':
    main()
