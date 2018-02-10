import pytest

from red_black_tree import BLACK, Node, RedBlackTree


def insert_tree(data):
    root = Node(data[0], BLACK)
    rbt = RedBlackTree(root)
    for i in data[1:]:
        rbt.insert(i)
    return rbt


def delete_tree(data, nums):
    rbt = insert_tree(data)
    for num in nums:
        rbt.delete(num)
    return rbt


three_data = [1, 2, 0]
insert_three = (
    three_data,
    """
black [1] p:na
├── red [0] p:1
└── red [2] p:1
"""
)

five_data = [2, 4, 3, 1, 0]
insert_five = (
    five_data,
    """
black [3] p:na
├── black [1] p:3
│   ├── red [0] p:1
│   └── red [2] p:1
└── black [4] p:3
"""
)

eight_data = [4, 6, 5, 3, 2, 7, 1, 0]
insert_eight = (
    eight_data,
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   ├── red [0] p:1
│   │   └── red [2] p:1
│   └── black [4] p:3
└── black [6] p:5
    └── red [7] p:6
"""
)

twelve_data = [9, 4, 10, 6, 5, 1, 0, 7, 11, 3, 2, 8]
insert_twelve = (
    twelve_data,
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)

seventeen_data = [2, 5, 6, 9, 4, 10, 1, 3, 8, 7, 13, 14, 11, 12, 17, 15, 16]
insert_seventeen = (
    seventeen_data,
    """
black [5] p:na
├── black [2] p:5
│   ├── black [1] p:2
│   └── black [4] p:2
│       └── red [3] p:4
└── black [13] p:5
    ├── red [9] p:13
    │   ├── black [7] p:9
    │   │   ├── red [6] p:7
    │   │   └── red [8] p:7
    │   └── black [11] p:9
    │       ├── red [10] p:11
    │       └── red [12] p:11
    └── red [15] p:13
        ├── black [14] p:15
        └── black [17] p:15
            └── red [16] p:17
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
    rbt = insert_tree(data)
    assert expected.replace('\n', '', 1) == rbt.root.show(False)


# three data
delete_three_leaf_left = (
    three_data,
    [0],
    """
black [1] p:na
└── red [2] p:1
"""
)
delete_three_leaf_right = (
    three_data,
    [2],
    """
black [1] p:na
└── red [0] p:1
"""
)
delete_three_root = (
    three_data,
    [1],
    """
black [0] p:na
└── red [2] p:0
"""
)

# five data
delete_five_leaf1 = (
    five_data,
    [0],
    """
black [3] p:na
├── black [1] p:3
│   └── red [2] p:1
└── black [4] p:3
"""
)
delete_five_leaf2 = (
    five_data,
    [3],
    """
black [2] p:na
├── black [1] p:2
│   └── red [0] p:1
└── black [4] p:2
"""
)
delete_five_node1 = (
    five_data,
    [1],
    """
black [3] p:na
├── black [0] p:3
│   └── red [2] p:0
└── black [4] p:3
"""
)
delete_five_node2 = (
    five_data,
    [4],
    """
red [1] p:na
├── black [0] p:1
└── black [3] p:1
    └── red [2] p:3
"""
)
delete_five_root = (
    five_data,
    [2],
    """
black [3] p:na
├── black [1] p:3
│   └── red [0] p:1
└── black [4] p:3
"""
)

# eight data
delete_eight_leaf1 = (
    eight_data,
    [0],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   └── red [2] p:1
│   └── black [4] p:3
└── black [6] p:5
    └── red [7] p:6
"""
)
delete_eight_leaf2 = (
    eight_data,
    [5],
    """
black [4] p:na
├── red [1] p:4
│   ├── black [0] p:1
│   └── black [3] p:1
│       └── red [2] p:3
└── black [6] p:4
    └── red [7] p:6
"""
)
delete_eight_leaf3 = (
    eight_data,
    [7],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   ├── red [0] p:1
│   │   └── red [2] p:1
│   └── black [4] p:3
└── black [6] p:5
"""
)
delete_eight_node1 = (
    eight_data,
    [3],
    """
black [5] p:na
├── red [2] p:5
│   ├── black [1] p:2
│   │   └── red [0] p:1
│   └── black [4] p:2
└── black [6] p:5
    └── red [7] p:6
"""
)
delete_eight_node2 = (
    eight_data,
    [2],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   └── red [0] p:1
│   └── black [4] p:3
└── black [6] p:5
    └── red [7] p:6
"""
)
delete_eight_node3 = (
    eight_data,
    [1],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [0] p:3
│   │   └── red [2] p:0
│   └── black [4] p:3
└── black [6] p:5
    └── red [7] p:6
"""
)
delete_eight_node4 = (
    eight_data,
    [6],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   ├── red [0] p:1
│   │   └── red [2] p:1
│   └── black [4] p:3
└── black [7] p:7
"""
)
delete_eight_root = (
    eight_data,
    [4],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       └── red [2] p:3
└── black [6] p:5
    └── red [7] p:6
"""
)

# twelve data
delete_twelve_red1 = (
    twelve_data,
    [1],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [0] p:3
│   │   └── red [2] p:0
│   └── black [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_red2 = (
    twelve_data,
    [2],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_red3 = (
    twelve_data,
    [4],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       └── red [2] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_red4 = (
    twelve_data,
    [6],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_red5 = (
    twelve_data,
    [8],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   └── red [6] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_red6 = (
    twelve_data,
    [9],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [8] p:5
    ├── black [7] p:8
    │   └── red [6] p:7
    └── black [10] p:8
        └── red [11] p:10
"""
)
delete_twelve_red7 = (
    twelve_data,
    [11],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
"""
)
delete_twelve_black1 = (
    twelve_data,
    [0],
    """
black [5] p:na
├── red [3] p:5
│   ├── black [1] p:3
│   │   └── red [2] p:1
│   └── black [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_black2 = (
    twelve_data,
    [3],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [2] p:1
│       └── red [4] p:2
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_black3 = (
    twelve_data,
    [7],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [6] p:9
    │   └── red [8] p:6
    └── black [10] p:9
        └── red [11] p:10
"""
)
delete_twelve_black4 = (
    twelve_data,
    [10],
    """
black [5] p:na
├── red [1] p:5
│   ├── black [0] p:1
│   └── black [3] p:1
│       ├── red [2] p:3
│       └── red [4] p:3
└── red [9] p:5
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [11] p:11
"""
)
delete_twelve_root = (
    twelve_data,
    [5],
    """
black [4] p:na
├── red [1] p:4
│   ├── black [0] p:1
│   └── black [3] p:1
│       └── red [2] p:3
└── red [9] p:4
    ├── black [7] p:9
    │   ├── red [6] p:7
    │   └── red [8] p:7
    └── black [10] p:9
        └── red [11] p:10
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

        delete_twelve_red1,
        delete_twelve_red2,
        delete_twelve_red3,
        delete_twelve_red4,
        delete_twelve_red5,
        delete_twelve_red6,
        delete_twelve_red7,
        delete_twelve_black1,
        delete_twelve_black2,
        delete_twelve_black3,
        delete_twelve_black4,
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

        ' twelve red1 ',
        ' twelve red2 ',
        ' twelve red3 ',
        ' twelve red4 ',
        ' twelve red5 ',
        ' twelve red6 ',
        ' twelve red7 ',
        ' twelve black1 ',
        ' twelve black2 ',
        ' twelve black3 ',
        ' twelve black4 ',
        ' twelve root ',
    ]
)
def test_delete(data, nums, expected):
    bst = delete_tree(data, nums)
    assert expected.replace('\n', '', 1) == bst.root.show(False)
