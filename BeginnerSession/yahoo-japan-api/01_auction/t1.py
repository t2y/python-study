# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

import requests

"""
yahoo auction api を呼び出して出品リストを取得する

* http://developer.yahoo.co.jp/webapi/auctions/auction/v2/categoryleaf.html
"""

URL = 'http://auctions.yahooapis.jp/AuctionWebService/V2/categoryLeaf'
APPID = 'your-app-id'
#  オークション > コンピュータ > パソコン > Mac > ノートブック、ノートパソコン > MacBook Air
CATEGORY = 2084286828

params = {
    'appid': APPID,
    'category': CATEGORY,
}
r = requests.get(URL, params=params)
root = ET.fromstring(r.text)
print(root)

for result in root.findall('{urn:yahoo:jp:auc:categoryLeaf}Result'):
    for item in result.findall('{urn:yahoo:jp:auc:categoryLeaf}Item'):
        print('=' * 72)
        title = item.find('{urn:yahoo:jp:auc:categoryLeaf}Title')
        url = item.find('{urn:yahoo:jp:auc:categoryLeaf}ItemUrl')
        price = item.find('{urn:yahoo:jp:auc:categoryLeaf}CurrentPrice')
        print('title: {}'.format(title.text))
        print('price: {}'.format(price.text))
        print('url: {}'.format(url.text))
