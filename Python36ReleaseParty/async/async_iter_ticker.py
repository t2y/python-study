# -*- coding: utf-8 -*-
"""
PEP 525 -- Asynchronous Generators

the difference of implementation for asynchronous generators

https://www.python.org/dev/peps/pep-0525/#rationale-and-goals
"""
import asyncio


class Ticker:
    """Yield numbers from 0 to `to` every `delay` seconds."""

    def __init__(self, delay, to):
        self.delay = delay
        self.i = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.to:
            raise StopAsyncIteration
        self.i += 1
        if i:
            await asyncio.sleep(self.delay)
        return i


async def ticker(delay, to):
    """Yield numbers from 0 to `to` every `delay` seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def run(delay, to):
    async for i in Ticker(delay, to):
        print(i)

    print('-' * 36)

    async for i in ticker(delay, to):
        print(i)


def main():
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(run(0.1, 3))
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
