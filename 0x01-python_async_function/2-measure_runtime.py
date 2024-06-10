#!/usr/bin/env python3
"""Measure the runtime."""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime."""
    temp = time.time()
    asyncio.run(wait_n(n, max_delay))
    temp_2 = time.time()

    temp_3 = temp_2 - temp
    return (temp_3/n)
