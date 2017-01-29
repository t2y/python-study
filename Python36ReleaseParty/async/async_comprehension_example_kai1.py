# -*- coding: utf-8 -*-
"""
pep 530 -- asynchronous comprehensions

https://www.python.org/dev/peps/pep-0530
"""
import asyncio
from random import choice


async def do_something():
    while True:
        await asyncio.sleep(0.2)
        print('do something ...')


async def aiter(num):
    for i in range(num):
        await asyncio.sleep(0.1)
        print('%d yielding aiter ...' % i)
        yield i


async def apow(num):
    sleep_second = choice(range(3))
    await asyncio.sleep(sleep_second)
    print('%d applying apow ...' % num)
    return pow(num, 2)


async def run(num):
    data = [await apow(i) async for i in aiter(num)]
    for i in data:
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.create_task(do_something())
        event_loop.run_until_complete(run(10))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
