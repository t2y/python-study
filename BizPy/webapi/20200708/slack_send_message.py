import os
import sys

import requests

"""
slack のチャンネルにメッセージを投稿する

* https://api.slack.com/methods/chat.postMessage
"""

TOKEN = os.environ.get('SLACK_TOKEN')
if TOKEN is None:
    print('configure SLACK_TOKEN as environment variable')

URL = 'https://slack.com/api/chat.postMessage'
CHANNEL = 'C014VCWT5KR'


if len(sys.argv) < 2:
    print('need text message')
    sys.exit(0)


def main():
    text = sys.argv[1]
    data = {
        'token': TOKEN,
        'channel': CHANNEL,
        'text': text,
    }

    response = requests.post(URL, data=data)

    response_data = response.json()
    if response_data['ok']:
        print('メッセージ "{0}" の登録に成功しました'.format(text))
    else:
        print('メッセージ "{0}" の登録に失敗しました'.format(text))
        print(response.text)


if __name__ == '__main__':
    main()
