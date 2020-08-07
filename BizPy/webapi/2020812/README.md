
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


## requests

[requests](https://requests.readthedocs.io/en/master/) というライブラリを HTTP クライアントに使って Web API を呼び出している。
requests を使う理由は、[Python の標準ライブラリを使う](https://docs.python.org/ja/3/library/urllib.request.html#examples) よりも簡単にコードが書けるから。

> 参考 The Requests package is recommended for a higher-level HTTP client interface.
> 
> [http.client のドキュメント](https://docs.python.org/ja/3/library/http.client.html) にもそう書いてある。

```bash
$ pip install requests
```

### Content-Type 

> application/x-www-form-urlencoded、application/json形式でのPOSTを受け付けます。

[Content-Type](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Content-Type) とは、
HTTP プロトコルで扱うデータのことをリソースと呼ぶ。
リソースのメディア種別を示すために使うヘッダーになる。

* HTTP リクエストの場合は送るデータの種別を指す
* HTTP レスポンスの場合は受け取るデータの種別を指す

実際にリクエストヘッダーとデータのフォーマットをみてみる。

```python
headers = get_headers(ContentType.URLENCODED)
r = requests.post(URL, headers=headers, data=data)
pprint(r.request.headers)
pprint(r.request.body)
```

## gooラボさんの日本語解析 API を試す

![](https://u.xgoo.jp/img/sgoo.png)

### 利用方法

基本的に GitHub アカウントがあれば API を呼び出すときに必要なアプリケーションIDを取得できる。

* [gooラボAPI利用方法](https://labs.goo.ne.jp/apiusage/)

### 日本語解析 API 一覧

それぞれのドキュメントを読みながら実際に動かしてみる。

* [形態素解析API](https://labs.goo.ne.jp/api/jp/morphological-analysis/)
* [固有表現抽出API](https://labs.goo.ne.jp/api/jp/named-entity-extraction/)
* [ひらがな化API](https://labs.goo.ne.jp/api/jp/hiragana-translation/)
* [キーワード抽出API](https://labs.goo.ne.jp/api/jp/keyword-extraction/)
* [時刻情報正規化API](https://labs.goo.ne.jp/api/jp/time-normalization)
* [テキストペア類似度API](https://labs.goo.ne.jp/api/textpair_doc)
* [スロット値抽出API](https://labs.goo.ne.jp/api/jp/slot-value-extraction/)


## Python プログラミング Tips

### [enum: 列挙型](https://docs.python.org/ja/3/library/enum.html)

グルーピングされた定数の宣言などに使うとコードの見通しがよくなる。

```python
class OperatingSystem(Enum):
    WINDOWS = 'win'
    MAC_OS = 'mac'
    LINUX = 'linux'
```

慣習として定数を意図する変数は大文字で書く。


## 日本語の形態素解析ライブラリ

[janome](https://mocobeta.github.io/janome/) がオススメ！

* Pure Python で実装されているのでインストールが簡単
* 辞書も内包しているのでインストールしたらすぐ使える

```bash
$ pip install janome
```
