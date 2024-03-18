#!/usr/bin/env python3
"""Module for task 4
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that spawns task_wait_random n
    times with the specified max_delay.

    Parameters:
        n (int): The number of times to spawn
        task_wait_random coroutine.
        max_delay (int): The maximum delay time in seconds
        for each task_wait_random coroutine.

    Returns:
        List[float]: The list of all the delays (float values)
        in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return sorted(delay)
