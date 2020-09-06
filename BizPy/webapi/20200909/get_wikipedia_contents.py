"""
MediaWiki API を使って Wikipedia の記事を取得する
"""
import json
import sys
from pprint import pprint

from client import HttpClient

URL = 'https://ja.wikipedia.org/w/api.php'


def main():
    title = sys.argv[1]
    client = HttpClient()
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'revisions',
        'rvprop': 'content',
        'titles': title,
    }
    data = client.get(URL, params)
    if data is not None:
        pprint(data)
        json.dump(data, open('contents.json', 'w'))  # ファイルとして保存


if __name__ == '__main__':
    main()
