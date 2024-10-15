#!/usr/bin/env python3
"""
Module 4-tasks
This module defines a coroutine that spawns multiple
task_wait_random coroutines.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns task_wait_random n times with the
    specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay time for each
        task_wait_random call.

    Returns:
        List[float]: A list of the delays in ascending order.
    """
    delays = []
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
