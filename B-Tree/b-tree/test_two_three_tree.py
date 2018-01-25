import pytest

from two_three_tree import Node, TwoThreeTree


def insert_tree(data):
    root = Node([data[0]])
    tt_tree = TwoThreeTree(root)
    for i in data[1:]:
        tt_tree.insert(i)
    tt_tree.update_parent(tt_tree.root)
    return tt_tree


def delete_tree(data, nums):
    tt_tree = insert_tree(data)
    for num in nums:
        tt_tree.delete(num)
    tt_tree.update_parent(tt_tree.root)
    return tt_tree


three_data = [2, 1, 0]
insert_three = (
    three_data,
    'Node[1] parent: None children: (Leaf[0] parent: Keys[1], Leaf[2] '
    'parent: Keys[1])',
)

five_data = [2, 4, 3, 1, 0]
insert_five = (
    five_data,
    'Node[1, 3] parent: None children: (Leaf[0] parent: Keys[1, 3], '
    'Leaf[2] parent: Keys[1, 3], Leaf[4] parent: Keys[1, 3])',
)

eight_data = [4, 6, 5, 3, 2, 7, 1, 0]
insert_eight = (
    eight_data,
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: '
    '(Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[5] parent: '
    'Keys[3] children: (Leaf[4] parent: Keys[5], Leaf[6, 7] parent: Keys[5]))',
)

twelve_data = [7, 6, 5, 1, 2, 8, 3, 9, 4, 11, 10, 0]
insert_twelve = (
    twelve_data,
    'Node[6] parent: None children: (Node[2, 4] parent: Keys[6] children: '
    '(Leaf[0, 1] parent: Keys[2, 4], Leaf[3] parent: Keys[2, 4], Leaf[5] '
    'parent: Keys[2, 4]), Node[8, 10] parent: Keys[6] children: (Leaf[7] '
    'parent: Keys[8, 10], Leaf[9] parent: Keys[8, 10], Leaf[11] parent: '
    'Keys[8, 10]))',
)

seventeen_data = [2, 5, 6, 9, 4, 10, 1, 3, 8, 7, 13, 14, 11, 12, 17, 15, 16]
insert_seventeen = (
    seventeen_data,
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)

