from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def answer_sms():
    number = request.form['From']
    body = request.form['Body']

    response = MessagingResponse()
    response.message(f'Hello {number}, you said: {body}')
    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
