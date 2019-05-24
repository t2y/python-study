# Python の標準ライブラリのみを使う

標準ライブラリとして以下のものがあります。

* [doctest](http://docs.python.jp/3/library/doctest.html)
* [unittest](http://docs.python.jp/3/library/unittest.html)
* [unittest.mock](http://docs.python.jp/3/library/unittest.mock-examples.html)

利点

* doctest はドキュメントと簡単なテストを兼ねるので気軽に書きやすい
* サードパーティーのパッケージをインストールしなくて良い

欠点

* xUnit スタイルのテストしかできない
* 歴史的経緯で unittest は PEP 8 のコーディングスタイルに準拠していない
* サードパーティー製の専用ツールと比べて機能が劣る

ここで紹介するのは簡単な使い方のみです。
ライブラリの機能や詳細についてはドキュメントを参照してください。


## doctest

### 基本的な使い方

doctest は Python オリジナルのドキュメントと簡単なテストを兼用した便利な仕組みです。

簡単な例からみてみます。以下のように Python での複数行コメント (docstring) のドキュメントを書きつつ、 **>>>** の後ろにインタラクティブシェルから実行するような形で実行結果を記述します。

```python
def add(x, y):
    """
    引数に渡したパラメーターを加算した結果を返す

    >>> add(1, 2)
    3
    >>> add(-3, 3)
    0
    """
    return x + y
```

doctest が実装されているモジュールを実行するには以下のように実行します。

    $ python -m doctest doctest_sample.py

ここで何もエラーが出力されなければ、テストが正しいことを表しています。

ただそうは言っても、最初に書いたときはちゃんと実行されているのかどうか不安に思いますよね？そんなときは冗長モードで実行できます。

    $ python -m doctest doctest_sample.py -v
    Trying:
        add(1, 2)
    Expecting:
        3
    ok
    Trying:
        add(-3, 3)
    Expecting:
        0
    ok
    1 items had no tests:
        doctest_sample
    1 items passed all tests:
       2 tests in doctest_sample.add
    2 tests in 2 items.
    2 passed and 0 failed.
    Test passed.

確かに実行されていることを確認できました。それでは docstring 内のテストをわざと失敗するように書き換えてみましょう。

```python
>>> add(1, 2)
5
```

この状態で再度実行してみます。

    $ python -m doctest doctest_sample.py
    **********************************************************************
    File "path/to/01_use_standard_library_only/doctest_sample.py", line 11, in doctest_sample.add
    Failed example:
        add(1, 2)
    Expected:
        5
    Got:
        3
    **********************************************************************
    1 items had failures:
       1 of   2 in doctest_sample.add
    ***Test Failed*** 1 failures.

このようにエラーが表示されました。

### doctest のちょっと便利な使い方

doctest のオプションフラグを使って簡潔な記述ができます。

例えば、以下のように多くの要素をもつリストを返す関数があるとします。

```python
def get_twenty_list():
    """
    0-19 までの20個の値をもつリストを返す

    >>> len(get_twenty_list())
    20
    """
    return list(range(20))
```

要素数のみを確認するのも1つの方法ですが、中身の要素も確認したいとします。

```python
def get_twenty_list():
    """
    0-19 までの20個の値をもつリストを返す

    >>> get_twenty_list()
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    """
    return list(range(20))
```

ここでリストの途中の要素数をわざわざ確認する必要がないときは *ELLIPSIS* というオプションを指定して以下のように記述して doctest を実行できます。

```python
>>> get_twenty_list()  # doctest: +ELLIPSIS
[0, 1, ..., 18, 19]
```

**...** は省略を表すマーカーでどんな文字列にも一致します。

他に知っておくと便利なフラグとして、ドキュメントとして見やすくするために任意の改行を入れられるようにする *NORMALIZE_WHITESPACE* などもあります。

```python
>>> get_twenty_list()  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0, 1,
 ...,
18, 19]
```

### doctest で任意の関数のテストのみを実行する方法

基本的に doctest はファイル全体をまとめてテスト実行する手法ですが、開発途中のときなど任意の関数だけをテストしたいときもあります。

そんなときに [doctest.run_docstring_examples](http://docs.python.jp/3/library/doctest.html#doctest.run_docstring_examples) を使うと良いです。ライブラリドキュメントの [アドバイス](http://docs.python.jp/3/library/doctest.html#soapbox) に良いサンプルコードがあったのでそのまま引用します。

```python
if __name__ == '__main__':
    import doctest
    import sys

    flags = doctest.REPORT_NDIFF | doctest.FAIL_FAST
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in globals():
            obj = globals()[name]
        else:
            obj = __test__[name]
        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)
        print("{} failures out of {} tests".format(fail, total))
```

関数名を指定しないときは全てのテストが実行されます。

    $ python doctest_sample.py
    0 failures out of 5 tests

関数名を引数に指定して、そのテストに失敗したときは以下のようなレポートが出力されます。

    $ python doctest_sample.py add
    **********************************************************************
    File "doctest_sample.py", line 14, in add
    Failed example:
        add(-3, 3)
    Differences (ndiff with -expected +actual):
        - 5
        + 0

*doctest.run_docstring_examples()* の引数に渡す [オプション引数](http://docs.python.jp/3/library/doctest.html#doctest-options) でレポート出力などを制御できます。


### doctest で気をつけること

doctest はとても便利な仕組みですが、この仕組みで全ての単体テストを記述しようと考えないことが重要です。確かにユーティリティ関数などのテストには向いていますが、あくまでドキュメントの延長上にあるものと考える方が適切です。

本当に適切な単体テストを書こうと思ったら正常系、異常系、境界値テストなど、テストケースは多岐に渡ります。それらを全て docstring に記述して検証そのものは確かにできますが、膨大なドキュメント量になってしまう場合があります。

doctest はより分かりやすいドキュメントを書くために関数の使い方も記述するものであり、その使い方が正しく動くことを doctest ライブラリにより検証できるといった考え方で良いです。そのため、その関数の使い方として典型的な呼び出し例などを記述するのが良いでしょう。


## unittest

いわゆる xUnit スタイルのテストライブラリです。

### 基本的な使い方

ライブラリドキュメントからのサンプルコードをそのまま紹介します。

```python
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
```

unittest のテストコードを実行するには以下のように実行します。

    $ python -m unittest unittest_tests/test_sample1.py 
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

どんなテストを実行したか分かるように冗長モードで実行してみます。

    $ python -m unittest unittest_tests/test_sample1.py -v
    test_isupper (unittest_tests.test_sample1.TestStringMethods) ... ok
    test_split (unittest_tests.test_sample1.TestStringMethods) ... ok
    test_upper (unittest_tests.test_sample1.TestStringMethods) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

### サブテスト

テストのを書く手法の1つとして [Data-driven testing](https://en.wikipedia.org/wiki/Data-driven_testing) (データ駆動テスト) と呼ばれる手法があります。あるテスト関数に対して複数の入力 (あるいは出力) をテストデータとして与え、それぞれのパラメーターに対してテスト関数を1回のテスト実行で行うような手法です。あるパラメーターでテストが失敗したとしてもそこでテストが終了するのではなく、他のパラメーターのテストも全て実行できるので1回のテスト実行で全てのパラメーターの結果が分かるのが利点です。

サブテストを使うことでこのデータ駆動テストが行えます。

例えば、素数かどうかを判定する *is_prime()* 関数のテストは以下のように実装できます。

```python
class PrimeTest(unittest.TestCase):

    def test_is_prime(self):
        """
        Test that number is prime or not.
        """
        data = [
            (0, False),
            (1, False),
            (2, True),
            (3, True),
            (4, False),
            (5, True),
            (6, False),
            (7, True),
            (8, False),
            (9, False),
        ]

        for n, expect in data:
            with self.subTest(n=n, expect=expect):
                self.assertEqual(is_prime(n), expect)
```

unittest を実行します。このテストは10個の入力データに対してサブテストが実行されますが、unittest からは1つのテストとして扱われます。

    $ python -m unittest unittest_tests/test_sample2.py -v
    test_is_prime (unittest_tests.test_sample2.PrimeTest) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

ここで *data* のリストにあえて失敗するデータを混ぜてみましょう。

```python
    data = [
        (0, False),
        (1, False),
        (2, True),
        (11, False),
        (3, True),
        (4, False),
        (5, True),
        (15, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
    ]
```

わざと失敗する 11 と 15 のテストデータを追加して実行すると、以下のように全ての失敗したデータのエラーを表示してくれます。

    $ python -m unittest unittest_tests/test_sample2.py -v
    test_is_prime (unittest_tests.test_sample2.PrimeTest) ...
    ======================================================================
    FAIL: test_is_prime (unittest_tests.test_sample2.PrimeTest) (expect=False, n=11)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "path/to/01_use_standard_library_only/unittest_tests/test_sample2.py", line 51, in test_is_prime
        self.assertEqual(is_prime(n), expect)
    AssertionError: True != False

    ======================================================================
    FAIL: test_is_prime (unittest_tests.test_sample2.PrimeTest) (expect=True, n=15)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "path/to/01_use_standard_library_only/unittest_tests/test_sample2.py", line 51, in test_is_prime
        self.assertEqual(is_prime(n), expect)
    AssertionError: False != True

    ----------------------------------------------------------------------
    Ran 1 test in 0.001s

    FAILED (failures=2)

### テスト探索

unittest はシンプルなテスト探索機能も提供しています。前節ではテストファイルを引数に実行しましたが、テストファイルがプロジェクトの最上位からインポート可能なモジュールもしくはパッケージである場合、自動的にテストファイルを検出してテストを実行してくれます。

いま *unittest_tests* は Python のパッケージである (\_\_init\_\_.py をもつ) ため、引数を指定しなくてもそのディレクトリ配下のファイルを検出してテストが実行されます。デフォルトではファイル名に *test* の接頭辞をもつファイルをテストファイルとして検出します。

    $ python -m unittest -v
    test_isupper (unittest_tests.test_sample1.TestStringMethods) ... ok
    test_split (unittest_tests.test_sample1.TestStringMethods) ... ok
    test_upper (unittest_tests.test_sample1.TestStringMethods) ... ok
    test_is_prime (unittest_tests.test_sample2.PrimeTest) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK

### モック

モックを使ってテストの実行時のみ任意の値を返すようにすることもできます。

例えば、以下の *greet()* 関数は実行時の時間によって返り値が変わります。

```python
def greet(name):
    now = datetime.now()
    if now.hour < 12:
        return '%s, good morning' % name
    elif 12 <= now.hour < 16:
        return '%s, good afternoon' % name
    else:
        return '%s, good evening' % name
```

こういった関数の返り値に依存する処理などはモックにある *@patch* デコレーターを使うと便利なときがあります。*greet()* 関数の返り値を任意の値に変更して、それが変わっていることをテストをしてみます。パッチの適用を分かりやすくするため、モンキーパッチを適用した *greet()* 関数のテストをしています。そのため、このテスト自体にはあまり意味はありません。

```python
class GreetingTestCase(unittest.TestCase):

    @patch('unittest_tests.test_sample3.greet')
    def test_greet(self, mock_greet):
        name = 'john'
        expected = '%s, good night' % name

        mock_greet.return_value = expected
        actual = greet(name)
        self.assertEqual(actual, expected)

        # assert greet function is called with this parameter
        mock_greet.assert_called_with(name)
```

パッチを適用するモジュールを指定して *mock_greet.return_value* に返したい任意の値をセットします。

ここで *datetime.now()* の返す値を変更すれば良いのではないかと思うかもしれません。

```python
@patch('datetime.datetime.now')
def test_datetime(self, mock_datetime_now):
    mock_datetime_now.return_value = datetime(2016, 12, 8, 8, 15, 30)
    ...
```

こんな感じに *datetime* オブジェクトをセットするようにして実行してみます。すると、以下のようなエラーが発生しました。

    Traceback (most recent call last):
      File "/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/unittest/mock.py", line 1170, in patched
        patching.__exit__(*exc_info)
      File "/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/unittest/mock.py", line 1332, in __exit__
        setattr(self.target, self.attribute, self.temp_original)
    TypeError: can't set attributes of built-in/extension type 'datetime.datetime'

C 側で実装された拡張型などはモンキーパッチを適用することができません。そのため、こういったエラーが発生します。

同様に *@patch.object* デコレーターを使うとオブジェクトのメソッドに対しても同様にモンキーパッチを適用できます。

```python
class Greeting:

    def __init__(self, name):
        self.name = name

    def do_greet(self):
        return greet(self.name)

class GreetingTestCase(unittest.TestCase):

    @patch.object(Greeting, 'do_greet')
    def test_obj_greet(self, mock_obj_greet):
        name = 'bob'
        expected = '%s, hello' % name

        mock_obj_greet.return_value = expected
        g = Greeting(name)
        actual = g.do_greet()
        self.assertEqual(actual, expected)

        # assert Greeting.greet method is called with these parameter
        mock_obj_greet.assert_called_with()
```

モックは簡単な用途に使う分には良いですが、複雑な用途に実装してしまうと、テスト対象の機能の仕様が変わってしまったときに保守するのが大変だったり、動作がよく分からなくなってしまい、保守できなくなってしまう場合があります。

複雑なモックは技術的負債になりやすいです。保守できないテストは意味をなさないのでやり過ぎないことも重要です。
