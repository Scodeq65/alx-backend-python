#!/usr/bin/env python3
"""
Module 3-tasks
This module defines a function to create an asyncio.Task from wait_random.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task to execute wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay time for wait_random.

    Returns:
        asyncio.Task: The task that will run the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
