import os
import sys
from pprint import pprint

from twilio.rest import Client


ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

if ACCOUNT_SID is None or AUTH_TOKEN is None:
    print('configure AUTH_TOKEN as environment variable')


def main():
    from_number=os.environ.get('TRIAL_NUMBER')
    to_number = sys.argv[1]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        from_=from_number,
        to=to_number)
    pprint(vars(call))


if __name__ == '__main__':
    main()
