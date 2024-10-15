#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
This module defines a coroutine that spawns multiple wait_random coroutines.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay time for each wait_random call.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
