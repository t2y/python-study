# -*- coding: utf-8 -*-
"""
implement Producer-Consumer pattern using asyncio

* native coroutine version

http://www.hyuki.com/dp/dpinfo.html#ProducerConsumer
"""
import asyncio
from random import choice


async def heavy_job():
    sleep_second = choice(range(3))
    await asyncio.sleep(sleep_second)


async def put(fruit, table):
    counter = 0
    while True:
        if table.empty():
            table.put_nowait(fruit)  # might occur QueueFull if full
            print('%d: put %s' % (counter, fruit))
            counter += 1
        await heavy_job()


async def get(consumer, table):
    counter = 0
    while True:
        if table.full():
            fruit = table.get_nowait()  # might occur QueueEmpty if empty
            print('%d: %s eats %s' % (counter, consumer, fruit))
            counter += 1
        await heavy_job()


def main():
    event_loop = asyncio.get_event_loop()
    table = asyncio.Queue(maxsize=1, loop=event_loop)
    try:
        # producer
        event_loop.create_task(put('apple', table))
        event_loop.create_task(put('banana', table))
        event_loop.create_task(put('candy', table))
        # consumer
        event_loop.create_task(get('bob', table))
        event_loop.create_task(get('john', table))
        event_loop.create_task(get('mary', table))
        # start
        event_loop.run_forever()
    finally:
        event_loop.close()


if __name__ == '__main__':
    main()
