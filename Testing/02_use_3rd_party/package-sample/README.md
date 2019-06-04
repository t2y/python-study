# Python パッケージングのサンプルリポジトリ

## このリポジトリの目的

Python のパッケージングを実際のサンプルを触りながら学ぶ。

## リファレンス

このリポジトリで扱っているパッケージング詳細のドキュメントやツールの情報です。

* パッケージング: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/

    * PyPI: https://pypi.python.org/pypi
    * PyPA (Python Packaging Authorigy): https://github.com/pypa

* virtualenv: https://virtualenv.pypa.io/en/stable/
* setuptools: https://pypi.python.org/pypi/setuptools
* pytest: http://docs.pytest.org/en/latest/

    * https://pypi.python.org/pypi/pytest-pep8
    * https://pypi.python.org/pypi/pytest-flakes

* tox: https://tox.readthedocs.io/en/latest/

## パッケージをインストールする

このサンプルパッケージのリポジトリを clone する。

    $ git clone https://github.com/t2y/python-study.git
    $ cd python-study/Testing/02_use_3rd_party/package-sample
    $ cd package-sample
    $ ls
    LICENSE  MANIFEST.in  README.md  mypackage  mypackage.egg-info  setup.py  tests  tox.ini

サンプルパッケージをインストールするための仮想環境を作成する。ここでは Python 3.6 を使って仮想環境を作ります。

    $ python3.6 -m venv myenv
    $ source myenv/bin/activate
    (myenv) $

pip (Python のパッケージマネージャー) コマンドでインストールされているパッケージを確認する。仮想環境を作成したばかりなので何も表示されない。

    (myenv) $ pip freeze

サンプルパッケージをインストールする。setup.py の *develop* コマンドを使うと、パッケージをインストールするディレクトリからこのリポジトリへのリンクを貼ってくれる。*develop* でインストールすると、ローカルのリポジトリのソースコードを修正しながらパッケージ開発ができるので便利です。

    (myenv) $ python setup.py develop

pip でインストールされているパッケージを確認すると以下のように表示される。

    (myenv) $ pip freeze
    -e git+https://github.com/t2y/python-study.git@2a3d1c34f6f974885f44cb907954ebb38e97b5b7#egg=mypackage&subdirectory=Testing/02_use_3rd_party/package-sample

ローカルのファイルシステム上のパスを指すパッケージが検出される。pip freeze のすべての内容は以下になる。

    (myenv) $ pip freeze
    certifi==2019.3.9
    chardet==3.0.4
    idna==2.8
    -e git+https://github.com/t2y/python-study.git@2a3d1c34f6f974885f44cb907954ebb38e97b5b7#egg=mypackage&subdirectory=Testing/02_use_3rd_party/package-sample
    requests==2.22.0
    urllib3==1.25.3

インストールしたサンプルパッケージのコマンドを実行してみましょう。このサンプルパッケージでは *mycmd* と *yourcmd* というコマンドがインストールされます。

    (myenv) $ mycmd red
    I am mypackage.main
    Color.red
    (myenv) $ mycmd 2
    I am mypackage.main
    Color.green
    (myenv) $ yourcmd
    I am utils.cmd

## パッケージングの詳細

Python は標準ライブラリで Distutils というパッケージングのためのライブラリを提供していますが、そのライブラリでは機能不足であったため、歴史的な経緯で *setuptools* というサードパーティ製のパッケージライブラリが Python パッケージングのデファクトスタンダードとなり、現在はそのツールを PyPA (Python Packaging Authorigy) という Python コミュニティの公式な組織によって保守されています。

*setuptools* では setup.py というファイルにパッケージ設定の情報を記述します。setup.py から大事なところだけを抜き出して説明します。特に説明していないところは *setuptools* のドキュメントを参照してください。

    from setuptools import find_packages, setup

*setup()* 関数でパッケージの定義をします。*find_packages()* 関数を使うと、自動的に Python のソースファイルを検出して公開するパッケージを設定してくれます。

次に *setup()* 関数の主な項目をコメントで説明します。

    setup(
        name='mypackage',  # パッケージ名
        version=metadata['version'],  # パッケージのバージョン
        description='Sample pakcage to learn Python packaging',  # パッケージの説明
        url='https://github.com/t2y/python-study/tree/master/Testing',  # パッケージサイト
        license='Apache License 2.0',  # ライセンス
        author='Tetsuya Morimoto',  # 著者
        author_email='t2y@example.com',  # 著者のメールアドレス
        packages=find_packages(),  # 公開するパッケージ
        install_requires=[
            'requests',
        ],  # 依存するパッケージ
        tests_require=[  # テストでのみ使う依存パッケージ
            'tox', 'pytest', 'pytest-pep8', 'pytest-flakes',
        ],
        entry_points = {
            'console_scripts': [  # コマンドラインから使うときのコマンド名とそれに対応するコード
                'mycmd=mypackage.main:main',
                'yourcmd=mypackage.utils:cmd',
            ],
        },
    )


