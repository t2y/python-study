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

    $ git clone $url
    $ cd python-package-sample
    $ ls
    MANIFEST.in        README.md        mypackage        mypackage.egg-info    setup.py        tests            tox.ini

サンプルパッケージをインストールするための仮想環境を作成する。ここでは Python 2.7 のインタープリターを使う仮想環境が作成されています。*virtualenv* はそれぞれの OS ごとのやり方を調べてインストールしてください

    $ virtualenv ~/.virtualenvs/mypackage
    New python executable in /Users/t2y/.virtualenvs/mypackage/bin/python2.7
    Also creating executable in /Users/t2y/.virtualenvs/mypackage/bin/python
    Installing setuptools, pip, wheel...done.
    $ source ~/.virtualenvs/mypackage/bin/activate
    (mypackage) $

pip (Python のパッケージマネージャー) コマンドでインストールされているパッケージを確認する。仮想環境を作成したばかりなので何も表示されない。

    (mypackage) $ pip freeze

サンプルパッケージをインストールする。setup.py の *develop* コマンドを使うと、パッケージをインストールするディレクトリからこのリポジトリへのリンクを貼ってくれる。*develop* でインストールすると、ローカルのリポジトリのソースコードを修正しながらパッケージ開発ができるので便利です。

    (mypackage) $ python setup.py develop

pip でインストールされているパッケージを確認すると以下のように表示される。setup.py の *instal_requires* をみてもらえば Python 3.4 より低い環境のときだけ *enum34* というパッケージをインストールするように設定があります。Python 3.4 で *enum* パッケージが標準ライブラリに追加されました。3.4 より古い Python インタープリターのバージョン向けに *enum34* というパッケージが PyPI で公開されています。

    (mypackage) $ pip freeze
    enum34==1.1.6

インストールしたサンプルパッケージのコマンドを実行してみましょう。このサンプルパッケージでは *mycmd* と *yourcmd* というコマンドがインストールされます。

    (mypackage) $ mycmd red
    I am mypackage.main
    Color.red
    (mypackage) $ mycmd 2
    I am mypackage.main
    Color.green
    (mypackage) $ yourcmd
    I am utils.cmd

## パッケージングの詳細

Python は標準ライブラリで Distutils というパッケージングのためのライブラリを提供していますが、そのライブラリでは機能不足であったため、歴史的な経緯で *setuptools* というサードパーティ製のパッケージライブラリが Python パッケージングのデファクトスタンダードとなり、現在はそのツールを PyPA (Python Packaging Authorigy) という Python コミュニティの公式な組織によって保守されています。

*setuptools* では setup.py というファイルにパッケージ設定の情報を記述します。setup.py から大事なところだけを抜き出して説明します。特に説明していないところは *setuptools* のドキュメントを参照してください。

    from setuptools import find_packages, setup

*setup()* 関数でパッケージの定義をします。*find_packages()* 関数を使うと、自動的に Python のソースファイルを検出して公開するパッケージを設定してくれます。

    REQUIRES = []

    if sys.version_info < (3, 4):
        REQUIRES.append('enum34')

Python のバージョンよって標準ライブラリの違いがあります。setup.py を実行する Python インタープリターのバージョンから依存関係を変更したいときはこういった方法で動的に依存関係のパッケージを設定します。

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
        install_requires=REQUIRES,  # 依存するパッケージ (動的に生成する必要がなければ、リストにパッケージ名を列挙する)
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

    (mypackage) $ pip install tox
    (mypackage) $ tox -e py35
    GLOB sdist-make: /Users/t2y/work/repo/python-package-sample/setup.py
    py35 inst-nodeps: /Users/t2y/work/repo/python-package-sample/.tox/dist/mypackage-0.1.0.zip
    py35 installed: apipkg==1.4,execnet==1.4.1,mypackage==0.1.0,pep8==1.7.0,py==1.4.31,pyflakes==1.3.0,pytest==3.0.5,pytest-cache==1.0,pytest-flakes==1.0.1,pytest-pep8==1.0.6,storage-deploy==0.1.0
    py35 runtests: PYTHONHASHSEED='4159216310'
    py35 runtests: commands[0] | py.test -v --pep8 --flakes mypackage tests
    === test session starts ===
    platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0 -- /Users/t2y/work/repo/python-package-sample/.tox/py35/bin/python3.5
    cachedir: .cache
    rootdir: /Users/t2y/work/repo/python-package-sample, inifile:
    plugins: pep8-1.0.6, flakes-1.0.1
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
    ________________________________________________________________________________________________ summary ________________________________________________________________________________________________
      py35: commands succeeded
      congratulations :)


## ローカル環境でソースコードや機能に対するテストを実行する

*tox* の設定ファイルである *tox.ini* をみてみましょう。*deps* にあるのはテストに必要なツールのパッケージ名です。*commands* にあるコマンドが実際にテストを実行するためのコマンドになります。

    (mypackage) $ cat tox.ini
    [tox]
    envlist = py27, py33, py34, py35

    [testenv]
    deps =
        pytest
        pytest-pep8
        pytest-flakes

    commands = py.test -v --pep8 --flakes mypackage tests

ここでは *pytest* というテストランナーを使っています。ローカルの仮想環境にも *pytest* と関連するプラグインをインストールしてローカルでテストを実行してみましょう。

mypackage ディレクトリのコーディングスタイルをテストします。

    (mypackage) $ pip install pytest pytest-pep8 pytest-flakes
    (mypackage) $ py.test -v --pep8 --flakes mypackage
    ========================================================================================== test session starts ==========================================================================================
    platform darwin -- Python 2.7.12, pytest-3.0.5, py-1.4.31, pluggy-0.4.0 -- /Users/t2y/.virtualenvs/mypackage/bin/python2.7
    cachedir: .cache
    rootdir: /Users/t2y/work/repo/python-package-sample, inifile:
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

    (mypackage) $ py.test -v --pep8 --flakes tests
    === test session starts ===
    platform darwin -- Python 2.7.12, pytest-3.0.5, py-1.4.31, pluggy-0.4.0 -- /Users/t2y/.virtualenvs/mypackage/bin/python2.7
    cachedir: .cache
    rootdir: /Users/t2y/work/repo/python-package-sample, inifile:
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

