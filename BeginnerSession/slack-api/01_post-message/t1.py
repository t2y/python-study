# -*- coding: utf-8 -*-

import requests

"""
slack api を呼び出してメッセージを POST する

* https://api.slack.com/methods/chat.postMessage
"""

url = 'https://slack.com/api/chat.postMessage?token=xoxp-2445376243-2445376247-81017233411-dac7613762&channel=C02D3B287&text=%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF%E3%83%BC&pretty=1'
r = requests.get(url)
print(r.text)
