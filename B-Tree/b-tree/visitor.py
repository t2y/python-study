from abc import ABC
from abc import abstractmethod

from treelib import Node, Tree


class NodeVisitor(ABC):

    @abstractmethod
    def visit_root(self, node, **kwargs):
        pass

    @abstractmethod
    def visit_node(self, node, **kwargs):
        pass

    @abstractmethod
    def visit_leaf(self, node, **kwargs):
        pass

    def visit(self, node, **kwargs):
        if node.is_leaf:
            return self.visit_leaf(node, **kwargs)
        elif node.is_root:
            return self.visit_root(node, **kwargs)
        else:  # root or internal node
            return self.visit_node(node, **kwargs)
        return ''


class TreeLibPrinter(NodeVisitor):

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


def visit(visitor, node, indent=''):
    if node.is_leaf:
        return visitor.visit_leaf(node, indent)
    elif node.is_root:
        return visitor.visit_root(node, indent)
    else:  # root or internal node
        return visitor.visit_node(node, indent)
    return ""


def print_node(node):
    node.update_parent()
    printer = TreeLibPrinter()
    print(visit(printer, node))
