# 型ヒントと型チェッカーを使う

Python 3.5 から静的型をアノテーションとして記述する構文が typing モジュールとともに標準化されました。但し、型アノテーションを記述できるようになったものの、Python インタープリターは、現時点では、実行時にその型アノテーションを全く使いません。

そのため *mypy* といったサードパーティー製の型チェッカーによって型チェックを行います。Python 自体は依然として動的型付けであるため、型チェッカーを高度な Lint ツールといったイメージで捉えても良いかもしれません。

* [[翻訳] PEP 0484 -- 型ヒント (Type Hints)](http://qiita.com/t2y/items/f95f6efe163b29be59af)
* [Python と型ヒント (Type Hints)](http://www.slideshare.net/t2y/python-type-hints-53759060)
* [mypy](http://mypy-lang.org/)
* [Pythonと型チェッカー](https://www.slideshare.net/t2y/python-typechecker-20180519)

Zulip という大規模な Web アプリケーションで型ヒントをつかって Python2/3 対応や型チェックを行ってみた事例が紹介されています。

* [[翻訳] Python の静的型、すごい mypy!](http://qiita.com/t2y/items/2a1310608da7b5c4860b)

利点

* スクリプトを実行しなくても型エラーを検出できる

欠点

* 型ヒントを付ける/保守するコスト
* すべてのソースに型ヒントがついていないと役に立たない場合もある

ここで紹介するのは簡単な使い方のみです。
詳細は [mypy document](http://mypy.readthedocs.io/en/latest/index.html) を参照してください。


## 型ヒント

[Mypy syntax cheat sheet (Python 3)](http://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) からよく使いそうな型ヒントを抜き出して簡単に紹介します。

### 組み込み型

変数は最初に代入するときに型推論も行われますが、明示的に型ヒントを書くにはコメントで記述します。

```python
# 組み込みの基本型
i = 1 # type: int
f = 1.0 # type: float
b = True # type: bool
s = "test" # type: str
by = b"test" # type: bytes

# リストと集合
l = [1] # type: List[int]
si = set([6, 7]) # type: Set[int]

# ディクショナリ
d = dict(field=2.0) # type: Dict[str, float]

# タプル
t = (3, "yes", 7.5) # type: Tuple[int, str, float]
```

ある値が *None* を取り得る場合はオプション型を指定します。例えば、文字列型と *None* を取り得る場合は *Optional[str]* と記述します。

```python
def func(n: int) -> Optional[str]:
    if n == 0:
        return None
    return 'not zero'

input_str = func(0)  # type: Optional[str]
```

また Python 3.6 から [PEP 526](https://www.python.org/dev/peps/pep-0526/) で変数アノテーション構文が追加され、以下のような構文で変数定義のときにアノテーションを記述できるようになります。

```python
foo: Optional[int]
bar: List[str] = []
```

### 関数

関数の引数と返り値の型アノテーションを記述します。

```python
def stringify(num: int) -> str:
    return str(num)
```

関数そのものは *Callable* を使って記述します。

```python
from typing import Callable

def f1(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

x = f1 # type: Callable[[int, float], float]
```

イテレーターは *Iterable* を使って記述します。

```python
from typing import Iterable

def f2(n: int) -> Iterable[int]:
    i = 0
    while i < n:
        yield i
        i += 1
```

### 複雑な型

複数の型が混在するようなリストは *Union* を使って記述します。

```python
from typing import Union, List

x1 = [3, 5, "test", "fun"]  # type: List[Union[int, str]]
```

型が分からない場合はすべての型の操作を許容する (型エラーが発生しない) *Any* という特別な型があります。

```python
from typing import Any

x2 = mystery_function()  # type: Any
```

### クラス

クラスも違和感なく記述できますが、いくつか条件が異なります。

* *\_\_init\_\_()* メソッドは return しませんが、便宜上は *None* を返すように型アノテーションを記述する
* *self* の型アノテーションは不要

```python
class MyClass:
   def __init__(self) -> None:
       ...

   def my_class_method(self, num: int, str1: str) -> str:
       return num * str1

x = MyClass() # type: MyClass
```

## 型チェッカー

mypy をインストールします。

    $ source ~/.virtualenvs/py3testing/bin/activate
    (py3testing) $ pip install mypy-lang

*mypy* というコマンドがインストールされます。これが型チェッカーです。

    (py3testing) $ cd 03_use_type_hint
    (py3testing) $ mypy --version
    mypy 0.4.6

mypy の型チェックを確認するために誤った型ヒントがついたコードを用意します。

```python
from typing import Dict, List

def f(x: float, y: float) -> Dict[str, int]:
    d = {
        'x': x,
        'y': y,
    }
    return d

def g() -> List[int]:
    numbers = []  # type: List[str]
    for i in range(10):
        numbers.append(i)
    numbers.append('test')
    return numbers
```

例えば、こういったコードを mypy で型チェックすると以下のようなエラーが検出されます。

    (py3testing) $ mypy error_sample1.py
    error_sample1.py: note: In function "f":
    error_sample1.py:10: error: Incompatible return value type (got Dict[str, float], expected Dict[str, int])
    error_sample1.py: note: In function "g":
    error_sample1.py:16: error: Argument 1 to "append" of "list" has incompatible type "int"; expected "str"
    error_sample1.py:18: error: Incompatible return value type (got List[str], expected List[int])

型ヒントと実際のコードから期待される型の操作が異なるためにこういったエラーが出力されます。

ここで実際にこのスクリプトを実行すると、以下の結果を得られます。

    (py3testing) $ python error_sample1.py
    {'x': 0.1, 'y': 0.2}
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'test']

型ヒントが誤っていてもそのコードが実行可能なものであれば、Python インタープリターはそのまま実行します。このように処理系は型ヒントを全くみないというのが **型ヒントはあくまでオプションである** といわれる所以です。

### 型チェッカーの実用性

[Mypy Development Roadmap](http://mypy-lang.org/roadmap.html) によると、1.0 というバージョンを実用的な区切りのリリースと考えているようにみえます。まだまだ活発な開発状況というのもあり、現時点 (2016-12) では、mypy の利用にあたっては試験運用といったレベルで考えた方が良いでしょう。

ただ型ヒント (型アノテーション) そのものは Python コミュニティで既に標準化されたものなのでコードに徐々に書いていくことをしても構いません。

