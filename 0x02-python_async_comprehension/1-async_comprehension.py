#!/usr/bin/env python3
""" Module for task 1
"""

import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    return [i async for i in async_generator()]
