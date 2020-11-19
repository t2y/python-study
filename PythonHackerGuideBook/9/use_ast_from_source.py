import ast
import sys


def parse_source(filename):
    with open('adder.py') as py:
        source = py.read()
        return ast.parse(source)


def run_code(filename):
    tree = parse_source(filename)
    print(tree)
    code = compile(tree, '<input>', 'exec')
    print(code)
    exec(code)


def walk_ast(filename):
    tree = parse_source(filename)
    for node in ast.walk(tree):
        print(node)


def dump_ast(filename):
    tree = parse_source(filename)
    print(ast.dump(tree, indent=2))


class MultiplicationNodeTransformer(ast.NodeTransformer):

    def visit_BinOp(self, node):
        print(f'orig: {vars(node)}')
        print(f'left: {vars(node.left)}')
        print(f'right: {vars(node.right)}')
        bin_op = ast.BinOp(
            left=node.left,
            op=ast.Mult(),
            right=node.right
        )
        ast.copy_location(bin_op, node)
        print(f'modified: {vars(bin_op)}')
        return bin_op
        #import ipdb; ipdb.set_trace()


def transform_ast(filename):
    tree = parse_source(filename)
    print('before transform')
    code = compile(tree, '', 'exec')
    exec(code)

    print('=' * 32)
    transformer = MultiplicationNodeTransformer()
    tree = transformer.visit(tree)
    print('=' * 32)

    code = compile(tree, '', 'exec')
    print('after transform')
    exec(code)


def main():
    filename = sys.argv[1]
    run_code(filename)
    dump_ast(filename)
    walk_ast(filename)
    transform_ast(filename)


if __name__ == '__main__':
    main()
