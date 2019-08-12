import requests
from bs4 import BeautifulSoup

page_data = requests.get('https://book.impress.co.jp/staff_blog/').text
page = BeautifulSoup(page_data, 'lxml')
details = page.select("""
body > div.block-wrap > div.block-content > main > div > div:nth-child(3) > div.block-book-detail-box-body.module-usr-text > div.block-book-detail
""")

for detail in details:
    hrefs = detail.select('h2 > a')
    reprint_messages = detail.select('div.module-book-copy > b')
    hrefs_and_reprints = zip(hrefs, reprint_messages)
    for href, reprint in hrefs_and_reprints:
        print(f'{href["title"]}: {reprint.text}')