hundred_data = [
    46, 5, 22, 15, 47, 14, 84, 87, 66, 98, 25, 96, 34, 21, 50, 56, 91, 81, 12,
    72, 64, 10, 68, 1, 32, 53, 71, 9, 3, 73, 88, 0, 28, 89, 44, 57, 19, 35, 65,
    63, 17, 82, 67, 41, 61, 78, 83, 39, 60, 26, 30, 99, 16, 95, 29, 77, 38, 86,
    6, 45, 33, 74, 42, 40, 31, 48, 51, 90, 59, 54, 97, 85, 43, 49, 62, 93, 75,
    24, 18, 27, 2, 52, 80, 11, 7, 79, 37, 13, 36, 4, 94, 58, 92, 76, 23, 70, 8,
    20, 55, 69
]
insert_hundred = (
    hundred_data,
    'Node[47] parent: None children: (Node[22] parent: Keys[47] children: '
    '(Node[10] parent: Keys[22] children: (Node[5] parent: Keys[10] '
    'children: (Node[1, 3] parent: Keys[5] children: (Leaf[0] parent: '
    'Keys[1, 3], Leaf[2] parent: Keys[1, 3], Leaf[4] parent: Keys[1, 3]), '
    'Node[7] parent: Keys[5] children: (Leaf[6] parent: Keys[7], Leaf[8, 9] '
    'parent: Keys[7])), Node[16] parent: Keys[10] children: (Node[12, 14] '
    'parent: Keys[16] children: (Leaf[11] parent: Keys[12, 14], Leaf[13] '
    'parent: Keys[12, 14], Leaf[15] parent: Keys[12, 14]), Node[19] parent: '
    'Keys[16] children: (Leaf[17, 18] parent: Keys[19], Leaf[20, 21] parent: '
    'Keys[19]))), Node[34] parent: Keys[22] children: (Node[30] parent: '
    'Keys[34] children: (Node[25, 28] parent: Keys[30] children: '
    '(Leaf[23, 24] parent: Keys[25, 28], Leaf[26, 27] parent: Keys[25, 28], '
    'Leaf[29] parent: Keys[25, 28]), Node[32] parent: Keys[30] children: '
    '(Leaf[31] parent: Keys[32], Leaf[33] parent: Keys[32])), Node[41] '
    'parent: Keys[34] children: (Node[37, 39] parent: Keys[41] children: '
    '(Leaf[35, 36] parent: Keys[37, 39], Leaf[38] parent: Keys[37, 39], '
    'Leaf[40] parent: Keys[37, 39]), Node[44] parent: Keys[41] children: '
    '(Leaf[42, 43] parent: Keys[44], Leaf[45, 46] parent: Keys[44])))), '
    'Node[72] parent: Keys[47] children: (Node[61] parent: Keys[72] '
    'children: (Node[56] parent: Keys[61] children: (Node[50, 53] parent: '
    'Keys[56] children: (Leaf[48, 49] parent: Keys[50, 53], Leaf[51, 52] '
    'parent: Keys[50, 53], Leaf[54, 55] parent: Keys[50, 53]), Node[59] '
    'parent: Keys[56] children: (Leaf[57, 58] parent: Keys[59], Leaf[60] '
    'parent: Keys[59])), Node[66] parent: Keys[61] children: (Node[64] '
    'parent: Keys[66] children: (Leaf[62, 63] parent: Keys[64], Leaf[65] '
    'parent: Keys[64]), Node[68, 70] parent: Keys[66] children: (Leaf[67] '
    'parent: Keys[68, 70], Leaf[69] parent: Keys[68, 70], Leaf[71] parent: '
    'Keys[68, 70]))), Node[84] parent: Keys[72] children: (Node[77] parent: '
    'Keys[84] children: (Node[74] parent: Keys[77] children: (Leaf[73] '
    'parent: Keys[74], Leaf[75, 76] parent: Keys[74]), Node[79, 81] parent: '
    'Keys[77] children: (Leaf[78] parent: Keys[79, 81], Leaf[80] parent: '
    'Keys[79, 81], Leaf[82, 83] parent: Keys[79, 81])), Node[91, 96] parent: '
    'Keys[84] children: (Node[86, 88] parent: Keys[91, 96] children: '
    '(Leaf[85] parent: Keys[86, 88], Leaf[87] parent: Keys[86, 88], '
    'Leaf[89, 90] parent: Keys[86, 88]), Node[94] parent: Keys[91, 96] '
    'children: (Leaf[92, 93] parent: Keys[94], Leaf[95] parent: '
    'Keys[94]), Node[98] parent: Keys[91, 96] children: (Leaf[97] '
    'parent: Keys[98], Leaf[99] parent: Keys[98])))))',
)


@pytest.mark.parametrize(
    ('data', 'expected'), [
        insert_three,
        insert_five,
        insert_eight,
        insert_twelve,
        insert_seventeen,
        insert_hundred,
    ],
    ids=[
        ' three ',
        ' five ',
        ' eight ',
        ' twelve ',
        ' seventeen ',
        ' hundred ',
    ]
)
def test_insert(data, expected):
    tt_tree = insert_tree(data)
    assert expected == str(tt_tree.root)


# three data
delete_three_leaf_left = (
    three_data,
    [0],
    'Leaf[1, 2] parent: None',
)
delete_three_leaf_right = (
    three_data,
    [2],
    'Leaf[0, 1] parent: None',
)
delete_three_root = (
    three_data,
    [1],
    'Leaf[0, 2] parent: None',
)


# five data
delete_five_leaf_left = (
    five_data,
    [0],
    'Node[3] parent: None children: (Leaf[1, 2] parent: Keys[3], Leaf[4] '
    'parent: Keys[3])',
)
delete_five_leaf_middle = (
    five_data,
    [2],
    'Node[3] parent: None children: (Leaf[0, 1] parent: Keys[3], Leaf[4] '
    'parent: Keys[3])',
)
delete_five_leaf_right = (
    five_data,
    [4],
    'Node[3] parent: None children: (Leaf[0, 1] parent: Keys[3], Leaf[2] '
    'parent: Keys[3])',
)
delete_five_root_left = (
    five_data,
    [1],
    'Node[3] parent: None children: (Leaf[0, 2] parent: Keys[3], Leaf[4] '
    'parent: Keys[3])',
)
delete_five_root_right = (
    five_data,
    [3],
    'Node[1] parent: None children: (Leaf[0, 2] parent: Keys[1], Leaf[4] '
    'parent: Keys[1])',
)


