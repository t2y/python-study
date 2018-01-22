import argparse
import bisect
import logging
import random


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


class Node:

    def __init__(self, keys):
        self.keys = keys
        self.children = []
        self.parent = None  # if node is root, then parent is None

    def __getitem__(self, index):
        return self.keys[index]

    def __len__(self):
        return len(self.keys)

    def __str__(self):
        # for debug print
        desc = 'Node%s parent: %s' % (self.keys, repr(self.parent))
        if self.is_leaf():
            desc = 'Leaf%s parent: %s' % (self.keys, repr(self.parent))
        else:
            children = ', '.join(str(i) for i in self.children)
            desc = '%s children: (%s)' % (desc, children)
        return desc

    def __repr__(self):
        # for tree print
        return 'Keys%s' % self.keys

    def merge(self, node):
        for key in node.keys:
            bisect.insort(self.keys, key)
        for child in node.children:
            child.parent = self
            index = bisect.bisect(self.keys, child.keys[0])
            self.children.insert(index, child)

    def delete_child(self, node):
        index = bisect.bisect(self.keys, node.keys[0])
        del self.children[index]

    def index(self, key):
        return self.keys.index(key)

    def is_leaf(self):
        return len(self.children) == 0

    def split(self):
        if len(self.keys) <= 2:
            return

        left_key = self.keys.pop(0)
        left = Node([left_key])
        left.children = self.children[0:2]
        left.parent = self

        right_key = self.keys.pop()
        right = Node([right_key])
        right.children = self.children[2:4]
        right.parent = self

        self.children = [left, right]

    def search(self, key, parent=None):
        self.parent = parent
        if key in self.keys:
            return True, self, self.keys.index(key)

        index = bisect.bisect(self.keys, key)
        if self.is_leaf():
            return False, self, index

        return self.children[index].search(key, parent=self)

    def insert(self, key):
        found, node, position = self.search(key)
        bisect.insort(node.keys, key)

    def show(self, indent=0):
        keys = '%s%s' % ('  ' * indent, repr(self))
        print(keys)
        for child in self.children:
            child.show(indent + 1)


class TwoThreeTree:

    def __init__(self, root):
        self.root = root

    def search(self, key):
        return self.root.search(key)

    def need_split(self, node):
        for child in node.children:
            if len(child.keys) == 3:
                return child, node
            else:
                grandchild, gc_parent = self.need_split(child)
                if grandchild is not None:
                    return grandchild, gc_parent
        return None, node

    def split_children(self, child, parent):
        parent.delete_child(child)
        child.split()
        parent.merge(child)

        if len(parent.keys) == 3:
            if parent.parent is not None:  # means not root node
                self.split_children(parent, parent.parent)

    def insert(self, key):
        self.root.insert(key)

        child, parent = self.need_split(self.root)
        if child is not None:
            self.split_children(child, parent)

        if len(self.root.keys) == 3:
            self.root.split()

    def update_parent(self, node, parent=None):
        # FIXME: set correct parent
        node.parent = parent
        for child in node.children:
            self.update_parent(child, node)

    def show(self):
        self.root.show()


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        max_num=50,
        verbose=False,
    )

    parser.add_argument(
        '--max-num', dest='max_num', type=int,
        help='set maximum number of key range',
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

    if args.max_num == 8:
        from test_two_three_tree import eight_data as data
    elif args.max_num == 17:
        from test_two_three_tree import seventeen_data as data
    elif args.max_num == 100:
        from test_two_three_tree import seventeen_data as data
    else:
        data = list(random.sample(range(args.max_num), args.max_num))

    log.info(data)
    first = data.pop(0)
    root = Node([first])
    tt_tree = TwoThreeTree(root)

    for i in data:
        tt_tree.insert(i)

    tt_tree.show()

    if args.verbose:
        tt_tree.update_parent(tt_tree.root)
        log.debug(str(tt_tree.root))


if __name__ == '__main__':
    main()
