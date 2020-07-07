
## twilio API を試す

* [無料のTwilioトライアルアカウントの使用方法](https://jp.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)

### SMS を送る

```bash
(twilio) $ python send_sms.py +81XXYYYYZZZZ メッセージ
```

サンプルコード

* [send_sms.py](./send_sms.py)
* [send_sms_with_media.py](./send_sms_with_media.py)
* [answer_sms.py](./answer_sms.py)

内容

* twilio のライブラリ (sdk) のインストール
* 環境変数の扱い
* ドキュメントとソースコードの場所
* デモ

#### リファレンス

* [Twilio SMS Python クイックスタート](https://jp.twilio.com/docs/sms/quickstart/python)
* [メッセージの送信](https://jp.twilio.com/docs/sms/send-messages)
* [TwiML™ for Programmable SMS](https://jp.twilio.com/docs/sms/twiml)

### 電話をかける

サンプルコード

* [make_call.py](make_call.py)
* [answer_phone.py](answer_phone.py)

```bash
(twilio) $ python call.py +818033431243
# 電話がかかってくるのでなんか番号を押せと言っているのでどれでも番号を押すと音楽が再生される
```

twilio の電話番号に電話をかけたときに自動応答させることもできる。
alice は語学が堪能で language='ja-JP' をパラメーターに指定することで日本語も話せる。

> 18 languages and 14 locales

#### リファレンス

* [Programmable Voice クイックスタート for Python](https://jp.twilio.com/docs/voice/quickstart/python)
* [TwiML™ Voice: <Say>](https://www.twilio.com/docs/voice/twiml/say)

### Slack 連携

  * slack の Outgoing WebHooks を使う
  * Autopilot というコンポーネントに設定する

内容

* ドキュメントをみながら設定を一緒にやってみる

#### リファレンス

* [Build a Slackbot with Twilio Autopilot](https://www.twilio.com/blog/build-a-slackbot-with-twilio-autopilot)
* [How to build a chatbot](https://jp.twilio.com/docs/autopilot/guides/how-to-build-a-chatbot)

