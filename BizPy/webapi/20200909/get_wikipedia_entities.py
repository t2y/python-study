"""
MediaWiki API を使って Wikipedia の記事に含まれるタイトルを取得する
"""
import json
import sys
from pprint import pprint

from client import HttpClient
from utils import get_contents, get_entities

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
        contents = get_contents(data)
        entities = get_entities(contents)
        pprint(entities)
        print('=' * 72)

        print('\nカテゴリのみを出力')
        for category in filter(lambda x: x.startswith('Category:'), entities):
            print(category)


if __name__ == '__main__':
    main()
