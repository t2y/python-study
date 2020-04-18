"""
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
"""

s = 'パタトクカシーー'
# answer1
print('%s%s%s%s' % (s[0], s[2], s[4], s[6]))
print('{}{}{}{}'.format(s[0], s[2], s[4], s[6]))
print(f'{s[0]}{s[2]}{s[4]}{s[6]}')

# answer2
print(''.join(s[i] for i in range(0, 7, 2)))

# answer3
from operator import itemgetter
print(''.join(itemgetter(0, 2, 4, 6)(s)))

# answer4
print(''.join(c for i, c in enumerate(s) if i % 2 == 0))

# answer5
print(s[::2])
