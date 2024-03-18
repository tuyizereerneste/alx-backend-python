#!/usr/bin/env python3
""" Module for task 0
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that waits for a randon number.

    Parameter:
        max_delay: int

    Return:
        float: The actual delay time in seconds.
    """

    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