# eight data
delete_eight_left_leaf_left = (
    eight_data,
    [0],
    'Node[3, 5] parent: None children: (Leaf[1, 2] parent: Keys[3, 5], '
    'Leaf[4] parent: Keys[3, 5], Leaf[6, 7] parent: Keys[3, 5])',
)
delete_eight_left_leaf_right = (
    eight_data,
    [2],
    'Node[3, 5] parent: None children: (Leaf[0, 1] parent: Keys[3, 5], '
    'Leaf[4] parent: Keys[3, 5], Leaf[6, 7] parent: Keys[3, 5])',
)
delete_eight_right_leaf_left = (
    eight_data,
    [4],
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: '
    '(Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[6] parent: '
    'Keys[3] children: (Leaf[5] parent: Keys[6], Leaf[7] parent: Keys[6]))',
)
delete_eight_right_leaf_right0 = (
    eight_data,
    [6],
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: '
    '(Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[5] parent: '
    'Keys[3] children: (Leaf[4] parent: Keys[5], Leaf[7] parent: Keys[5]))',
)
delete_eight_right_leaf_right1 = (
    eight_data,
    [7],
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: '
    '(Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[5] parent: '
    'Keys[3] children: (Leaf[4] parent: Keys[5], Leaf[6] parent: Keys[5]))',
)
delete_eight_left_node = (
    eight_data,
    [1],
    'Node[3, 5] parent: None children: (Leaf[0, 2] parent: Keys[3, 5], '
    'Leaf[4] parent: Keys[3, 5], Leaf[6, 7] parent: Keys[3, 5])',
)
delete_eight_right_node = (
    eight_data,
    [5],
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: '
    '(Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[6] parent: '
    'Keys[3] children: (Leaf[4] parent: Keys[6], Leaf[7] parent: Keys[6]))',
)
delete_eight_root = (
    eight_data,
    [3],
    'Node[2, 5] parent: None children: (Leaf[0, 1] parent: Keys[2, 5], '
    'Leaf[4] parent: Keys[2, 5], Leaf[6, 7] parent: Keys[2, 5])',
)


