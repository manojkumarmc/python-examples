import asyncio
from time import time
import types

async def call_me(n):
    await asyncio.sleep(1)
    print('Call me at {}'.format(n))

@types.coroutine
def my_gen():
    print('something is going on here')
    yield

async def main():
    await asyncio.wait([
        call_me(1),
        call_me(2),
        call_me(3)
    ])
    print('hello there')
    await my_gen()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

