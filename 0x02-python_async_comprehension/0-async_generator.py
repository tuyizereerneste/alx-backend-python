"""Module for task 0
"""


import asyncio
import random


async def async_generator():
    """Coroutine that generates random numbers between 0 and 10, one number
    at a time.

    Yields:
        Generator[float, None, None]:  A random number between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