# seventeen data - leaf -
delete_seventeen_leaf1 = (
    seventeen_data,
    [1],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[3] parent: Keys[5] children: (Leaf[2] parent: Keys[3], Leaf[4] '
    'parent: Keys[3]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)
delete_seventeen_leaf2 = (
    seventeen_data,
    [3],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)
delete_seventeen_leaf3 = (
    seventeen_data,
    [4],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], '
    'Leaf[3] parent: Keys[2]), Node[7] parent: Keys[5] children: '
    '(Leaf[6] parent: Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: '
    'Keys[9] children: (Node[11] parent: Keys[13] children: (Leaf[10] parent: '
    'Keys[11], Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] '
    'children: (Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)
delete_seventeen_leaf4 = (
    seventeen_data,
    [6],
    'Node[9, 13] parent: None children: (Node[2, 5] parent: Keys[9, 13] '
    'children: (Leaf[1] parent: Keys[2, 5], Leaf[3, 4] parent: Keys[2, 5], '
    'Leaf[7, 8] parent: Keys[2, 5]), Node[11] parent: Keys[9, 13] children: '
    '(Leaf[10] parent: Keys[11], Leaf[12] parent: Keys[11]), Node[15] parent: '
    'Keys[9, 13] children: (Leaf[14] parent: Keys[15], Leaf[16, 17] parent: '
    'Keys[15]))',
)
delete_seventeen_leaf5 = (
    seventeen_data,
    [8],
    'Node[9, 13] parent: None children: (Node[2, 5] parent: Keys[9, 13] '
    'children: (Leaf[1] parent: Keys[2, 5], Leaf[3, 4] parent: Keys[2, 5], '
    'Leaf[6, 7] parent: Keys[2, 5]), Node[11] parent: Keys[9, 13] children: '
    '(Leaf[10] parent: Keys[11], Leaf[12] parent: Keys[11]), Node[15] '
    'parent: Keys[9, 13] children: (Leaf[14] parent: Keys[15], Leaf[16, 17] '
    'parent: Keys[15]))',
)
delete_seventeen_leaf6 = (
    seventeen_data,
    [10],
    'Node[5, 9] parent: None children: (Node[2] parent: Keys[5, 9] children: '
    '(Leaf[1] parent: Keys[2], Leaf[3, 4] parent: Keys[2]), Node[7] parent: '
    'Keys[5, 9] children: (Leaf[6] parent: Keys[7], Leaf[8] parent: Keys[7]), '
    'Node[13, 15] parent: Keys[5, 9] children: (Leaf[11, 12] parent: '
    'Keys[13, 15], Leaf[14] parent: Keys[13, 15], Leaf[16, 17] parent: '
    'Keys[13, 15]))',
)
delete_seventeen_leaf7 = (
    seventeen_data,
    [12],
    'Node[5, 9] parent: None children: (Node[2] parent: Keys[5, 9] children: '
    '(Leaf[1] parent: Keys[2], Leaf[3, 4] parent: Keys[2]), Node[7] parent: '
    'Keys[5, 9] children: (Leaf[6] parent: Keys[7], Leaf[8] parent: Keys[7]), '
    'Node[13, 15] parent: Keys[5, 9] children: (Leaf[10, 11] parent: '
    'Keys[13, 15], Leaf[14] parent: Keys[13, 15], Leaf[16, 17] parent: '
    'Keys[13, 15]))',
)
delete_seventeen_leaf8 = (
    seventeen_data,
    [14],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[16] parent: Keys[13] children: '
    '(Leaf[15] parent: Keys[16], Leaf[17] parent: Keys[16])))',
)
delete_seventeen_leaf9 = (
    seventeen_data,
    [16],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[17] parent: Keys[15])))',
)
delete_seventeen_leaf10 = (
    seventeen_data,
    [17],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16] parent: Keys[15])))',
)
# seventeen data - node -
delete_seventeen_node1 = (
    seventeen_data,
    [2],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[3] parent: Keys[5] children: (Leaf[1] parent: Keys[3], Leaf[4] '
    'parent: Keys[3]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)
delete_seventeen_node2 = (
    seventeen_data,
    [7],
    'Node[9, 13] parent: None children: (Node[2, 5] parent: Keys[9, 13] '
    'children: (Leaf[1] parent: Keys[2, 5], Leaf[3, 4] parent: Keys[2, 5], '
    'Leaf[6, 8] parent: Keys[2, 5]), Node[11] parent: Keys[9, 13] children: '
    '(Leaf[10] parent: Keys[11], Leaf[12] parent: Keys[11]), Node[15] '
    'parent: Keys[9, 13] children: (Leaf[14] parent: Keys[15], Leaf[16, 17] '
    'parent: Keys[15]))',
)
delete_seventeen_node3 = (
    seventeen_data,
    [11],
    'Node[5, 9] parent: None children: (Node[2] parent: Keys[5, 9] '
    'children: (Leaf[1] parent: Keys[2], Leaf[3, 4] parent: Keys[2]), '
    'Node[7] parent: Keys[5, 9] children: (Leaf[6] parent: Keys[7], '
    'Leaf[8] parent: Keys[7]), Node[13, 15] parent: Keys[5, 9] children: '
    '(Leaf[10, 12] parent: Keys[13, 15], Leaf[14] parent: Keys[13, 15], '
    'Leaf[16, 17] parent: Keys[13, 15]))',
)
delete_seventeen_node4 = (
    seventeen_data,
    [15],
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: '
    '(Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] '
    'parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: '
    'Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: '
    '(Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[16] parent: Keys[13] children: '
    '(Leaf[14] parent: Keys[16], Leaf[17] parent: Keys[16])))',
)
delete_seventeen_node5 = (
    seventeen_data,
    [5],
    'Node[9, 13] parent: None children: (Node[2, 7] parent: Keys[9, 13] '
    'children: (Leaf[6] parent: Keys[2, 7], Leaf[8] parent: Keys[2, 7]), '
    'Node[11] parent: Keys[9, 13] children: (Leaf[10] parent: Keys[11], '
    'Leaf[12] parent: Keys[11]), Node[15] parent: Keys[9, 13] children: '
    '(Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15]))',
)
delete_seventeen_node6 = (
    seventeen_data,
    [13],
    'Node[5, 9] parent: None children: (Node[2] parent: Keys[5, 9] children: '
    '(Leaf[1] parent: Keys[2], Leaf[3, 4] parent: Keys[2]), Node[7] parent: '
    'Keys[5, 9] children: (Leaf[6] parent: Keys[7], Leaf[8] parent: '
    'Keys[7]), Node[11, 15] parent: Keys[5, 9] children: (Leaf[14] parent: '
    'Keys[11, 15], Leaf[16, 17] parent: Keys[11, 15]))',
)
delete_seventeen_root = (
    seventeen_data,
    [9],
    'Node[8, 13] parent: None children: (Node[2, 5] parent: Keys[8, 13] '
    'children: (Leaf[1] parent: Keys[2, 5], Leaf[3, 4] parent: Keys[2, 5], '
    'Leaf[6, 7] parent: Keys[2, 5]), Node[11] parent: Keys[8, 13] children: '
    '(Leaf[10] parent: Keys[11], Leaf[12] parent: Keys[11]), Node[15] parent: '
    'Keys[8, 13] children: (Leaf[14] parent: Keys[15], Leaf[16, 17] '
    'parent: Keys[15]))',
)


@pytest.mark.parametrize(
    ('data', 'nums', 'expected'), [
        delete_three_leaf_left,
        delete_three_leaf_right,
        delete_three_root,

        delete_five_leaf_left,
        delete_five_leaf_middle,
        delete_five_leaf_right,
        delete_five_root_left,
        delete_five_root_right,

        delete_eight_left_leaf_left,
        delete_eight_left_leaf_right,
        delete_eight_right_leaf_left,
        delete_eight_right_leaf_right0,
        delete_eight_right_leaf_right1,
        delete_eight_left_node,
        delete_eight_right_node,
        delete_eight_root,

        delete_seventeen_leaf1,
        delete_seventeen_leaf2,
        delete_seventeen_leaf3,
        delete_seventeen_leaf4,
        delete_seventeen_leaf5,
        delete_seventeen_leaf6,
        delete_seventeen_leaf7,
        delete_seventeen_leaf8,
        delete_seventeen_leaf9,
        delete_seventeen_leaf10,
        delete_seventeen_node1,
        delete_seventeen_node2,
        delete_seventeen_node3,
        delete_seventeen_node4,
        delete_seventeen_node5,
        delete_seventeen_node6,
        delete_seventeen_root,
    ],
    ids=[
        ' three leaf left ',
        ' three leaf right ',
        ' three root ',

        ' five leaf left ',
        ' five leaf middle ',
        ' five leaf right ',
        ' five root left ',
        ' five root right ',

        ' eight left leaf left ',
        ' eight left leaf right ',
        ' eight right leaf left ',
        ' eight right leaf right0 ',
        ' eight right leaf right1 ',
        ' eight left node ',
        ' eight right node ',
        ' eight root ',

        ' seventeen_leaf1 ',
        ' seventeen_leaf2 ',
        ' seventeen_leaf3 ',
        ' seventeen_leaf4 ',
        ' seventeen_leaf5 ',
        ' seventeen_leaf6 ',
        ' seventeen_leaf7 ',
        ' seventeen_leaf8 ',
        ' seventeen_leaf9 ',
        ' seventeen_leaf10 ',
        ' seventeen_node1 ',
        ' seventeen_node2 ',
        ' seventeen_node3 ',
        ' seventeen_node4 ',
        ' seventeen_node5 ',
        ' seventeen_node6 ',
        ' seventeen_root ',
    ]
)
def test_delete(data, nums, expected):
    tt_tree = delete_tree(data, nums)
    assert expected == str(tt_tree.root)
