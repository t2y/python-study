
# テスト

[ソフトウェアテスト](https://ja.wikipedia.org/wiki/%E3%82%BD%E3%83%95%E3%83%88%E3%82%A6%E3%82%A7%E3%82%A2%E3%83%86%E3%82%B9%E3%83%88) (以下テスト) はソフトウェア開発の歴史とともに発展してきました。様々な手法があり、分類の仕方もあります。

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

ここではこういったテスト分類の違いを説明しませんが、テスト対象のアプリケーションの特性や組織によってテストの呼び方や内容が異なることもあります。とくに結合テストやシステムテストの内容はチームや組織によって異なることが多いです。

こういったテスト分類の中でももっとも基本的なテスト、且つ重要度も高いものが単体テスト (以下ユニットテスト) です。最近のプログラミング言語ではたいていユニットテストのためのライブラリやツールがあり、そのやり方もプラクティスとして広く共有されています。

Python においても [unittest](https://docs.python.org/ja/3/library/unittest.html) という、まさにその名前の通り、ユニットテストのためのフレームワークが標準ライブラリとして付属しています。

また Python 独自のテストとして [doctest](https://docs.python.org/ja/3/library/doctest.html) と呼ばれるものがあります。doctest はユニットテストの代替にはなりませんが、ビジネスパーソン向けのお手軽なテストとしてお奨めできるものです。


## doctest

[doctest](https://docs.python.org/ja/3/library/doctest.html) は、ドキュメント内に書いたコードをテストにするユニークな仕組みです。

Pythonのモジュール・クラス・関数などの先頭に書く文章のことを **docstring** と呼びます。doctest は docstring に記述したコードをテストのために実行します。

docstring はモジュールや関数の `__doc__` 属性から参照できます。

```python
>>> import utils
>>> print(utils.__doc__)

ここがモジュールレベルの docstring です。
このモジュールはユーティリティ関数を提供します。
```

```python
>>> print(utils.get_entities.__doc__)

    ここが関数の docstring です。
    [[エントリ]] のように二重角括弧で囲まれた文字列を取り出します。

    >>> get_entities("")
    []
    >>> get_entities("括弧でくくられた[[エントリ]]を取り出す")
    ['エントリ']
    >>> get_entities("[[カッコ|括弧]]でくくられた[[エントリ]]を取り出す")
    ['カッコ', 'エントリ']
    >>> get_entities("テストが[[失敗 ]]する例を書く")
    ['失敗']
```

ドキュメントとしてそのモジュールや関数の代表的な使い方を説明するときに実際のコードの利用例を紹介することを考えます。利用例のドキュメントとしても役立ち、ちょっとしたテストにもなるという一石二鳥のようなものです。

### テスト実行例

```bash
$ python utils.py
```

### 使いどころ

汎用的な用途に使える小さい関数 (ユーティリティ関数と呼んだりします) などのドキュメント代わりにテストを書くとよいと思います。

例)

* 日時を扱うような煩雑な処理
* 正規表現の処理のようなパッとみて入出力がわかりにくい処理


## unittest

[unittest](https://docs.python.org/ja/3/library/unittest.html) は、ユニットテストのためのフレームワークです。

> unittest ユニットテストフレームワークは元々 JUnit に触発されたもので、 他の言語の主要なユニットテストフレームワークと同じような感じです。 テストの自動化、テスト用のセットアップやシャットダウンのコードの共有、テストのコレクション化、そして報告フレームワークからのテストの独立性をサポートしています。

doctest はドキュメントのおまけにちょっとしたテストを書くといった用途に使います。ちゃんとしたユニットテストを書くときは unittest を使った方がよいです。

```python
class MyTestCase(unittest.TestCase):

    def test_case1(self):
        expected = 3
        actual = call_some_method(param)
        self.assertEqual(expected, actual)

    def test_case2(self):
        ...
```

`setUp`/`tearDown` といったメソッドを使うことでテストの前処理や後処理を実行することもできます。テストデータを読み込んだり、テストで出力された一時ファイルを削除したりといった用途に使えます。

### テスト実行例

```bash
$ python test_utils.py 
```

### 使いどころ

doctest では面倒なとき、モジュールやクラスなど一定数以上のテストケースを伴うユニットテストを書きたいときなどに使います。

例)

* 一般的なユニットテストを必要とするモジュールや処理
* テストデータを必要とするモジュールや処理

### 余談: PEP 8 に準拠していない標準ライブラリ

[JUnit](https://junit.org/) という、Java 製のテストフレームワークの仕組みをもってきたという歴史的経緯があり、命名規則が [PEP 8](https://pep8-ja.readthedocs.io/ja/latest/) に準拠していません。Python 3 に移行するときに PEP 8 に準拠するように変更しては？といった意見も出たそうですが、既存のテストコードの互換性を壊すほどのメリットはないだろうということで見送られたような話しを聞いた気がします。

PEP 8 が確立する前に作られた古くからあるライブラリなどでは後方互換性を維持する目的のために命名規則に準拠していない場合があります。[threading](https://docs.python.org/ja/3/library/threading.html) ライブラリなどもそう。


## pytest

Python の unittest ライブラリは JUnit に由来するものであることを説明しました。ユニットテストの考え方自体は問題ないけれど、Python と Java の言語の違いに由来する大きな違いとして unittest はテストクラスを作ることを前提とした設計思想の違いがあります。Java はクラスを書かないとプログラミングできないが、Python はそうではありません。

そこで他言語からもってきたものではなく、Python という言語向けに設計されたテストライブラリとして [pytest](https://docs.pytest.org/en/stable/) があります。おそらく Python におけるサードパーティ製のテストライブラリのデファクトスタンダードと呼んでいいと思います。また pytest はユニットテストだけでなく、インテグレーションテスト向けの機能も含んでいます。中規模以上の開発プロジェクトなどでは pytest をテストライブラリとして採用しているプロジェクトも多いです。

pytest は多くの機能を提供していますが、ここではテストを書き始める取っ掛かりとなるよう、ユニットテストに必要な簡単な機能のみの紹介に留めます。

pip コマンドでインストールします。

```bash
$ pip install pytest
```

### 基本はテスト関数と assert 文のみ

Python のデバッグ用の機能として [assert 文](https://docs.python.org/ja/3/reference/simple_stmts.html#the-assert-statement) があります。

pytest ではこの assert 文を使ってテスト結果を検証します。unittest のようにテストクラスを作ったり、専用のアサート関数を使い分けたりする必要はありません。

```python
def test_single_entry():
    expected = ['エントリ']
    actual = get_entities("括弧でくくられた[[エントリ]]を取り出す")
    assert expected == actual
```

これだけでも十分シンプルにテスト関数を実装できます。

### データ駆動テスト

pytest の用語ではパラメーターテストまたはフィクスチャテストと呼ばれています。一般的なテストの用語だと、**データ駆動テスト** と呼ばれたりもします。

テスト関数に対して複数のテストデータをパラメーター化してテストするやり方です。境界値のテストや網羅的なテストに便利です。

```python
@pytest.mark.parametrize('year, month, expected', [
    (2019, 12, date(2019, 12, 31)),
    (2020, 1, date(2020, 1, 31)),
    (2020, 2, date(2020, 2, 29)),
    (2020, 3, date(2020, 3, 31)),
    (2020, 4, date(2020, 4, 30)),
    (2020, 5, date(2020, 5, 31)),
    (2020, 6, date(2020, 6, 30)),
    (2020, 7, date(2020, 7, 31)),
    (2020, 8, date(2020, 8, 31)),
    (2020, 9, date(2020, 9, 30)),
    (2020, 10, date(2020, 10, 31)),
    (2020, 11, date(2020, 11, 30)),
    (2020, 12, date(2020, 12, 31)),
    (2021, 1, date(2021, 1, 31)),
])
def test_last_day_of_month(year, month, expected):
    assert expected == get_last_day_of_month1(year, month)
```

#### リファレンス

* [Parametrizing fixtures and test functions](https://docs.pytest.org/en/stable/parametrize.html)

### フィクスチャテスト

unittest で行ったようなテストデータを読み込むケースもやってみましょう。pytest ではフィクスチャテストと呼んでいます。

`@pytest.fixture` というデコレーターが付いた関数の名前を、他のテスト関数の引数名として使うと自動的に実行結果が引数として渡されます。一見びっくりするようなやり方にみえるかもしれません。pytest ではこういった仕組みを依存性注入 (dependency injection) とも呼んでいます。unittest のやり方とは全く毛色が異なることがわかると思います。

```python
@pytest.fixture
def contents():
    with open('./contents.json') as f:
        data = json.load(f)
    for key in data['query']['pages']:
        revision = data['query']['pages'][key]['revisions'][0]
        contents = revision['*']
        return contents

def test_actual_contents(contents):
    actual = get_entities(contents)
    assert 223 == len(actual)
    assert 'File:Prog_one.png' == actual[0]
    assert 'Category:ソフトウェア開発工程' == actual[-1]
```

組み込みのフィクスチャもいくつか用意されています。例えば `tmp_path` という引数を指定すると、一時ディレクトリへのパスが渡されます。

#### リファレンス

* [pytest fixtures: explicit, modular, scalable](https://docs.pytest.org/en/stable/fixture.html)

### テスト実行例

```bash
$ pytest pytest_utils.py
```

### 使いどころ

pytest は多くの機能をもっているのでシンプルな用途から高度なテストにも使えます。

例)

* unittest のスタイルが好きではない
* ユニットテストよりもさらに複雑なテストを必要とするモジュールや処理


## Python プログラミング Tips

### `-m` オプションでモジュールを実行する

> sys.path から指定されたモジュール名のモジュールを探し、その内容を `__main__` モジュールとして実行します。
> 
> https://docs.python.org/ja/3/using/cmdline.html?#cmdoption-m

#### doctest

次のコードを書かなくても実行できる。

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

これで実行できる。

```python
$ python3 -m doctest utils.py
```

#### unittest

次のコードを書かなくても実行できる。

```python
if __name__ == '__main__':
    unittest.main()
```

これで実行できる。

```python
$ python3 -m unittest -v
```
