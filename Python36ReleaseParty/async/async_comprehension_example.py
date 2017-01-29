# -*- coding: utf-8 -*-
"""
pep 530 -- asynchronous comprehensions

https://www.python.org/dev/peps/pep-0530
"""
import asyncio


async def aiter(num):
    for i in range(num):
        yield i


async def apow(num):
    return pow(num, 2)


async def run(num):
    data = [i async for i in aiter(num)]
    for i in data:
        print(i)
    print('-' * 12)
    power = [await apow(i) for i in data]
    for i in power:
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run(10))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
