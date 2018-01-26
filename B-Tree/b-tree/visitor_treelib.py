from treelib import Tree

from visitor import NodeVisitor


class TreeLibVisitor(NodeVisitor):

    def visit_root(self, node, tree=None):
        tree = Tree()
        root = repr(node)
        tree.create_node(root, root)
        for child in node.children:
            tree = self.visit(child, tree=tree)
        return tree

    def visit_node(self, node, tree=None):
        _node = repr(node)
        tree.create_node(_node, _node, parent=repr(node.parent))
        for child in node.children:
            tree = self.visit(child, tree=tree)
        return tree

    def visit_leaf(self, node, tree=None):
        leaf = repr(node)
        tree.create_node(leaf, leaf, parent=repr(node.parent))
        return tree


def print_node(node):
    node.update_parent()
    print(TreeLibVisitor().visit(node))
