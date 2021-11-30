import os
from pprint import pformat

import logging
logging.basicConfig(level=logging.INFO)

from slack_bolt import App
from slack_bolt.context.respond import Respond
import requests

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

@app.event('message')
def handle_message_events(ack, body, logger):
    ack()
    logger.info(f'called message')

@app.event('app_mention')
def handle_app_mention(body, say, logger):
    logger.info('app_mention: {body}')
    say('はろーわーるど')

_HOME_VIEW = {
    'type': 'home',
    'blocks': [
        {
           'type': 'section',
           'text': {
               'type': 'mrkdwn',
               'text': "*BizPy ボット* アプリへようこそ :tada:"
           }
        },
        {
            'type': 'divider'
        },
        {
            'type': 'section',
            'text': {
                'type': 'mrkdwn',
                'text': 'ボタンを配置する、section だと位置は右詰めになる？'
            },
            'accessory': {
                'type': 'button',
                'action_id': 'my_buton_click',
                'text': {
                    'type': 'plain_text',
                    'text': 'なにかのボタン'
                },
            },
        },
        {
            'type': 'actions',
            'block_id': 'modal_button_block',
            'elements': [
                {
                    'type': 'button',
                    'action_id': 'open_modal',
                    'text': {
                        'type': 'plain_text',
                        'text': 'モーダル画面を開く',
                    },
                    'style': 'primary',
                },
            ],
        },
    ]
}

@app.event('app_home_opened')
def handle_app_home_opened_events(client, event, body, logger):
    logger.info(pformat(body))
    client.views_publish(user_id=event['user'], view=_HOME_VIEW)

@app.action('my_buton_click')
def handle_click_button(ack, body, logger):
    ack()
    logger.info(pformat(body))

_MODAL_VIEW = {
    'type': 'modal',
    'callback_id': 'my_modal_view',
    'title': {
        'type': 'plain_text',
        'text': 'モーダル画面',
        'emoji': True
    },
    'submit': {
        'type': 'plain_text',
        'text': '実行',
        'emoji': True
    },
    'close': {
        'type': 'plain_text',
        'text': 'キャンセル',
        'emoji': True
    },
    'blocks': [
        {
            'type': 'section',
            'text': {
                'type': 'plain_text',
                'text': 'フォームに入力してください',
                'emoji': True
            }
        },
        {
            'type': 'input',
            'block_id': 'text1',
            'element': {
                'type': 'plain_text_input',
                'action_id': 'my_modal_text_input'
            },
            'label': {
                'type': 'plain_text',
                'text': 'シンプルなテキスト入力',
                'emoji': True
            }
        },
        {
            'type': 'input',
            'block_id': 'radio1',
            'element': {
                'type': 'radio_buttons',
                'options': [
                    {
                        'text': {
                            'type': 'plain_text',
                            'text': ':octopus:',
                            'emoji': True
                        },
                        'value': 'たこ'
                    },
                    {
                        'text': {
                            'type': 'plain_text',
                            'text': ':squid:',
                            'emoji': True
                        },
                        'value': 'いか'
                    },
                    {
                        'text': {
                            'type': 'plain_text',
                            'text': ':seal:',
                            'emoji': True
                        },
                        'value': 'あしか'
                    }
                ],
                'action_id': 'my_modal_radio_buttons'
            },
            'label': {
                'type': 'plain_text',
                'text': '好きな動物を選んでください',
                'emoji': True
            }
        },
    ]
}

@app.action('open_modal')
def handle_open_modal(ack, client, body, logger):
    ack()  # 先に ack を返さないと入力中にタイムアウトしてイベントが再度届く
    logger.info(pformat(body))
    res = client.views_open(
        trigger_id=body['trigger_id'],
        view=_MODAL_VIEW)
    # レスポンスを何に使うかよくわからないけど、一応返ってくる
    logger.info(res.status_code)

