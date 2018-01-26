from anytree import Node, RenderTree
from anytree.exporter import DotExporter

from visitor import NodeVisitor


class AnyTreeVisitor(NodeVisitor):

    def visit_root(self, node, parent=None):
        root = Node(repr(node))
        for child in node.children:
            self.visit(child, parent=root)
        return root

    def visit_node(self, node, parent=None):
        internal_node = Node(repr(node), parent=parent)
        for child in node.children:
            self.visit(child, parent=internal_node)
        return internal_node

    def visit_leaf(self, node, parent=None):
        leaf = Node(repr(node), parent=parent)
        return leaf


def print_node(node):
    node.update_parent()
    root = AnyTreeVisitor().visit(node)

    for pre, fill, node in RenderTree(root):
        print('%s%s' % (pre, node.name))

    # export graphviz files
    exporter = DotExporter(root)
    exporter.to_dotfile('graphviz.dot')
    exporter.to_picture('graphviz.png')
