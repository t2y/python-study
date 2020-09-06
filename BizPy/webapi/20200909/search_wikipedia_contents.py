"""
MediaWiki API を使って Wikipedia の記事を取得する
"""
import json
import sys
from pprint import pprint

from client import HttpClient

URL = 'https://ja.wikipedia.org/w/api.php'


def search(client, keyword):
    titles = []
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srlimit': 100,
        'sroffset': 0,
        'srsearch': keyword,
    }

    while True:
        data = client.get(URL, params)
        if data is None:
            break

        #json.dump(data, open('search.json', 'w'))  # ファイルとして保存
        #pprint(data)
        for item in data['query']['search']:
            titles.append(item['title'])

        totalhits = data['query']['searchinfo']['totalhits']
        print(f'{totalhits=}')
        data_continue = data.get('continue')
        if data_continue is None:
            break

        sroffset = data_continue['sroffset']
        print(f'{sroffset=}')
        if totalhits <= sroffset or 500 == sroffset:
            break

        params['sroffset'] = sroffset

    return titles


def main():
    keyword = sys.argv[1]
    client = HttpClient()

    titles = search(client, keyword)
    pprint(titles)
    print(f'{len(titles)=}')


if __name__ == '__main__':
    main()
