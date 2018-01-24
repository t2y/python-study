import argparse
import bisect
import logging
import random
from itertools import chain


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


def flatten(list_of_list):
    return list(chain.from_iterable(list_of_list))


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
        if self.is_leaf:
            desc = 'Leaf%s parent: %s' % (self.keys, repr(self.parent))
        else:
            children = ', '.join(str(i) for i in self.children)
            desc = '%s children: (%s)' % (desc, children)
        return desc

    def __repr__(self):
        # for tree print
        return 'Keys%s' % self.keys

    @property
    def is_leaf(self):
        return len(self.children) == 0

    @property
    def is_root(self):
        return self.parent is None

    @property
    def leftmost(self):
        return self.keys[0] if len(self.keys) > 0 else None

    @property
    def rightmost(self):
        return self.keys[-1] if len(self.keys) > 0 else None

    def index(self, key):
        return self.keys.index(key)

    def get_number_of_keys(self, include_children=True):
        num = len(self.keys)
        if include_children:
            num += sum(len(i) for i in self.children)
        return num

    def insert_merge(self, node):
        for key in node.keys:
            bisect.insort(self.keys, key)
        for child in node.children:
            child.parent = self
            index = bisect.bisect(self.keys, child.keys[0])
            self.children.insert(index, child)

    def delete_child(self, node):
        self.children.remove(node)

    def need_redistribute(self):
        if self.is_leaf:
            return False

        if self.get_number_of_keys() < 3:
            return False

        if (
            len(self.keys) == 0 or
            any(True for i in self.children if len(i.keys) == 0)
           ):
            """
            Keys[] (self)
                or
            Keys[5] (self)
              Keys[4]
              Keys[]
            """
            return True

        if (
            len(self.keys) == 1 and
            len(self.children) == 1 and len(self.children[0].keys) == 2
           ):
            """
            Keys[5] (self)
              Keys[6, 7]
            """
            return True

        if self.leftmost > self.children[0].leftmost:
            """
            Keys[1] (self)
              Keys[2]
              Keys[3]
            """
            return True

        if self.rightmost < self.children[-1].rightmost:
            """
            Keys[3] (self)
              Keys[2]
              Keys[1]
            """
            return True

        return False

    def redistribute(self):
        """
            Keys[5] (self) => Keys[6]
              Keys[6, 7]        Keys[5]
                                Keys[7]

            Keys[1] (self) => Keys[2]
              Keys[2]           Keys[1]
              Keys[3]           Keys[3]

            Keys[5] (self) => Keys[5]
              Keys[4]           Keys[4]
              Keys[6, 7]        Keys[7]

            Keys[2] (self) => Keys[2]
              Keys[0, 1]        Keys[1]
              Keys[3]           Keys[3]
        """
        if self.is_leaf:
            return

        children_keys = flatten([i.keys for i in self.children])
        keys = self.keys + children_keys
        keys.sort()

        node = Node([keys[1]])

        left = Node([keys[0]])
        left.parent = node
        left.children = self.children[0].children

        node.children = [left]

        right_keys = keys[2:]
        if len(right_keys) > 0:
            right = Node(right_keys)
            right.parent = node
            if len(self.children) > 1:  # TODO: consider later
                right.children = self.children[1].children
            node.children.append(right)

        if self.parent is not None:
            prev_node = self
            self.parent.delete_child(prev_node)

            node.parent = prev_node.parent
            index = bisect.bisect(self.parent.keys, self.keys[0])
            self.parent.children.insert(index, node)

        self = node

    def join(self):
        """
            delete: 2
            Keys[1, 3] (self) => Keys[3]
              Keys[0]              Keys[0, 1]
              Keys[2]              Keys[4]
              Keys[4]

            delete: 0
            Keys[3]          => Keys[3]         => Keys[3, 5]
              Keys[1] (self)      Keys[] (self)      Keys[1, 2]
                Keys[0]             Keys[1,2]        Keys[4]
                Keys[2]           Keys[5]            Keys[6, 7]
              Keys[5]               Keys[4]
                Keys[4]             Keys[6, 7]
                Keys[6, 7]
        """
        if self.is_leaf:
            return

        target_child = left_child = self.children[0]
        if len(self.children) > 1:
            if len(left_child.keys) == 0:
                target_child = self.children[1]

        bisect.insort(target_child.keys, self.keys.pop(0))
        if len(self.keys) == 0:
            if not self.is_root:
                for child in reversed(self.children):  # FIXME: right child
                    self.parent.children[1].children.insert(0, child)
                self.parent.children.remove(self)

            parent = self.parent
            while parent is not None:
                parent.join()
                parent = parent.parent

    def join_on_node(self, position):
        child = self.children[position]
        self.keys.insert(position, child.keys.pop(0))
        self.delete_child(child)
        if self.need_redistribute():
            self.redistribute()
        else:
            self.join()

    def split(self):
        """
            Keys[1, 2, 4] => Keys[2]
             (self)            Keys[1]
                               Keys[4]
        """
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
        if self.is_leaf:
            return False, self, index

        return self.children[index].search(key, parent=self)

    def insert(self, key):
        found, node, position = self.search(key)
        bisect.insort(node.keys, key)

    def delete(self, key):
        self.keys.remove(key)
        if not self.is_root:
            if self.is_leaf and len(self.keys) == 0:
                self.parent.delete_child(self)

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
        parent.insert_merge(child)

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

    def delete(self, key):
        found, node, position = self.search(key)
        if not found:
            return

        if node.is_leaf:
            number_of_children = len(node.parent.children)
            node.delete(key)
            if number_of_children == 3:
                node.parent.join()
            elif number_of_children == 2:
                if node.parent.need_redistribute():
                    node.parent.redistribute()
                else:
                    node.parent.join()
            else:
                if not node.is_root:
                    msg = 'the number of children is 2 or 3, but %d !'
                    assert False, msg % number_of_children
        else:  # internal node
            node.delete(key)
            node.join_on_node(position)

        if len(self.root.keys) == 0:
            self.root = self.root.children[0]  # TODO: consider later

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
        help='set delete number of 2-3 tree',
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

    if args.max_num == 5:
        from test_two_three_tree import five_data as data
    elif args.max_num == 8:
        from test_two_three_tree import eight_data as data
    elif args.max_num == 17:
        from test_two_three_tree import seventeen_data as data
    elif args.max_num == 100:
        from test_two_three_tree import hundred_data as data
    else:
        data = list(random.sample(range(args.max_num), args.max_num))

    log.info(data)
    first = data.pop(0)
    root = Node([first])
    tt_tree = TwoThreeTree(root)

    for i in data:
        tt_tree.insert(i)

    print('=== initial tree structure ===')
    tt_tree.show()

    if args.verbose:
        tt_tree.update_parent(tt_tree.root)
        log.debug(str(tt_tree.root))

    if len(args.delete_nums) > 0:
        for num in args.delete_nums:
            tt_tree.delete(num)
            print('=== after deleting ===')
            tt_tree.show()


if __name__ == '__main__':
    main()
