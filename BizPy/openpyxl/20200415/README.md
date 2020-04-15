
## コードレビュー/リファクタリング

* tkinter を使ってダイアログでファイルの選択と保存を行っている
  * 処理を自動化するなら GUI から CLI へ
* コマンドライン引数を受け取る
* あるディレクトリ配下のファイルをフィルターする
* `main()` 関数を設ける
* グローバル変数を使わないようにする
* ジェネレーター (`yield`) を使って繰り返し処理を効率化する

## リファレンス

### Python 公式ドキュメント

* [pathlib --- オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)
* [sys --- システムパラメータと関数](https://docs.python.org/ja/3/library/sys.html)

### ジェネレーター

* [Pythonオンライン学習サービス PyQ（パイキュー）ドキュメント: ジェネレーター](https://docs.pyq.jp/python/library/generator.html)

### サンプルコード 

* [できる 仕事がはかどるPython自動処理 全部入り。](https://book.impress.co.jp/books/1118101147)

