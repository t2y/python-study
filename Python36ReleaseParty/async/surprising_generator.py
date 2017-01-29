"""
design mistake

http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/
"""

def surprising_generator(n):
    if n in (0, 1):
        return [1]
    for i in range(n):
        yield i * 2


print('list(surprising_generator(0): ', list(surprising_generator(0)))
print('list(surprising_generator(1): ', list(surprising_generator(1)))
print('list(surprising_generator(2): ', list(surprising_generator(2)))
