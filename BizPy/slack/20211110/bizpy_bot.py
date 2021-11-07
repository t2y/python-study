from pprint import pformat

import logging
logging.basicConfig(level=logging.INFO)

from slack_bolt import App

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

@app.event('message')
def handle_message_events(ack, body, logger):
    logger.info(f'message: {body}')

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
def handle_open_modal(ack, client, event, body, logger):
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

if __name__ == '__main__':
    # POST http://localhost:3000/slack/events
    app.start(port=3000, path='/slack/events', http_server_logger_enabled=False)
