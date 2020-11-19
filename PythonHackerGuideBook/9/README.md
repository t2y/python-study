
## Simple sample code

```python
def add(x, y):
    z = x + y
    return z


print(add(3, 5))
```

```bash
(py39) $ python adder.py
8
```

## How to use ast helpers

```bash
(py39) $ python use_ast_from_source.py adder.py
```

## Use hy

> Hy is a Lisp dialect that's embedded in Python. Since Hy transforms its Lisp code into Python abstract syntax tree (AST) objects, you have the whole beautiful world of Python at your fingertips, in Lisp form.
> 
> https://github.com/hylang/hy


```
(py39) $ pip install hy
```

```lisp
(defn add [x, y]
    (+ x, y)) 

(print (add 3, 5))
```

```bash
(py39) $ hy hyadder.hy 
8
```

## Unparse ast from hy source

```bash
(py39) $ python unparse_hy_ast.py
def add(hyx_xXcommaX, y):
    return hyx_xXcommaX + y
print(add(3, 5))
```
