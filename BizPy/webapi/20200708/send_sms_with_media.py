import os
import sys
import time
from pprint import pprint

from twilio.rest import Client


ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

if ACCOUNT_SID is None or AUTH_TOKEN is None:
    print('configure AUTH_TOKEN as environment variable')


def main():
    from_number=os.environ.get('TRIAL_NUMBER')
    to_number = sys.argv[1]
    body = sys.argv[2]
    media_url = [
        'https://pbs.twimg.com/profile_images/1243612485/bangasa320x240_400x400.jpg'
    ]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=from_number,
        to=to_number,
        media_url=media_url)

    pprint(vars(message))


if __name__ == '__main__':
    main()
