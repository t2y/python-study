# サードパーティー製のテストツールを使う

有名なテストフレームワークの1つとして pytest があります。pytest は標準ライブラリの unittest よりも強力なフレームワークであり、xUnit スタイルではない独自のテストに対する哲学をもっています。他にも有名なテストフレームはいくつかありますが、ここでは筆者の好みで pytest を取り上げます。

また複数の Python インタープリターのバージョンごとに仮想環境を作成し、その仮想環境へパッケージをインストールしてテストを行う tox というツールがあります。私が知る限り tox の代替となるプロダクトはなく、Python コミュニティにおける CI 向けのツールとしてデファクトスタンダードと言えます。

余談ですが、pytest と tox は同じ開発者 (Holger Krekel) によるプロダクトです。もちろん tox と他のテストフレームワークを組み合わせて使うこともできます。

* [pytest](http://docs.pytest.org/en/latest/)
* [tox](https://tox.readthedocs.io/en/latest/)

利点

* 標準ライブラリ (unittest) よりも機能が豊富で開発が活発なサードパーティ製のツールを使うことにより CI の構築や運用を効率化する

欠点

* 外部パッケージをインストールする必要がある
* 強力なツールを使いこなす上での学習コストがかかる
* pytest は独自スタイルのテスト手法であるため、作り込み過ぎるとベンダーロックインになる

ここで紹介するのは簡単な使い方のみです。
ライブラリの機能や詳細についてはそのドキュメントを参照してください。


## pytest

pytest は強力なテストフレームワークであるため、全ての機能をここでは紹介できませんが、比較的簡単に実行できて便利な機能のみを紹介します。

pytest をインストールします。

    $ source ~/.virtualenvs/pytesting/bin/activate
    (pytesting) $ pip install pytest

*py.test* というコマンドがインストールされます。これがテストランナーです。

    (pytesting) $ cd pytest_sample
    (pytesting) $ py.test --version
    This is pytest version 4.6.2, imported from path/to/pytesting/lib/python3.7/site-packages/pytest.py

*py.test* は unittest のように Python パッケージではないディレクトリのテストも探索できます。標準では *test\_* または *\_test.py* で終わるファイル名をテストファイルとみなします。

    (pytesting) $ py.test tests

さらにテストが失敗したときにその場所でデバッガー (pdb) を起動するといったこともコマンドラインオプションから指定できます。テストがエラーになるとデバッガーモードに入るので何度か **q** を入力して終了してください。

    (pytesting) $ py.test --pdb tests/test_assert.py
    ...
    (Pdb) q


### アサート機能

pytest の特徴の1つとして特別な *assert* 関数がありません。

例えば [unittest.TestCase](http://docs.python.jp/3/library/unittest.html#unittest.TestCase) のドキュメントをみると、数十の *assert* を行うためのユーティリティ関数が用意されています。これは便利な反面、これだけの数の *assert* 関数の振る舞いを理解しなければいけないことから学習コストが高くつくという欠点もあります。

pytest のテストは標準の *assert* 関数のみでアサートします (内部的にはテストの実行前に assert 文を置き換えていますが、テストを書く人が意識することはない) 。そのため、テストを書くときに検証するのは assert 文を使うか、例外をチェックするかの2通りしかありません。

実際にエラーになるテストをみてみましょう。以下のようなテスト関数があるとします。

```python
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

実行結果です。

```
    (pytesting) $ py.test tests/test_assert.py`
    ...
        def test_answer():
    >       assert func(3) == 5
    E       assert 4 == 5
    E        +  where 4 = func(3)
```

テストが失敗してそのレポートがこのような形で表示されます。このレポートの見やすさも pytest の特徴の1つにあげられます (他の言語では *Power Assert* と呼ばれることもあります) 。

次の例をみてみます。次のテスト関数は例外が発生することを期待しています (実際には発生しません) 。

```python
def test_raise():
    with pytest.raises(ZeroDivisionError):
        1 / 1
```

実行結果です。

```
        def test_raise():
            with pytest.raises(ZeroDivisionError):
    >           1 / 1
    E           Failed: DID NOT RAISE <class 'ZeroDivisionError'>

    pytest_sample/tests/test_assert.py:13: Failed
```

### pytest プラグイン

pytest は有名なフレームワークの1つであるため、サードパーティ製のプラグインも豊富です。デフォルトでインストールしておくと良いプラグインとして *pytest-pep8* と *pytest-flakes* があります。これらは Python コードの lint チェックとして機能します。

```
    (pytesting) $ pip install pytest-pep8 pytest-flakes
    (pytesting) $ py.test --help
      ...
      --pep8                perform some pep8 sanity checks on .py files
      --flakes              run pyflakes on .py files
      ...
```

例えば、Python のコーディングスタイルを定めた [PEP 8](https://www.python.org/dev/peps/pep-0008/) に準拠していない以下のようなコードのチェックができます。

```python
import sys


def f(x,y):
    z=x+y
    return z

def g():
    d = {'x':1, 'y':2}
    return d
```

実行結果です。

```
    (pytesting) $ py.test --pep8 --flakes bad_coding_style.py
    ...
    === FAILURES ===
    ___ pyflakes-check ___
    path/to/python3-testing-tutorial/02_use_3rd_party/pytest_sample/bad_coding_style.py:2: UnusedImport
    'sys' imported but unused
    ___ PEP8-check ___
    path/to/pytest_sample/bad_coding_style.py:5:8: E231 missing whitespace after ','
    def f(x,y):
           ^
    path/to/pytest_sample/bad_coding_style.py:6:6: E225 missing whitespace around operator
        z=x+y
         ^
    path/to/pytest_sample/bad_coding_style.py:8:1: W293 blank line contains whitespace

    ^
    path/to/pytest_sample/bad_coding_style.py:9:1: E302 expected 2 blank lines, found 1
    def g():
    ^
    path/to/pytest_sample/bad_coding_style.py:10:13: E231 missing whitespace after ':'
        d = {'x':1, 'y':2}
                ^
    path/to/pytest_sample/bad_coding_style.py:10:20: E231 missing whitespace after ':'
        d = {'x':1, 'y':2}
                       ^
```

[pytest 3rd party plugins](http://plugincompat.herokuapp.com/) で他にも多くのプラグインが提供されています。プロジェクトの用途にあったプラグインを選択すると良いでしょう。

### フィクスチャ

pytest には任意のテスト関数のパラメーターに任意のオブジェクトを渡す [fixture](http://docs.pytest.org/en/latest/fixture.html) 機能があります。以下のように *@pytest.fixture* でデコレートされた関数名がフィクスチャとして扱われます。

```python
@pytest.fixture
def my_args():
    return [1, 2, 3]


def test_fixture(my_args):
    assert len(my_args) == 3
    assert my_args[0] == 1
```

ここで *test_fixture()* に渡される *my_args* はフィクスチャで返されるオブジェクトになります。

また pytest が標準で用意されているフィクスチャもあります。例えば *tmpdir* というパラメーター名は一時ディレクトリを扱うオブジェクトが返されます。

```python
def test_use_tmpdir(tmpdir):
    print(tmpdir)
    assert True
```

このテストを以下のように実行します (*-s* をつけると print の出力がコンソールに表示されます) 。

    (pytesting) $ py.test -s tests/test_fixture.py
    ...
    tests/test_fixture.py ./private/var/folders/gv/bbddqtnj35x1qslfv3jhv2r5zdddnp/T/pytest-of-temorimo/pytest-9/test_use_tmpdir0

一時ディレクトリのパスが出力されます。

### データ駆動テスト

フィクスチャとよく似た機能として *@pytest.mark.parametrize* デコレーターを使ってデータ駆動テストもできます。

```python
@pytest.mark.parametrize(('x', 'y', 'expected'), [
    (1, 2, 3),
    (3, 4, 7),
    (5, 6, 11),
])
def test_parameter(x, y, expected):
    assert x + y == expected
```

実行結果です。

    (pytesting) $ py.test tests/test_parameterize.py -v
    ...
    tests/test_parameterize.py::test_parameter[1-2-3] PASSED
    tests/test_parameterize.py::test_parameter[3-4-7] PASSED
    tests/test_parameterize.py::test_parameter[5-6-11] PASSED

### どこまでテストを実装するべきか

ここで紹介した pytest の機能は一部です。詳細は公式ドキュメントを参照してください。

pytest はテストを実行する際に多くの箇所でフックできるため、フィクスチャ生成、依存性の注入、レポートの変更など、様々な要件に応じてカスタマイズできます。但し、モックの節でも述べた通り、複雑なテストは保守コストがかかり技術的負債になりやすい側面があります。

プロジェクトの要件や工数を考慮しながら適切なレベルのテストを実装するようにしましょう。


## tox

複数の Python 処理系に対して Python パッケージのインストールやテストを実行できます。

package-sample に Python 2/3 の両方で動くサンプルパッケージがあります。このサンプルパッケージを使って説明します。

* 前提条件として、複数の Python バージョンがシステムにインストールしているものとして作業を進める

仮想環境に tox をインストールします。

    $ source ~/.virtualenvs/pytesting/bin/activate
    (pytesting) $ pip install tox
    (pytesting) $ cd path/to/package-sample

### tox の設定ファイル

このサンプルパッケージでは以下の2つを設定しています。

* テストする Python インタープリターのバージョン
* テストのために必要なパッケージとテストランナーのコマンド

```
    (pytesting) $ cat tox.ini
    [tox]
    envlist = py35, py36, py37

    [testenv]
    deps =
        pytest
        pytest-pep8
        pytest-flakes

    commands = py.test -v --pep8 --flakes mypackage tests
```

*[testenv]* セクションの設定は全ての環境で利用されますが、特定の環境だけ設定を変更することもできます。例えば、py35 の環境だけ変更したい場合は *[testenv:py35]* を設定します。

    [tox]
    envlist = py35, py36, py37

    [testenv:py35]
    deps = ...
    commands = ...

    [testenv]
    deps = ...
    commands = ...

### tox の実行

Python 3.6 の環境でテストを実行してみます。

    (pytesting) $ tox -e py36
    GLOB sdist-make: path/to/package-sample/setup.py
    py36 inst-nodeps: path/to/package-sample/.tox/.tmp/package/1/mypackage-0.1.0.zip
    py36 installed: apipkg==1.5,atomicwrites==1.3.0,attrs==19.1.0,execnet==1.6.0,importlib-metadata==0.17,more-itertools==7.0.0,mypackage==0.1.0,packaging==19.0,pep8==1.7.1,pluggy==0.12.0,py==1.8.0,pyflakes==2.1.1,pyparsing==2.4.0,pytest==4.6.2,pytest-cache==1.0,pytest-flakes==4.0.0,pytest-pep8==1.0.6,six==1.12.0,wcwidth==0.1.7,zipp==0.5.1
    py36 run-test-pre: PYTHONHASHSEED='3325479124'
    py36 run-test: commands[0] | py.test -v --pep8 --flakes mypackage tests
    ================================================ test session starts ================================================
    platform darwin -- Python 3.6.8, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- path/to/package-sample/.tox/py36/bin/python
    cachedir: .tox/py36/.pytest_cache
    rootdir: path/to/package-sample
    plugins: flakes-4.0.0, pep8-1.0.6
    collected 16 items

    mypackage/__init__.py SKIPPED                                                                      [  6%]
    mypackage/__init__.py PASSED                                                                       [  6%]
    mypackage/main.py SKIPPED                                                                          [ 12%]
    mypackage/main.py PASSED                                                                           [ 12%]
    mypackage/utils.py SKIPPED                                                                         [ 18%]
    mypackage/utils.py PASSED                                                                          [ 18%]
    tests/test_enum.py SKIPPED                                                                         [ 25%]
    tests/test_enum.py PASSED                                                                          [ 25%]
    tests/test_enum.py::test_get_color_normal[red is specified as argument] PASSED                     [ 31%]
    tests/test_enum.py::test_get_color_normal[blue is specified as argument] PASSED                    [ 37%]
    tests/test_enum.py::test_get_color_normal[green is specified as argument] PASSED                   [ 43%]
    tests/test_enum.py::test_get_color_normal[1 is specified as argument] PASSED                       [ 50%]
    tests/test_enum.py::test_get_color_normal[2 is specified as argument] PASSED                       [ 56%]
    tests/test_enum.py::test_get_color_normal[3 is specified as argument] PASSED                       [ 62%]
    tests/test_enum.py::test_get_color_exception[yellow] PASSED                                        [ 68%]
    tests/test_enum.py::test_get_color_exception[5] PASSED                                             [ 75%]

    ================================================= warnings summary ==================================================
    .tox/py36/lib/python3.6/site-packages/_pytest/mark/structures.py:337
      path/to/package-sample/.tox/py36/lib/python3.6/site-packages/_pytest/mark/structures.py:337:
      PytestUnknownMarkWarning: Unknown pytest.mark.pep8 - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
        PytestUnknownMarkWarning,

    -- Docs: https://docs.pytest.org/en/latest/warnings.html
    ================================= 12 passed, 4 skipped, 1 warnings in 0.11 seconds ==================================
    ______________________________________________________ summary ______________________________________________________
      py36: commands succeeded
      congratulations :)

カレントディレクトリ配下に *.tox/py36* というディレクトリを設け、その配下に仮想環境を作成してパッケージのインストールやテストランナーの実行が行われます。

    (pytesting) $ tree -L 1 .tox/py36/
    .tox/py36/
    ├── bin
    ├── include
    ├── lib
    ├── log
    └── tmp

    5 directories, 1 file

先ほどは *-e py36* を指定して Python 3.6 の環境のみテストを実行しましたが、引数を指定せずに実行すると全ての環境のテストが実行されます。

    (pytesting) $ tox
    ...
      py35: commands succeeded
      py36: commands succeeded
      py37: commands succeeded
      congratulations :)

パッケージの開発中はどれか1つの環境を指定してテストを行い、そのテストが通るようになったら他の環境のテストも実行してみると良いでしょう。

### 複数環境の並行実行

tox コマンドはそれぞれの環境のテストを逐次的に実行します。1つの環境の実行に時間のかからないテストであれば、それでも構いませんが、この環境ごとのテストを並行実行する [detox](https://pypi.python.org/pypi/detox) というツールがあります。

    (pytesting) $ pip install detox
    (pytesting) $ detox
    ...
      py35: commands succeeded
      py36: commands succeeded
      py37: commands succeeded
      congratulations :)

