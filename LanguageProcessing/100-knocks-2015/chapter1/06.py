"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ,XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

def char_bi_gram(s):
    length = len(s)
    if length < 2:
        yield s
        return

    for i, c in enumerate(s):
        yield c + s[i + 1]
        if i == length - 2:
            break

s1 = 'paraparaparadise'
s1_bi_gram = set(char_bi_gram(s1))
print(f's1: {s1_bi_gram}')

s2 = 'paragraph'
s2_bi_gram = set(char_bi_gram(s2))
print(f's2: {s2_bi_gram}')

def show_sets_operation(s1, s2):
    sum_of_sets = s1.copy()
    sum_of_sets.update(s2)
    print(f'sum: {sum_of_sets}')

    product_sets = s1.copy()
    product_sets.intersection_update(s2)
    print(f'product: {product_sets}')

    difference_sets = s1.copy()
    difference_sets.difference_update(s2)
    print(f'diff: {difference_sets}')

show_sets_operation(s1_bi_gram, s2_bi_gram)
