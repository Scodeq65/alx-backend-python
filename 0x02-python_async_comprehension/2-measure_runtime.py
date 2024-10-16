#!/usr/bin/env python3
"""
Module 2-measure_runtime
This module defines a coroutine that
measures the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total
    runtime of running async_comprehension
    four times concurrently using
    asyncio.gather.

    Returns:
        Total runtime in seconds as a float
    """
    start_time = time.time()

    await asyncio.gather(*[async_comprehension() for _ in range(4)])

    total_runtime = time.time() - start_time
    return total_runtime
