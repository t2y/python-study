
# Web API とは

> API (Application Programming Interface) はアプリケーションを利用するときに、外部とのインターフェースとなるものの総称です。
> アプリケーションの提供元が利用者に対して「この機能はこのような仕様で使えます」と定めたものです。
> Web APIは Webで利用する HTTP/HTTPS というプロトコルを使用し、ネットワークを経由して提供される API を指します。

Web API は基本的には1つのリクエストに対して1つのレスポンスを返す仕組み。

Web API を使う SDK (Software Development Kit) というのは、
複数の Web API を呼び出してなんらかの処理を実現したり、
開発者が Web API の仕様を知らなくても使えるように簡潔にしたり、
Web API を呼び出すときに本質ではないいろいろな面倒な処理を隠蔽する意図があったりする。

一般論として SDK を使うとプログラムの中から Web API の呼び出しを簡単にしてくれるものと考えてよい。
SDK も内部的には Web API を呼び出して機能を実現している。

## slack のチャンネルにメッセージを投稿する

これは直接 Web API を呼び出す例として紹介する。

サンプルコード

* [slack_send_message.py](./slack_send_message.py)

```bash
$ python slack_send_message.py てすと
```

[requests](https://requests.readthedocs.io/en/master/) というライブラリを使って Web API を呼び出している。
requests を使う理由は、[Python の標準ライブラリを使う](https://docs.python.org/ja/3/library/urllib.request.html#examples) よりも簡単にコードが書けるから。

> 参考 The Requests package is recommended for a higher-level HTTP client interface.
> 
> [http.client のドキュメント](https://docs.python.org/ja/3/library/http.client.html) にもそう書いてある。

```bash
$ pip install requests
```


# twilio API を試す

これは SDK を使う例として紹介する。

```bash
(twilio) $ pip install twilio
```

* [無料のTwilioトライアルアカウントの使用方法](https://jp.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account)

## SMS を送る

```bash
(twilio) $ python send_sms.py +81XXYYYYZZZZ メッセージ
```

```bash
(twilio) $ python answer_sms.py
(twilio) $ ./ngrok http 5000
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
  * 普通に sms を送る
  * 添付ファイル付きで sms を送る
  * sms の内容に返信する

### リファレンス

* [Twilio SMS Python クイックスタート](https://jp.twilio.com/docs/sms/quickstart/python)
* [メッセージの送信](https://jp.twilio.com/docs/sms/send-messages)
* [TwiML™ for Programmable SMS](https://jp.twilio.com/docs/sms/twiml)

## 電話をかける

サンプルコード

* [make_call.py](make_call.py)
* [answer_phone.py](answer_phone.py)

```bash
(twilio) $ python call.py +818033431243
# 電話がかかってくるのでなんか番号を押せと言っているのでどれでも番号を押すと音楽が再生される
```

内容

* 電話をかける
* 電話に応答する

alice は語学が堪能で language='ja-JP' をパラメーターに指定することで日本語も話せる。

> 18 languages and 14 locales

### リファレンス

* [Programmable Voice クイックスタート for Python](https://jp.twilio.com/docs/voice/quickstart/python)
* [TwiML™ Voice: <Say>](https://www.twilio.com/docs/voice/twiml/say)


## Slack 連携

  * slack の Outgoing WebHooks を使う
  * Autopilot というコンポーネントに設定する

内容

* ドキュメントをみながら設定を一緒にやってみる
* twilio じゃなくても同種のサービスはあちこちにある

### リファレンス

* [Build a Slackbot with Twilio Autopilot](https://www.twilio.com/blog/build-a-slackbot-with-twilio-autopilot)
* [How to build a chatbot](https://jp.twilio.com/docs/autopilot/guides/how-to-build-a-chatbot)

