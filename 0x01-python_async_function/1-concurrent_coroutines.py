#!/usr/bin/env python3
""" Module for task 1
"""

from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay.

    Parameters:
        n (int): The number of times to spawn wait_random coroutine.
        max_delay (int): The maximum delay time in seconds
        for each wait_random coroutine.

    Returns:
        List[float]: The list of all the delays (float values)
        in ascending order.
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
