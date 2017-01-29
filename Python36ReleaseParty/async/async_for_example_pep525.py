# -*- coding: utf-8 -*-
"""
pep 525 -- asynchronous generators

https://www.python.org/dev/peps/pep-0525
"""
import asyncio


async def aiter(num):
    for i in range(num):
        await asyncio.sleep(0.5)
        yield i


async def run(num):
    async for i in aiter(num):
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run(10))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
