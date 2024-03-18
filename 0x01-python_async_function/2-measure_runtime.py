#!/usr/bin/env python3
""" Module for task 2
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function to measure total delay time

    Parameters:
        n (int): The number of times to spawn wait_random coroutine.
        max_delay (int): The maximum delay time in seconds
        for each wait_random coroutine.

    Returns:
        float: The average time per coroutine.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