@app.view('my_modal_view')
def handle_my_modal_view(ack, body, logger):
    ack()
    # ユーザが入力した値を確認
    logger.info(body['view']['state']['values']['text1'])
    logger.info(body['view']['state']['values']['radio1'])

@app.command('/get-weather')
def handle_get_weather(ack, body, logger, respond):
    ack()
    location = body.get('text', 'ここ')
    logger.info(location)
    respond(
        response_type='ephemeral',  # in_channel または ephemeral
        replace_original=False,  # 新規のメッセージとして扱うかどうか？
        blocks=[
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'{location}の天気は晴れです',
                },
                'accessory': {
                    'type': 'image',
                    'image_url': 'http://placekitten.com/700/500',
                    'alt_text': 'Multiple cute kittens'
                },
            },
        ]
    )

_MODAL_WEATHER_VIEW = {
    'type': 'modal',
    'callback_id': 'weather_view',
    'title': {
        'type': 'plain_text',
        'text': '天気情報のパラメーター',
        'emoji': True
    },
    'submit': {
        'type': 'plain_text',
        'text': '実行',
        'emoji': True
    },
    'close': {
        'type': 'plain_text',
        'text': 'キャンセル',
        'emoji': True
    },
    'blocks': [
        {
            'type': 'section',
            'text': {
                'type': 'plain_text',
                'text': 'フォームに入力してください',
                'emoji': True
            }
        },
        {
            'type': 'input',
            'block_id': 'location',
            'element': {
                'type': 'plain_text_input',
                'action_id': 'wheather',
            },
            'label': {
                'type': 'plain_text',
                'text': '天候を取得する場所',
                'emoji': True
            }
        },
        {
            'type': 'input',
            'block_id': 'date',
            'element': {
                'type': 'datepicker',
                'action_id': 'wheather',
                'placeholder': {
                    'type': 'plain_text',
                    'text': '日付を指定してください'
                }
            },
            'label': {
                'type': 'plain_text',
                'text': '天候を取得する日付'
            }
        },
    ]
}

@app.command('/write-wheather')
def handle_write_wheather(ack, client, body, logger):
    ack()
    logger.info(pformat(body))
    view = _MODAL_WEATHER_VIEW.copy()
    view['private_metadata'] = body['channel_id']
    #view['private_metadata'] = body['response_url']
    res = client.views_open(
        trigger_id=body['trigger_id'],
        view=view)

def call_weather_api(location, date):
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': location,
        'appid': os.environ.get('OPEN_WHEATHER_API_KEY'),
    }
    res = requests.get(endpoint, params=params)
    data = res.json()
    return data

def get_maps_url(lat, lon):
    url = 'https://www.google.com/maps/search/?api=1&query='
    return f'{url}{lat},{lon}'

def get_weather_icon(icon):
    return f'http://openweathermap.org/img/wn/{icon}@2x.png'

@app.view('weather_view')
def handle_weather_view(ack, body, logger, client):
    ack()
    logger.info(pformat(body))
    location = body['view']['state']['values']['location']['wheather']['value']
    date = body['view']['state']['values']['date']['wheather']['selected_date']
    logger.info(f'{location=}, {date=}')

    data = call_weather_api(location, date)
    logger.info(pformat(data))
    coord = data['coord']
    maps_url = get_maps_url(coord['lat'], coord['lon'])
    icon_url = get_weather_icon(data['weather'][0]['icon'])
    desc = data['weather'][0]['description']

    channel = body['view']['private_metadata']
    client.chat_postMessage(
        channel=channel, 
        blocks=[
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'{desc}\n{maps_url}',
                },
                'accessory': {
                    'type': 'image',
                    'image_url': icon_url,
                    'alt_text': desc,
                },
            },
        ]
    )

    #response_url = body['view']['private_metadata']
    #respond = Respond(response_url=response_url)
    #respond('へんしん')

if __name__ == '__main__':
    # POST http://localhost:3000/slack/events
    app.start(port=3000, path='/slack/events', http_server_logger_enabled=False)
