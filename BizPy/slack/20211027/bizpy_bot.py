import logging
logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

@app.event("message")
def handle_message_events(ack, body, logger):
    logger.info(f'message: {body}'))

@app.event('app_mention')
def handle_app_mention(body, say, logger):
    logger.info('app_mention: {body}')
    say('はろーわーるど')

if __name__ == '__main__':
    # POST http://localhost:3000/slack/events
    app.start(port=3000, path='/slack/events', http_server_logger_enabled=False)
