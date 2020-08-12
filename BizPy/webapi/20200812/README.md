
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

それぞれの Content-Type のフォーマットの説明は以下のドキュメントを参照。

* `application/x-www-form-urlencoded`: [POST](https://developer.mozilla.org/ja/docs/Web/HTTP/Methods/POST) メソッドの説明に出てくる
* `application/json`: [JSON](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/JSON)　がそう

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

実行例)

```bash
$ python hiragana_translation.py "漢字が混ざっている文章"
application/x-www-form-urlencoded 形式でリクエスト
リクエストヘッダー: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-type': 'application/x-www-form-urlencoded', 'Content-Length': '201'}
リクエストボディ: app_id=XXX&sentence=%E6%BC%A2%E5%AD%97%E3%81%8C%E6%B7%B7%E3%81%96%E3%81%A3%E3%81%A6%E3%81%84%E3%82%8B%E6%96%87%E7%AB%A0&output_type=hiragana
レスポンス: {'converted': 'かんじが まざっている ぶんしょう', 'output_type': 'hiragana', 'request_id': 'labs.goo.ne.jp\t1597191586\t0'}
========================================================================
application/json 形式でリクエスト
リクエストヘッダー: {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-type': 'application/json', 'Content-Length': '187'}
リクエストボディ: {"app_id": "XXX", "sentence": "\u6f22\u5b57\u304c\u6df7\u3056\u3063\u3066\u3044\u308b\u6587\u7ae0", "output_type": "hiragana"}
レスポンス: {'converted': 'かんじが まざっている ぶんしょう', 'output_type': 'hiragana', 'request_id': 'labs.goo.ne.jp\t1597191586\t0'}
========================================================================
```

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

```python
from janome.tokenizer import Tokenizer

t = Tokenizer()
text = 'すもももももももものうち'
for token in t.tokenize(text):
    print(token)
```

```bash
$ python janome_parse.py
すもも	名詞,一般,*,*,*,*,すもも,スモモ,スモモ
も	助詞,係助詞,*,*,*,*,も,モ,モ
もも	名詞,一般,*,*,*,*,もも,モモ,モモ
も	助詞,係助詞,*,*,*,*,も,モ,モ
もも	名詞,一般,*,*,*,*,もも,モモ,モモ
の	助詞,連体化,*,*,*,*,の,ノ,ノ
うち	名詞,非自立,副詞可能,*,*,*,うち,ウチ,ウチ
```
