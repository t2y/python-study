"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
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

def word_bi_gram(s):
    for word in s.split():
        yield from char_bi_gram(word)

s = 'I am an NLPer'
print(f"'{s}'")
print(list(char_bi_gram(s)))
print(list(word_bi_gram(s)))
