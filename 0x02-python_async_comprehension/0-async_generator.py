#!/usr/bin/env python3
"""
Module 0-async_generator
This module defines a coroutine that yields random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that asynchronously yields 10 random numbers between 0 and 10,
    pausing for 1 second between each yield.

    Returns:
        Generator of floats
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
