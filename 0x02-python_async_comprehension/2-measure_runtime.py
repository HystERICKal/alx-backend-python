#!/usr/bin/env python3
"""Write a run time for four parallel comprehensions."""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Write a run time for four parallel comprehensions."""
    temp_1 = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    temp_2 = time.time()
    return temp_2 - temp_1
