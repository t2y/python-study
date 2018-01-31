"""
Implement Binary search tree

* https://en.wikipedia.org/wiki/Binary_search_tree

delete function is inspired by

* https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
"""
import argparse
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


class Node:

    def __init__(self, key, attr=''):
        self.key = key
        self.attr = attr
        self.left = None
        self.right = None

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return '%s [%s]' % (self.attr, self.key)

    @property
    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    @property
    def children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def search(self, key):
        if self.key == key:
            return self

        if not self.is_leaf:
            if key < self.key:
                return self.left.search(key)
            elif self.key < key:
                return self.right.search(key)

        return None

    def min(self):
        return self.key if self.left is None else self.left.min()

    def max(self):
        return self.key if self.right is None else self.right.max()

    def _insert(self, key, attr):
        node = getattr(self, attr)
        if node is None:
            node = Node(key, attr)
            setattr(self, attr, node)
        else:
            node.insert(key)

    def insert(self, key):
        if key < self.key:
            self._insert(key, 'left')
        elif self.key < key:
            self._insert(key, 'right')
        elif self.key == key:  # for duplicated key
            self._insert(key, 'right')
        else:
            assert False

    def find_max_node(self, node):
        max_node = node
        while max_node.right is not None:
            max_node = max_node.right
        return max_node

    def delete(self, key, parent=None):
        if self.key == key:
            self.key = None
            if parent is None:
                return True

            number_of_children = len(self.children)

            if self.is_leaf and parent is not None:
                if key < parent.key:
                    parent.left = None
                elif parent.key < key:
                    parent.right = None
                elif key == parent.key:
                    # delete sub tree node when deleting 2 children
                    parent.left = None

            elif number_of_children == 1:
                if self.left is not None:
                    if self.left.key < parent.key:
                        parent.left = self.left
                    elif parent.key < self.left.key:
                        parent.right = self.left
                        parent.right.attr = 'right'
                    self.left = None
                elif self.right is not None:
                    if self.right.key < parent.key:
                        parent.left = self.right
                        parent.left.attr = 'left'
                    elif parent.key < self.right.key:
                        parent.right = self.right
                    self.right = None

            elif number_of_children == 2:
                left_max_node = self.find_max_node(self.left)
                self.key = left_max_node.key

                # replace self with left sub-tree node
                # to delete the left max node in sub-tree
                temp = self
                self = self.left
                self.delete(left_max_node.key, temp)

            return True

        elif key < self.key and self.left is not None:
            return self.left.delete(key, self)
        elif self.key < key and self.right is not None:
            return self.right.delete(key, self)

        return False

    def show(self):
        from anytree import Node as AnyNode, RenderTree

        def visit(node, parent):
            any_node = AnyNode(repr(node), parent=parent)
            for child in node:
                visit(child, parent=any_node)

        root_any_node = AnyNode(repr(self))
        for child in self:
            visit(child, parent=root_any_node)

        s = ''
        for pre, fill, node in RenderTree(root_any_node):
            s += '%s%s\n' % (pre, node.name)
        return s


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def search(self, key):
        return self.root.search(key)

    def insert(self, key):
        self.root.insert(key)

    def delete(self, key):
        self.root.delete(key)

        if self.root.key is None:
            root = self.root.left
            root.attr = 'root'
            root.right = self.root.right
            self.root = root

    def show(self):
        print(self.root.show())


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        delete_nums=[],
        max_num=50,
        verbose=False,
    )

    parser.add_argument(
        '--max-num', dest='max_num', type=int,
        help='set maximum number of key range',
    )

    parser.add_argument(
        '--delete-num', dest='delete_nums', type=int, nargs='*',
        help='set delete key',
    )

    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='set verbose mode',
    )

    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    return args


def main():
    args = parse_argument()
    log.debug(args)

    if args.max_num == 3:
        from test_binary_search_tree import three_data as data
    elif args.max_num == 5:
        from test_binary_search_tree import five_data as data
    elif args.max_num == 8:
        from test_binary_search_tree import eight_data as data
    elif args.max_num == 12:
        from test_binary_search_tree import twelve_data as data
    elif args.max_num == 17:
        from test_binary_search_tree import seventeen_data as data
    elif args.max_num == 100:
        from test_binary_search_tree import hundred_data as data
    else:
        data = list(random.sample(range(args.max_num), args.max_num))

    log.info(data)
    first = data.pop(0)
    root = Node(first, 'root')

    bst = BinarySearchTree(root)
    for i in data:
        bst.insert(i)

    print('=== initial tree structure ===')
    bst.show()

    if len(args.delete_nums) > 0:
        for num in args.delete_nums:
            bst.delete(num)
            print('=== deleted %d, after deleting ===' % num)
            bst.show()


if __name__ == '__main__':
    main()
