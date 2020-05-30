
def add(x, *args):
    total = x
    for i in args:
        total += i
    print(f'{x=} + {args=} = {total}')

add(1, 2, 3)
add(1, 2)
add(1, 2, 3, 4, 5, 6, 7)
add(1)
