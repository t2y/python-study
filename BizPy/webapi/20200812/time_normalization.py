"""
時刻情報正規化API
https://labs.goo.ne.jp/api/jp/time-normalization
"""
import json
import os
import sys
from enum import Enum

import requests


URL = 'https://labs.goo.ne.jp/api/chrono'

APP_ID = os.environ.get('APP_ID')
if APP_ID is None:
    print('configure APP_ID as environment variable')


class ContentType(Enum):
    JSON = 'application/json'
    URLENCODED = 'application/x-www-form-urlencoded'


def get_headers(content_type):
    return {
        'Content-type': content_type.value
    }


def post_with_urlencoded(data):
    print('application/x-www-form-urlencoded 形式でリクエスト')
    headers = get_headers(ContentType.URLENCODED)
    r = requests.post(URL, headers=headers, data=data)
    print(f'リクエストヘッダー: {r.request.headers}')
    print(f'リクエストボディ: {r.request.body}')
    print(f'レスポンス: {r.json()}')
    print('=' * 72)


def main():
    sentence = sys.argv[1]
    headers = get_headers(ContentType.JSON)
    data = {
        'app_id': APP_ID,
        'sentence': sentence,
        'doc_time': '2020-08-12T09:00:00',
    }

    # urlencoded 形式でリクエスト
    post_with_urlencoded(data)


if __name__ == '__main__':
    main()
