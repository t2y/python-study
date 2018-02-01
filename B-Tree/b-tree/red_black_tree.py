"""
Implement Red–black tree

* https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
  * http://fujimura2.fiw-web.net/java/mutter/tree/red-black-tree.html
"""
import argparse
import logging
import random

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)

BLACK = 'black'
RED = 'red'


def is_leaf(node):
    return isinstance(node, Leaf)


def find_root(node):
    if node.parent is None:
        return node
    else:
        return find_root(node.parent)


def replace_node(node, child):
    if child.key < node.parent.key:
        node.parent.left = child
    elif node.parent.key < child.key:
        node.parent.right = child

    node.key = child.key
    node.left = child.left
    node.right = child.right
    return node, child


def grandparent(node):
    parent = node.parent
    if parent is None:
        return None
    return parent.parent


def sibling(node):
    parent = node.parent
    if parent is None:
        return None
    elif node is parent.left:
        return parent.right
    else:
        return parent.left


def uncle(node):
    parent = node.parent
    if parent is None:
        return None
    return sibling(parent)


def rotate_left(node, tree):
    log.debug('rotate_left: %s' % node)
    new_node = node.right
    assert new_node is not LEAF
    node.right = new_node.left
    node.right.parent = node
    new_node.left = node
    new_node.parent = node.parent
    node.parent = new_node

    if new_node.parent is None:
        tree.root = new_node
    else:
        if new_node.key < new_node.parent.key:
            new_node.parent.left = new_node
        elif new_node.parent.key < new_node.key:
            new_node.parent.right = new_node
        else:
            assert False, 'rotate left: %s' % node


def rotate_right(node, tree):
    log.debug('rotate_right: %s' % node)
    new_node = node.left
    assert new_node is not LEAF
    node.left = new_node.right
    node.left.parent = node
    new_node.right = node
    new_node.parent = node.parent
    node.parent = new_node

    if new_node.parent is None:
        tree.root = new_node
    else:
        if new_node.key < new_node.parent.key:
            new_node.parent.left = new_node
        elif new_node.parent.key < new_node.key:
            new_node.parent.right = new_node
        else:
            assert False, 'rotate left: %s' % node


def find_max_node(node):
    max_node = node
    while max_node.right is not LEAF:
        max_node = max_node.right
    return max_node


class Leaf:

    def __init__(self):
        self.left = None
        self.right = None
        self.color = BLACK

    def __repr__(self):
        return '%s [Leaf]' % self.color


LEAF = Leaf()


class Node:

    def __init__(self, key, color='', parent=None):
        self.key = key
        self.color = color
        self.left = LEAF
        self.right = LEAF
        self.parent = parent

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        pkey = 'na' if self.parent is None else self.parent.key
        return '%s [%s] p:%s' % (self.color, self.key, pkey)

    @property
    def children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    @property
    def number_of_children(self):
        num = 0
        if self.left is not LEAF:
            num += 1
        if self.right is not LEAF:
            num += 1
        return num

    def search(self, key):
        if self.key == key:
            return self

        if not is_leaf(self):
            if key < self.key:
                if self.left is not LEAF:
                    return self.left.search(key)
            elif self.key < key:
                if self.right is not LEAF:
                    return self.right.search(key)

    def show(self, verbose):
        from anytree import Node as AnyNode, RenderTree
        verbose = False  # TODO

        def visit(node, parent, verbose):
            any_node = AnyNode(repr(node), parent=parent)
            for child in node:
                if is_leaf(child):
                    if verbose:
                        AnyNode(repr(child), parent=any_node)
                else:
                    visit(child, any_node, verbose)

        root = self
        root_any_node = AnyNode(repr(root))
        for child in root:
            if is_leaf(child):
                if verbose:
                    AnyNode(repr(child), parent=root_any_node)
            else:
                visit(child, root_any_node, verbose)

        s = ''
        for pre, fill, node in RenderTree(root_any_node):
            s += '%s%s\n' % (pre, node.name)

        return s


