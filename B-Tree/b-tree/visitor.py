from abc import ABC
from abc import abstractmethod


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
