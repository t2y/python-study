# Python でテストを書くためのチュートリアル

## このリポジトリの目的

Python でテスト駆動開発 (TDD) をするための機能やツールなどを学ぶ。

* 本リポジトリにあるコードは Python 3.6 以上で動作確認している


## 概要

大きく分けて3つに分類されます。

これらの3つのうち、どれか1つを選択するといったものではなく、説明しやすいように分類しているだけです。例えば、標準ライブラリの doctest とサードパーティー製のツールを組み合わせて使うこともできます。そのプロジェクトの要件や状況に応じて適切な機能やテストツールの選択をすると良いです。

1. Python の標準ライブラリのみを使う

    * doctest
    * unittest (unittest.mock)

2. サードパーティー製のテストツールを使う

    * pytest
    * tox

3. 型ヒントと型チェッカーを使う

    * typing
    * mypy

## リポジトリを取得する

このリポジトリを clone する。

    $ git clone git@github.com:t2y/python-study.git
    $ cd python-study/Testing
    $ ls
    00_virtualenv			01_use_standard_library_only	02_use_3rd_party		03_use_type_hint		README.md

それぞれのテストのやり方については対応するディレクトリ配下にある README.md を参照してください。
