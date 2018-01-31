"""
Implement rotating tree

* https://en.wikipedia.org/wiki/Tree_rotation
"""
import argparse
import logging
import random

from binary_search_tree import Node, BinarySearchTree

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
)
log = logging.getLogger(__file__)


def rotate_left(node, tree):
    """
        P (node)             Q (new_root)
      /  \                  / \
    A     Q        =>      P    C
         / \              / \
        B   C            A   B
    """
    new_root = node.right
    node.right = new_root.left
    if node.right is not None:
        node.right.attr = 'right'
    new_root.left = node
    if new_root.left is not None:
        new_root.left.attr = 'left'
    new_root.parent = node.parent
    node.parent = new_root

    if new_root.parent is None:
        tree.root = new_root
        tree.root.attr = 'root'
    else:
        if new_root.key < new_root.parent.key:
            new_root.parent.left = new_root
        elif new_root.parent.key < new_root.key:
            new_root.parent.right = new_root


def rotate_right(node, tree):
    """
         Q (node)          P (new_root)
        / \              /  \
       P   C       =>   A     Q
      / \                    / \
     A   B                  B   C
    """
    new_root = node.left
    node.left = new_root.right
    if node.left is not None:
        node.left.attr = 'left'
    new_root.right = node
    if new_root.right is not None:
        new_root.right.attr = 'right'
    new_root.parent = node.parent
    node.parent = new_root

    if new_root.parent is None:
        tree.root = new_root
        tree.root.attr = 'root'
    else:
        if new_root.key < new_root.parent.key:
            new_root.parent.left = new_root
        elif new_root.parent.key < new_root.key:
            new_root.parent.right = new_root


def set_parent(node, parent=None):
    node.parent = parent
    for child in node:
        set_parent(child, node)


def parse_argument():
    parser = argparse.ArgumentParser()
    parser.set_defaults(
        target_key=None,
        max_num=50,
        verbose=False,
    )

    parser.add_argument(
        '--max-num', dest='max_num', type=int,
        help='set maximum number of key range',
    )

    parser.add_argument(
        '--target-key', dest='target_key', type=int,
        help='set target key to rotate',
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

    if args.target_key is not None:
        set_parent(bst.root)
        key = args.target_key
        node = bst.search(key)
        print('search:', node)

        if node.attr == 'left' or node.attr == 'root':
            print('=== target %d, rotating left ===' % key)
            rotate_left(node, bst)
            bst.show()

            print('=== target %d, rotating right ===' % node.parent.key)
            rotate_right(node.parent, bst)
            bst.show()
        elif node.attr == 'right':
            print('=== target %d, rotating right ===' % key)
            rotate_right(node, bst)
            bst.show()

            print('=== target %d, rotating left ===' % node.parent.key)
            rotate_left(node.parent, bst)
            bst.show()


if __name__ == '__main__':
    main()
