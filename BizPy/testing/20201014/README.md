
# テスト

[ソフトウェアテスト](https://ja.wikipedia.org/wiki/%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%83%86%E3%82%B9%E3%83%88) はソフトウェアの開発とともに発展してきました。様々な技術や手法があり、分類の仕方もあります。

まずテストを次のように分類してみます。

* 人間が手作業で行って結果を確認するテスト
* テストプログラムを実行して結果を確認するテスト

後者のテストを自動テストと呼ぶこともあります。本日の勉強会で扱うのは自動テストについてです。

さらにテストにはその目的や対象範囲の違いからも分類できます。

* 単体テスト (ユニットテスト)
* 結合テスト (インテグレーションテスト)
* システムテスト
* 受け入れテスト (アクセプタンステスト)
* 機能テスト (ファンクションテスト)
* 性能テスト (パフォーマンステスト)
* 負荷テスト (ストレステスト)

ここではこういったテスト分類の違いを説明しませんが、テスト対象のアプリケーションや組織によってテストの呼び方や内容が異なることもあります。とくに結合テストやシステムテストの内容はチームや組織によって異なることが多いです。

こういったテスト分類の中でももっとも基本的なテスト、且つ重要度も高いものが単体テスト (以下ユニットテスト) です。最近のプログラミング言語ではたいていユニットテストのためのライブラリやツールが標準で付属しているものが多く、そのやり方もプラクティスとして広く共有されています。

Python においても [unittest](https://docs.python.org/ja/3/library/unittest.html) という、まさにその名前の通り、ユニットテストのためのフレームワークが標準ライブラリとして付属しています。

先のテスト手法の分類で言えばユニットテストではありませんが、Python 独自のテストとして [doctest](https://docs.python.org/ja/3/library/doctest.html) と呼ばれるものがあります。ビジネスパーソン向けのテストとして私がお奨めしたい手法としても doctest はお手軽でよいと考えています。




## doctest

[doctest](https://docs.python.org/ja/3/library/doctest.html) は、ドキュメントとテストを組み合わせたユニークな仕組みです。




## unittest




## pytest






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

[requests というサードパーティライブラリ](https://github.com/t2y/python-study/tree/master/BizPy/webapi/20200812#requests) を使って Web API のリクエストを行います。

## HTTP クライアントを共通モジュールとして使う

前回の勉強会で使ったサンプルコードを再利用して汎用の HTTP クライアントとして使えるようにする。

状態をもたないものをクラスとして定義する必要性はないけど、一定の役割をもつ処理をクラスでまとめるとクラス名を1つの名前空間として扱えるので管理しやすくなる。[オブジェクト指向プログラミング](https://ja.wikipedia.org/wiki/%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%8C%87%E5%90%91%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0) と呼ばれるソフトウェアの開発手法の話題になる。難しい話題になるのでここでは扱いません。

```python
from client import HttpClient

client = HttpClient()
data = client.get('https://qiita.com/api/v2/users/t2y', {})
```

## Wikipedia の Web API のドキュメント

* https://www.mediawiki.org/wiki/API:Main_page/ja
* https://www.mediawiki.org/wiki/API:Data_formats/ja

## MediaWiki API 入門

[MediaWiki APIを使ってWikipediaの情報を取得](https://qiita.com/yubessy/items/16d2a074be84ee67c01f) の記事がわかりやすかったのでチュートリアルとしてみるとよいと思います。

この記事を参考にしながら MediaWiki API へ渡すパラメーターをみていきます。

### 記事の本文を取得

Wikipedia のタイトルを指定して記事を習得する。

#### `format` パラメーターの違い

レスポンスのデータフォーマットを `xml` か `json` で選択できる。

* https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0&rvprop=content&format=xml
* https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0&rvprop=content&format=json

#### xml と json の違い

`xml` を提供しているのは歴史的経緯だと推測します。昔は `xml` でも扱われていた。

* 特別な理由がなければ、いまは json を選択するとよいでしょう

このフォーマットによって日本語の文字列の扱いが違うことに気付いたのでみていく。

* xml: 文字コード指定を省略した場合は utf-8/utf-16 でエンコードされているとみなす
* json: Unicode エスケープされた文字列が返される

リファレンス

* https://ja.wikipedia.org/wiki/Extensible_Markup_Language

#### デバッグを容易にするために Web API のレスポンスを dump しておく

プログラムを作成しているとき、コードを修正して実行するといったことを何度も繰り返します。簡単なコードを書くときはそれでも構いませんが、毎回 Web API を呼び出す必要があります。

次のようなデメリットがあります。

* インターネットに接続していないと実行できない
* Web API を呼び出すので (呼び出さない場合と比べて) 実行時間がかかる
* クライアント/サーバーともにマシンリソースを浪費する

そういったとき、レスポンスのデータをローカルファイルとして保存しておくことでこれらの制約やリソースの浪費を回避できます。

```python
json.dump(data, open('contents.json', 'w'))  # ファイルとして保存
```

#### dump したレスポンスをベースにユーティリティ関数を実装する

例えば `contents.json` というファイルで保存したものを使ってコードを書くことで効率よくプログラミングできる。

```python
def test(path='./contents.json'):
    data = json.load(open(path))
    contents = get_contents(data)
    entities = get_entities(contents)
    pprint(entities)


if __name__ == '__main__':
    test()  # モジュールとしてインポートされたときは呼び出されない
```

次のようなユーティリティ関数を作ってみる。

* `get_contents()`: 記事の本文のみを取り出す
* `get_entities()`: 記事のリンクのみを取り出す

#### 実は Web API 用意されてた？！

* 記事からリンクしている記事の一覧を取得するには `prop=links` を指定する
* 記事が属するカテゴリの一覧を取得するには `prop=categories` を指定する

ドキュメントや仕様を確認してからプログラミングしましょう。。。


### キーワードで記事を検索

次のようなパラメーターで Web API を呼び出す。

* https://ja.wikipedia.org/w/api.php?format=xml&action=query&list=search&srsearch=%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0

#### 検索結果とページング

検索結果のような不特定の件数が返る一覧を取得するときは1回の Web API の呼び出しで全件を取得できないことが多い。一般論として、サーバーは多くのクライアントからのリクエストを受け付けるので1回の処理で多くのリソースを浪費してしまうと、同時に多くのリクエストを処理できなくなるからです。Google やヤフーなどの検索結果の画面などをイメージしてください。

MediaWiki API では次のパラメーターで検索結果の位置と件数を指定できる。

* srlimit: 取得する件数
* sroffset: 取得する検索結果の位置

こういった取得件数を制御しながらデータを取得する処理を **ページング** と呼びます。

1回の Web API の呼び出しで取得できない件数の検索結果を取得するときはページングを行って、何度か Web API を呼び出す必要があります。

MediaWiki API では `totalhits` というフィールドに検索結果の件数も返される。

```json
{
  "batchcomplete": "",
  "continue": {
    "sroffset": 100,
    "continue": "-||"
  },
  "query": {
    "searchinfo": {
      "totalhits": 10905
    },
    "search": [
      {
        ...
      }
    ]
  }
}
```

## Python プログラミング Tips

### 文字列のエンコードとデコード

文字列を使ったエンコーディングの操作を試してみる。

Python 3 では文字列は Unicode 文字列として扱われるようになった。例えば、次のように `'プログラミング'` という文字列は Unicode 文字列になる。

プログラミングするときに文字列のエンコーディング (文字コード) を意識する機会は減っている。

```python
>>> s = 'プログラミング'
>>> type(s)
<class 'str'>
```

文字列は str 型になる。

utf-8 でエンコードしたいときは次のようにして bytes 型として変換できる。

```python
>>> b = s.encode('utf-8')
>>> b
b'\xe3\x83\x97\xe3\x83\xad\xe3\x82\xb0\xe3\x83\xa9\xe3\x83\x9f\xe3\x83\xb3\xe3\x82\xb0'
>>> type(b)
<class 'bytes'>
>>> b.decode('utf-8')
'プログラミング'
```

### Python で Unicode エスケープされた文字列を出力する

Unicode エスケープされた文字列として扱いたい場合、`unicode_escape` という特別なエンコーディングを用いてエンコードする。

```python
>>> b = 'プログラミング'.encode('unicode_escape')
>>> b
b'\\u30d7\\u30ed\\u30b0\\u30e9\\u30df\\u30f3\\u30b0'
>>> type(b)
<class 'bytes'>
```

str 型をエンコードしたので bytes 型のデータに変換される。

これを str 型に戻したいときは `ascii` という特別なエンコーディングを指定してデコードする。

```python
>>> s = b.decode('ascii')
>>> s
'\\u30d7\\u30ed\\u30b0\\u30e9\\u30df\\u30f3\\u30b0'
>>> type(s)
<class 'str'>
>>> print(s)
\u30d7\u30ed\u30b0\u30e9\u30df\u30f3\u30b0
```

普通の文字列から Unicode エスケープされた文字列に変換できました。


### 正規表現を使ってみる

[正規表現](https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE) を簡潔に説明すると、ある文字列にマッチするパターンを表現したもの、もしくはその文法と言えます。プログラミングではよく使われる機能の1つなので簡単な正規表現が書けるようになると便利です。

Python では標準ライブラリの [RE モジュール](https://docs.python.org/ja/3/library/re.html) を使って正規表現を扱います。

例えば、`[[` と `]]` で囲まれた文字列にマッチする正規表現は次のようになります。Python で正規表現を記述するときは一般的に文字列の前に  `r` をつけた **Raw 文字列記法** を使います。

```python
> r'\[\[(.*?)\]\]'
```

実際に正規表現を使った実行例。

```python
>>> import re
>>> s = 'インターネット[[チェス]]のプログラム[[Lichess]]の[[人工知能]]のプログラミングの例。'
>>> re.findall(r'\[\[(.*?)\]\]', s)
['チェス', 'Lichess', '人工知能']
```

最初のうちは、ドキュメントを読みながらインタラクティブシェルを使って意図した文字列にマッチするか、実際に実行して正規表現を記述するとよいでしょう。

## リファレンス

* [MediaWiki APIを使ってWikipediaの情報を取得](https://qiita.com/yubessy/items/16d2a074be84ee67c01f)
* [PythonによるWikipediaを活用した自然言語処理](https://www.slideshare.net/ikuyamada/pythonwikipedia-120034699)

