#!/usr/bin/env python3
"""
Module 1-async_comprehension
This module defines a coroutine that
collects random numbers
using an async comprehension.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random
    numbers using an async comprehension
    over async_generator, and returns
    them as a list.

    Returns:
        List of 10 random floats
    """
    return [number async for number in async_generator()]
