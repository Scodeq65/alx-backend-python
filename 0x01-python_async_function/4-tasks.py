#!/usr/bin/env python3
"""
Module 4-tasks
This module defines a coroutine that spawns multiple tasks using task_wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Coroutine that spawns task_wait_random n times with the specified max_delay,
    and returns the list of all delays in ascending order.

    Args:
        n (int): The number of tasks to spawn.
        max_delay (int): The maximum delay time for each task.

    Returns:
        List[float]: A list of delays from each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)  
    return delays
