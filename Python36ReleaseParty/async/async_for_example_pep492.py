# -*- coding: utf-8 -*-
"""
pep492 aiter with coroutine before pep 525

https://www.python.org/dev/peps/pep-0492
https://www.python.org/dev/peps/pep-0525
"""
import asyncio


async def yield_num(i):
    await asyncio.sleep(0.5)
    return i


class AsyncIterable:
    def __init__(self, coroutines):
        self.done = []
        self.not_done = coroutines

    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data is not None:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        if self.not_done:
            self.done, self.not_done = await asyncio.wait(
                self.not_done, return_when=asyncio.FIRST_COMPLETED)
        if not self.done:
            return None
        return self.done.pop().result()


async def run(num):
    coroutines = [yield_num(i) for i in range(num)]
    async for i in AsyncIterable(coroutines):
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run(10))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
