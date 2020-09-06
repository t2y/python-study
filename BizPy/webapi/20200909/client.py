"""
HTTP クライアント
"""
from enum import Enum

import requests


class ContentType(Enum):
    JSON = 'application/json'
    URLENCODED = 'application/x-www-form-urlencoded'


class HttpClient:

    def __init__(self, headers={}):
        self.headers = headers

    def _handle_response(self, response):
        if response.ok:
            return response.json()
        # show extra information to confirm error
        print(f'{response.status_code=}, {response.reason=}')

    def get(self, url, params):
        response = requests.get(url, headers=self.headers, params=params)
        return self._handle_response(response)

    def post(self, url, data):
        self.headers['Content-type'] = ContentType.URLENCODED.value
        response = requests.post(url, headers=self.headers, data=data)
        return self._handle_response(response)
