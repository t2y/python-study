# -*- coding: utf-8 -*-
"""
pep492 aiter using queue before pep 525

https://www.python.org/dev/peps/pep-0492
https://www.python.org/dev/peps/pep-0525
"""
import asyncio


async def yield_num(num, queue):
    for i in range(num):
        queue.put_nowait(i)
        await asyncio.sleep(0.5)


class AsyncIterable:
    def __init__(self, queue):
        self.queue = queue
        self.done = []

    def __aiter__(self):
        return self

    async def __anext__(self):
        data = await self.fetch_data()
        if data is not None:
            return data
        else:
            raise StopAsyncIteration

    async def fetch_data(self):
        while not self.queue.empty():
            self.done.append(self.queue.get_nowait())
        if not self.done:
            return None
        return self.done.pop(0)


async def consume_num(queue):
    async for i in AsyncIterable(queue):
        await asyncio.sleep(0.5)
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=event_loop)
    try:
        event_loop.create_task(yield_num(10, queue))
        event_loop.run_until_complete(consume_num(queue))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
