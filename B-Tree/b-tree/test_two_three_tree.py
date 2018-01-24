import pytest

from two_three_tree import Node, TwoThreeTree


def insert_tree(data):
    root = Node([data.pop(0)])
    tt_tree = TwoThreeTree(root)
    for i in data:
        tt_tree.insert(i)
    tt_tree.update_parent(tt_tree.root)
    return tt_tree


three = (
    [2, 1, 0],
    'Node[1] parent: None children: (Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1])',
)

five_data = [2, 4, 3, 1, 0]
five = (
    five_data,
    'Node[1, 3] parent: None children: (Leaf[0] parent: Keys[1, 3], Leaf[2] parent: Keys[1, 3], Leaf[4] parent: Keys[1, 3])',
)

eight_data = [4, 6, 5, 3, 2, 7, 1, 0]
eight = (
    eight_data,
    'Node[3] parent: None children: (Node[1] parent: Keys[3] children: (Leaf[0] parent: Keys[1], Leaf[2] parent: Keys[1]), Node[5] parent: Keys[3] children: (Leaf[4] parent: Keys[5], Leaf[6, 7] parent: Keys[5]))',
)

twelve = (
    [7, 6, 5, 1, 2, 8, 3, 9, 4, 11, 10, 0],
    'Node[6] parent: None children: (Node[2, 4] parent: Keys[6] children: (Leaf[0, 1] parent: Keys[2, 4], Leaf[3] parent: Keys[2, 4], Leaf[5] parent: Keys[2, 4]), Node[8, 10] parent: Keys[6] children: (Leaf[7] parent: Keys[8, 10], Leaf[9] parent: Keys[8, 10], Leaf[11] parent: Keys[8, 10]))',
)

seventeen_data = [2, 5, 6, 9, 4, 10, 1, 3, 8, 7, 13, 14, 11, 12, 17, 15, 16]
seventeen = (
    seventeen_data,
    'Node[9] parent: None children: (Node[5] parent: Keys[9] children: (Node[2] parent: Keys[5] children: (Leaf[1] parent: Keys[2], Leaf[3, 4] parent: Keys[2]), Node[7] parent: Keys[5] children: (Leaf[6] parent: Keys[7], Leaf[8] parent: Keys[7])), Node[13] parent: Keys[9] children: (Node[11] parent: Keys[13] children: (Leaf[10] parent: Keys[11], Leaf[12] parent: Keys[11]), Node[15] parent: Keys[13] children: (Leaf[14] parent: Keys[15], Leaf[16, 17] parent: Keys[15])))',
)

hundred_data = [46, 5, 22, 15, 47, 14, 84, 87, 66, 98, 25, 96, 34, 21, 50, 56, 91, 81, 12, 72, 64, 10, 68, 1, 32, 53, 71, 9, 3, 73, 88, 0, 28, 89, 44, 57, 19, 35, 65, 63, 17, 82, 67, 41, 61, 78, 83, 39, 60, 26, 30, 99, 16, 95, 29, 77, 38, 86, 6, 45, 33, 74, 42, 40, 31, 48, 51, 90, 59, 54, 97, 85, 43, 49, 62, 93, 75, 24, 18, 27, 2, 52, 80, 11, 7, 79, 37, 13, 36, 4, 94, 58, 92, 76, 23, 70, 8, 20, 55, 69]
hundred = (
    hundred_data,
    'Node[47] parent: None children: (Node[22] parent: Keys[47] children: (Node[10] parent: Keys[22] children: (Node[5] parent: Keys[10] children: (Node[1, 3] parent: Keys[5] children: (Leaf[0] parent: Keys[1, 3], Leaf[2] parent: Keys[1, 3], Leaf[4] parent: Keys[1, 3]), Node[7] parent: Keys[5] children: (Leaf[6] parent: Keys[7], Leaf[8, 9] parent: Keys[7])), Node[16] parent: Keys[10] children: (Node[12, 14] parent: Keys[16] children: (Leaf[11] parent: Keys[12, 14], Leaf[13] parent: Keys[12, 14], Leaf[15] parent: Keys[12, 14]), Node[19] parent: Keys[16] children: (Leaf[17, 18] parent: Keys[19], Leaf[20, 21] parent: Keys[19]))), Node[34] parent: Keys[22] children: (Node[30] parent: Keys[34] children: (Node[25, 28] parent: Keys[30] children: (Leaf[23, 24] parent: Keys[25, 28], Leaf[26, 27] parent: Keys[25, 28], Leaf[29] parent: Keys[25, 28]), Node[32] parent: Keys[30] children: (Leaf[31] parent: Keys[32], Leaf[33] parent: Keys[32])), Node[41] parent: Keys[34] children: (Node[37, 39] parent: Keys[41] children: (Leaf[35, 36] parent: Keys[37, 39], Leaf[38] parent: Keys[37, 39], Leaf[40] parent: Keys[37, 39]), Node[44] parent: Keys[41] children: (Leaf[42, 43] parent: Keys[44], Leaf[45, 46] parent: Keys[44])))), Node[72] parent: Keys[47] children: (Node[61] parent: Keys[72] children: (Node[56] parent: Keys[61] children: (Node[50, 53] parent: Keys[56] children: (Leaf[48, 49] parent: Keys[50, 53], Leaf[51, 52] parent: Keys[50, 53], Leaf[54, 55] parent: Keys[50, 53]), Node[59] parent: Keys[56] children: (Leaf[57, 58] parent: Keys[59], Leaf[60] parent: Keys[59])), Node[66] parent: Keys[61] children: (Node[64] parent: Keys[66] children: (Leaf[62, 63] parent: Keys[64], Leaf[65] parent: Keys[64]), Node[68, 70] parent: Keys[66] children: (Leaf[67] parent: Keys[68, 70], Leaf[69] parent: Keys[68, 70], Leaf[71] parent: Keys[68, 70]))), Node[84] parent: Keys[72] children: (Node[77] parent: Keys[84] children: (Node[74] parent: Keys[77] children: (Leaf[73] parent: Keys[74], Leaf[75, 76] parent: Keys[74]), Node[79, 81] parent: Keys[77] children: (Leaf[78] parent: Keys[79, 81], Leaf[80] parent: Keys[79, 81], Leaf[82, 83] parent: Keys[79, 81])), Node[91, 96] parent: Keys[84] children: (Node[86, 88] parent: Keys[91, 96] children: (Leaf[85] parent: Keys[86, 88], Leaf[87] parent: Keys[86, 88], Leaf[89, 90] parent: Keys[86, 88]), Node[94] parent: Keys[91, 96] children: (Leaf[92, 93] parent: Keys[94], Leaf[95] parent: Keys[94]), Node[98] parent: Keys[91, 96] children: (Leaf[97] parent: Keys[98], Leaf[99] parent: Keys[98])))))',
)


@pytest.mark.parametrize(
    ('data', 'expected'), [
        three,
        five,
        eight,
        twelve,
        seventeen,
        hundred,
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
