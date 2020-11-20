import ast

from hy.lex import hy_parse
from hy.compiler import hy_compile


hy_source = """
(defn add [x, y]
    (+ x, y))

(print (add 3, 5))
"""


def main():
    hy_tree = hy_parse(hy_source)
    py_ast = hy_compile(hy_tree, '__main__')
    code = compile(py_ast, '', 'exec')
    exec(code)
    print('=' * 32)
    print(ast.unparse(py_ast))


if __name__ == '__main__':
    main()
