# Python の仮想環境の構築

Python の仮想環境の構築には [virtualenv](https://pypi.org/project/virtualenv/) を使う。virtualenv は Python 3.3 以降では同等の機能が [venv](https://docs.python.org/ja/3/library/venv.html) として提供されている。新しい Python を使っているなら virtualenv をインストールせずにすぐに使える。

## 仮想環境の作成

`venv` モジュールを使って仮想環境を作成する。

```bash
$ python3.6 -m venv myenv
$ tree -L 1 myenv
myenv
├── bin
├── include
├── lib
└── pyvenv.cfg

3 directories, 1 file
```

## 仮想環境の有効化

仮想環境を有効にするときは `source` コマンドで作成した仮想環境内にある `activate` ファイルを読み込む。

```bash
$ source myenv/bin/activate
(myenv) $
(myenv) $ pip freeze  # 何も出力されない
```

自分でなにかパッケージをインストールしてみましょう。

```bash
(myenv) $ pip install snorse
(myenv) $ pip freeze
click==3.3
snorse==1.0.0
(myenv) $ snorse snowman
☃ ☃ ☃   ⛄⛄⛄ ☃   ⛄⛄⛄ ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄ ⛄⛄⛄   ⛄⛄⛄ ⛄⛄⛄   ☃ ⛄⛄⛄   ⛄⛄⛄ ☃
```

## 仮想環境の無効化

仮想環境を無効にするときは `deactivate` というシェル関数を実行する。

```bash
(myenv) $ deactivate
$
```

## 仮想環境の削除

作成した仮想環境のディレクトリを削除する。

```bash
$ rm -rf myenv
```
