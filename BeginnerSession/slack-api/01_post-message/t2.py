# -*- coding: utf-8 -*-
import sys

import requests

"""
URL の生成を構造化して任意のメッセージを投稿する

* https://api.slack.com/methods/chat.postMessage
"""

URL = 'https://slack.com/api/chat.postMessage'
TOKEN = 'xoxp-2445376243-2445376247-81017233411-dac7613762'
CHANNEL = 'C02D3B287'


if len(sys.argv) < 2:
    print('need text message')
    sys.exit(0)

text = sys.argv[1]
params = {
    'token': TOKEN,
    'channel': CHANNEL,
    'text': text,
    'as_user': True,
    'pretty': 1,
}

r = requests.get(URL, params=params)
print(r.text)