## パッケージのテストを実行する

*tox* を使うと、それぞれの Python インタープリターのバージョンごとに仮想環境を作成してパッケージ作成とインストールのテストが行えます (もちろんコードに対するテストも一緒に実行されます) 。試しにこのサンプルパッケージのテストを実行してみましょう。*tox* を使う利点の1つにローカルにインストール済みのライブラリなどをうっかり依存関係に追加し忘れるといったことを防げます。

例えば、Python 3.5 のインタープリターを使った仮想環境では以下のように実行します。但し、実行するにはあらかじめシステムに Python 3.5 がインストールされている必要があります。複数の Python バージョンをシステムにインストールする方法はそれぞれの OS ごとのやり方を調べてインストールしてください。

    (myenv) $ pip install tox
    (myenv) $ tox -e py35
    === test session starts ===
    platform darwin -- Python 3.5.7, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- path/to/Testing/02_use_3rd_party/package-sample/.tox/py35/bin/python
    cachedir: .tox/py35/.pytest_cache
    rootdir: path/to/Testing/02_use_3rd_party/package-sample
    plugins: flakes-4.0.0, pep8-1.0.6
    collected 16 items

    mypackage/__init__.py SKIPPED
    mypackage/__init__.py PASSED
    mypackage/main.py SKIPPED
    mypackage/main.py PASSED
    mypackage/utils.py SKIPPED
    mypackage/utils.py PASSED
    tests/test_enum.py SKIPPED
    tests/test_enum.py PASSED
    tests/test_enum.py::test_get_color_normal[red is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[blue is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[green is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[1 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[2 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[3 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_exception[yellow] PASSED
    tests/test_enum.py::test_get_color_exception[5] PASSED

    === 12 passed, 4 skipped in 0.04 seconds ===
    ____________________________________ summary ____________________________________
      py35: commands succeeded
      congratulations :)


## ローカル環境でソースコードや機能に対するテストを実行する

*tox* の設定ファイルである *tox.ini* をみてみましょう。*deps* にあるのはテストに必要なツールのパッケージ名です。*commands* にあるコマンドが実際にテストを実行するためのコマンドになります。

    (myenv) $ cat tox.ini
    [tox]
    envlist = py35, py36, py37

    [testenv]
    deps =
        pytest
        pytest-pep8
        pytest-flakes

    commands = py.test -v --pep8 --flakes mypackage tests

ここでは *pytest* というテストランナーを使っています。ローカルの仮想環境にも *pytest* と関連するプラグインをインストールしてローカルでテストを実行してみましょう。

mypackage ディレクトリのコーディングスタイルをテストします。

    (myenv) $ pip install pytest pytest-pep8 pytest-flakes
    (myenv) $ py.test -v --pep8 --flakes mypackage
    ========================================================================================== test session starts ==========================================================================================
    platform darwin -- Python 3.5.7, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- path/to/Testing/02_use_3rd_party/package-sample/.tox/py35/bin/python
    cachedir: .cache
    rootdir: path/to/Testing/02_use_3rd_party/package-sample
    plugins: pep8-1.0.6, flakes-1.0.1
    collected 6 items

    mypackage/__init__.py SKIPPED
    mypackage/__init__.py PASSED
    mypackage/main.py SKIPPED
    mypackage/main.py PASSED
    mypackage/utils.py SKIPPED
    mypackage/utils.py PASSED

    === 3 passed, 3 skipped in 0.01 seconds ===

tests ディレクトリにあるテストを実行します。

    (myenv) $ py.test -v --pep8 --flakes tests
    === test session starts ===
    platform darwin -- Python 3.5.7, pytest-4.6.2, py-1.8.0, pluggy-0.12.0 -- path/to/Testing/02_use_3rd_party/package-sample/.tox/py35/bin/python
    cachedir: .cache
    rootdir: path/to/Testing/02_use_3rd_party/package-sample
    plugins: pep8-1.0.6, flakes-1.0.1
    collected 10 items

    tests/test_enum.py SKIPPED
    tests/test_enum.py PASSED
    tests/test_enum.py::test_get_color_normal[red is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[blue is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[green is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[1 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[2 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_normal[3 is specified as argument] PASSED
    tests/test_enum.py::test_get_color_exception[yellow] PASSED
    tests/test_enum.py::test_get_color_exception[5] PASSED

    === 9 passed, 1 skipped in 0.02 seconds ===

