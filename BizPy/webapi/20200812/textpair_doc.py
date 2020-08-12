"""
テキストペア類似度API
https://labs.goo.ne.jp/api/textpair_doc
"""
import json
import os
import sys
from enum import Enum

import requests


URL = 'https://labs.goo.ne.jp/api/textpair'


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


def post_with_json(data):
    print('application/json 形式でリクエスト')
    headers = get_headers(ContentType.JSON)
    r = requests.post(URL, headers=headers, data=json.dumps(data))
    print(f'リクエストヘッダー: {r.request.headers}')
    print(f'リクエストボディ: {r.request.body}')
    print(f'レスポンス: {r.json()}')
    print('=' * 72)


def main():
    text1 = sys.argv[1]
    text2 = sys.argv[2]
    headers = get_headers(ContentType.JSON)
    data = {
        'app_id': APP_ID,
        'text1': text1,
        'text2': text2,
    }

    # urlencoded 形式でリクエスト
    post_with_json(data)


if __name__ == '__main__':
    main()