class RedBlackTree:

    def __init__(self, root):
        self.root = root

    def search(self, key):
        return self.root.search(key)

    def insert_recurse(self, root, node):
        if node.key < root.key:
            if is_leaf(root.left):
                root.left = node
                root.left.parent = root
            else:
                self.insert_recurse(root.left, node)
        elif root.key <= node.key:  # for duplicated key
            if is_leaf(root.right):
                root.right = node
                root.right.parent = root
            else:
                self.insert_recurse(root.right, node)
        else:
            assert False

    def insert_case1(self, node):
        log.debug('insert_case1')
        if node.parent is None:
            node.color = BLACK

    def insert_case2(self, node):
        log.debug('insert_case2')
        pass  # do nothing

    def insert_case3(self, node):
        log.debug('insert_case3')
        node.parent.color = BLACK
        uncle(node).color = BLACK
        g = grandparent(node)
        g.color = RED
        self.insert_repair_tree(g)

    def insert_case4_step2(self, node):
        log.debug('insert_case4 step2')
        p = node.parent
        g = grandparent(node)

        if node is p.left:
            rotate_right(g, self)
        else:
            rotate_left(g, self)

        p.color = BLACK
        g.color = RED

    def insert_case4(self, node):
        log.debug('insert_case4')
        p = node.parent
        g = grandparent(node)

        if node is g.left.right:
            rotate_left(p, self)
            node = node.left
        elif node is g.right.left:
            rotate_right(p, self)
            node = node.right

        self.insert_case4_step2(node)

    def insert_repair_tree(self, node):
        if node.parent is None:
            self.insert_case1(node)
        elif node.parent.color is BLACK:
            self.insert_case2(node)
        elif uncle(node).color is RED:
            self.insert_case3(node)
        else:
            self.insert_case4(node)

    def insert(self, key):
        node = Node(key, RED)
        log.debug('insert: %s' % repr(node))
        self.insert_recurse(self.root, node)
        self.insert_repair_tree(node)

    def delete_case6(self, node):
        log.debug('delete_case6')
        s = sibling(node)
        s.color = node.parent.color
        node.parent.color = BLACK

        if node is node.parent.left:
            s.right.color = BLACK
            rotate_left(node.parent, self)
        else:
            s.left.color = BLACK
            rotate_right(node.parent, self)

    def delete_case5(self, node):
        log.debug('delete_case5')
        s = sibling(node)

        if s.color is BLACK:
            if (
                node is node.parent.left and
                s is not LEAF and
                s.right.color is BLACK and
                s.left.color is RED
            ):
                s.color = RED
                s.left.color = BLACK
                rotate_right(s, self)
            elif (
                node is node.parent.right and
                s is not LEAF and
                s.left.color is BLACK and
                s.right.color is RED
            ):
                s.color = RED
                s.right.color = BLACK
                rotate_left(s)

            self.delete_case6(node)

    def delete_case4(self, node):
        log.debug('delete_case4')
        s = sibling(node)

        if (
            node.parent.color is RED and
            s is not LEAF and
            s.color is BLACK and
            s.left.color is BLACK and
            s.right.color is BLACK
        ):
            s.color = RED
            node.parent.color = BLACK
        else:
            self.delete_case5(node)

    def delete_case3(self, node):
        log.debug('delete_case3')
        s = sibling(node)

        if (
            node.parent.color is BLACK and
            s.color is BLACK and
            s.left.color is BLACK and
            s.right.color is BLACK
        ):
            s.color = RED
            self.delete_case1(node.parent)
        else:
            self.delete_case4(node)

    def delete_case2(self, node):
        log.debug('delete_case2')
        s = sibling(node)

        if s.color is RED:
            node.parent.color = RED
            s.color = BLACK
            if node is node.parent.left:
                rotate_left(node.parent, self)
            else:
                rotate_right(node.parent, self)
            self.delete_case3(node)

    def delete_case1(self, node):
        log.debug('delete_case1')
        if node.parent is not None:
            self.delete_case2(node)

    def delete_one_child(self, node):
        log.debug('delete_one_child')

        child = node.left if is_leaf(node.right) else node.right
        node, child = replace_node(node, child)

        if node.color is BLACK:
            if child.color is RED:
                child.color = BLACK
            else:
                self.delete_case1(child)

    def delete_no_child(self, node):
        log.debug('delete_no_child')

        p = node.parent
        if node.color is BLACK:
            if node is p.left:
                rotate_left(p, self)
            else:
                rotate_right(p, self)

            # FIXME: need condtion to set color
            p.parent.color = RED
            p.color = BLACK
            s = sibling(p)
            s.color = BLACK

            for c in p.children:
                if c is not LEAF:
                    c.color = RED

        if node.key < node.parent.key:
            node.parent.left = LEAF
        elif node.parent.key < node.key:
            node.parent.right = LEAF
        elif node.key == node.parent.key:
            node.parent.left = LEAF  # with left_max_node

    def _delete(self, key, start_node):
        # TODO: work in progress
        node = start_node.search(key)
        if node.number_of_children == 0:
            self.delete_no_child(node)
        elif node.number_of_children <= 1:
            self.delete_one_child(node)
        elif node.number_of_children == 2:
            left_max_node = find_max_node(node.left)
            node.key = left_max_node.key
            self._delete(left_max_node.key, node.left)

    def delete(self, key):
        self._delete(key, self.root)

    def show(self, verbose):
        print(self.root.show(verbose))


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
    root = Node(first, BLACK)

    rbt = RedBlackTree(root)
    for i in data:
        rbt.insert(i)

    print('=== initial tree structure ===')
    rbt.show(args.verbose)

    if len(args.delete_nums) > 0:
        for num in args.delete_nums:
            rbt.delete(num)
            print('=== deleted %d, after deleting ===' % num)
            rbt.show(args.verbose)


if __name__ == '__main__':
    main()
