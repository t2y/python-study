# Slack のインテグレーション

https://api.slack.com/start/overview によると、Slack を拡張する方法として2つのやり方がある。

* ワークフロー
  * プログラミングする必要がない
* Slack API を使って Slack app を開発する
  * プログラミングする必要がある

## ワークフロービルダー

slack クライントでワークフローを作成するためのツール。
次のドキュメントを読み進めながらチュートリアルをこなせば簡単に作成できる。

* https://slack.com/intl/ja-jp/help/articles/360035692513-%E3%83%AF%E3%83%BC%E3%82%AF%E3%83%95%E3%83%AD%E3%83%BC%E3%83%93%E3%83%AB%E3%83%80%E3%83%BC%E3%82%AC%E3%82%A4%E3%83%89

残念ながらこの機能は有料プランでのみ利用できる。
BizPy ワークスペースはフリープランで使っているのでワークフロービルダーは使えない。

有料プランで運用している Slack ワークスペースでデモだけやります。
デモで利用するサンプルのワークフローを作成したワークフロービルダーの画面は次になります。

### ワークフロービルダーを起動する

![](slack-integration-workflow1.png)

### ワークフロービルダーで作成したワークフロー一覧

![](slack-integration-workflow2.png)

### ショートカットからワークフローを選択する

![](slack-integration-workflow-shortcut1.png)

## Slack app

ひとくちに Slack app と言ってもピンからキリまでありそう。

https://api.slack.com/start/building

