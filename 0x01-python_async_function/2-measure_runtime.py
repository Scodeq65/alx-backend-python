#!/usr/bin/env python3
"""
Module 2-measure_runtime
This module defines a function to measure the execution time of wait_n.
"""

import asyncio
import time
from typing import Callable
wait_n = __import__('1_concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of coroutines to spawn.
        max_delay (int): The maximum delay time for each wait_random call.

    Returns:
        float: The average time taken for each call of wait_n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
