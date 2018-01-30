import pytest

from binary_search_tree import Node, BinarySearchTree


def insert_tree(data):
    root = Node(data[0], 'root')
    bst = BinarySearchTree(root)
    for i in data[1:]:
        bst.insert(i)
    return bst


def delete_tree(data, nums):
    bst = insert_tree(data)
    for num in nums:
        bst.delete(num)
    return bst


three_data = [1, 2, 0]
insert_three = (
    three_data,
    """
root [1]
├── left [0]
└── right [2]
"""
)

five_data = [2, 4, 3, 1, 0]
insert_five = (
    five_data,
    """
root [2]
├── left [1]
│   └── left [0]
└── right [4]
    └── left [3]
"""
)

eight_data = [4, 6, 5, 3, 2, 7, 1, 0]
insert_eight = (
    eight_data,
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [1]
│           └── left [0]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)

twelve_data = [9, 4, 10, 6, 5, 1, 0, 7, 11, 3, 2, 8]
insert_twelve = (
    twelve_data,
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)

seventeen_data = [2, 5, 6, 9, 4, 10, 1, 3, 8, 7, 13, 14, 11, 12, 17, 15, 16]
insert_seventeen = (
    seventeen_data,
    """
root [2]
├── left [1]
└── right [5]
    ├── left [4]
    │   └── left [3]
    └── right [6]
        └── right [9]
            ├── left [8]
            │   └── left [7]
            └── right [10]
                └── right [13]
                    ├── left [11]
                    │   └── right [12]
                    └── right [14]
                        └── right [17]
                            └── left [15]
                                └── right [16]
"""
)


@pytest.mark.parametrize(
    ('data', 'expected'), [
        insert_three,
        insert_five,
        insert_eight,
        insert_twelve,
        insert_seventeen,
    ],
    ids=[
        ' three ',
        ' five ',
        ' eight ',
        ' twelve ',
        ' seventeen ',
    ]
)
def test_insert(data, expected):
    bst = insert_tree(data)
    assert expected.replace('\n', '', 1) == bst.root.show()


# three data
delete_three_leaf_left = (
    three_data,
    [0],
    """
root [1]
└── right [2]
"""
)
delete_three_leaf_right = (
    three_data,
    [2],
    """
root [1]
└── left [0]
"""
)
delete_three_root = (
    three_data,
    [1],
    """
root [0]
└── right [2]
"""
)

# five data
delete_five_leaf1 = (
    five_data,
    [0],
    """
root [2]
├── left [1]
└── right [4]
    └── left [3]
"""
)
delete_five_leaf2 = (
    five_data,
    [3],
    """
root [2]
├── left [1]
│   └── left [0]
└── right [4]
"""
)
delete_five_node1 = (
    five_data,
    [1],
    """
root [2]
├── left [0]
└── right [4]
    └── left [3]
"""
)
delete_five_node2 = (
    five_data,
    [4],
    """
root [2]
├── left [1]
│   └── left [0]
└── right [3]
"""
)
delete_five_root = (
    five_data,
    [2],
    """
root [1]
├── left [0]
└── right [4]
    └── left [3]
"""
)

# eight data
delete_eight_leaf1 = (
    eight_data,
    [0],
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [1]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)
delete_eight_leaf2 = (
    eight_data,
    [5],
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [1]
│           └── left [0]
└── right [6]
    └── right [7]
"""
)
delete_eight_leaf3 = (
    eight_data,
    [7],
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [1]
│           └── left [0]
└── right [6]
    └── left [5]
"""
)
delete_eight_node1 = (
    eight_data,
    [3],
    """
root [4]
├── left [2]
│   └── left [1]
│       └── left [0]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)
delete_eight_node2 = (
    eight_data,
    [2],
    """
root [4]
├── left [3]
│   └── left [1]
│       └── left [0]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)
delete_eight_node3 = (
    eight_data,
    [1],
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [0]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)
delete_eight_node4 = (
    eight_data,
    [6],
    """
root [4]
├── left [3]
│   └── left [2]
│       └── left [1]
│           └── left [0]
└── right [5]
    └── right [7]
"""
)
delete_eight_root = (
    eight_data,
    [4],
    """
root [3]
├── left [2]
│   └── left [1]
│       └── left [0]
└── right [6]
    ├── left [5]
    └── right [7]
"""
)

# twelve data
delete_twelve_leaf1 = (
    twelve_data,
    [0],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_leaf2 = (
    twelve_data,
    [2],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_leaf3 = (
    twelve_data,
    [5],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_leaf4 = (
    twelve_data,
    [8],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
└── right [10]
    └── right [11]
"""
)
delete_twelve_leaf5 = (
    twelve_data,
    [11],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
"""
)
delete_twelve_node1 = (
    twelve_data,
    [4],
    """
root [9]
├── left [3]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_node2 = (
    twelve_data,
    [1],
    """
root [9]
├── left [4]
│   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_node3 = (
    twelve_data,
    [3],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_node4 = (
    twelve_data,
    [6],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [5]
│       └── right [7]
│           └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_node5 = (
    twelve_data,
    [7],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [8]
└── right [10]
    └── right [11]
"""
)
delete_twelve_node6 = (
    twelve_data,
    [10],
    """
root [9]
├── left [4]
│   ├── left [1]
│   │   ├── left [0]
│   │   └── right [3]
│   │       └── left [2]
│   └── right [6]
│       ├── left [5]
│       └── right [7]
│           └── right [8]
└── right [11]
"""
)
delete_twelve_root = (
    twelve_data,
    [9],
    """
root [4]
├── left [1]
│   ├── left [0]
│   └── right [3]
│       └── left [2]
└── right [10]
    └── right [11]
"""
)


@pytest.mark.parametrize(
    ('data', 'nums', 'expected'), [
        delete_three_leaf_left,
        delete_three_leaf_right,
        delete_three_root,

        delete_five_leaf1,
        delete_five_leaf2,
        delete_five_node1,
        delete_five_node2,
        delete_five_root,

        delete_eight_leaf1,
        delete_eight_leaf2,
        delete_eight_leaf3,
        delete_eight_node1,
        delete_eight_node2,
        delete_eight_node3,
        delete_eight_node4,
        delete_eight_root,

        delete_twelve_leaf1,
        delete_twelve_leaf2,
        delete_twelve_leaf3,
        delete_twelve_leaf4,
        delete_twelve_leaf5,
        delete_twelve_node1,
        delete_twelve_node2,
        delete_twelve_node3,
        delete_twelve_node4,
        delete_twelve_node5,
        delete_twelve_node6,
        delete_twelve_root,
    ],
    ids=[
        ' three leaf left ',
        ' three leaf right ',
        ' three root ',

        ' five leaf1 ',
        ' five leaf2 ',
        ' five node1 ',
        ' five node2 ',
        ' five root ',

        ' eight leaf1 ',
        ' eight leaf2 ',
        ' eight leaf3 ',
        ' eight node1 ',
        ' eight node2 ',
        ' eight node3 ',
        ' eight node4 ',
        ' eight root ',

        ' twelve leaf1 ',
        ' twelve leaf2 ',
        ' twelve leaf3 ',
        ' twelve leaf4 ',
        ' twelve leaf5 ',
        ' twelve node1 ',
        ' twelve node2 ',
        ' twelve node3 ',
        ' twelve node4 ',
        ' twelve node5 ',
        ' twelve node6 ',
        ' twelve root ',
    ]
)
def test_delete(data, nums, expected):
    bst = delete_tree(data, nums)
    assert expected.replace('\n', '', 1) == bst.root.show()
