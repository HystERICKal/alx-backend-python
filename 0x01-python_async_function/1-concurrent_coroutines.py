#!/usr/bin/env python3
"""Spawn previous function."""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn previous function."""
    temp_1 = []
    temp_2 = []

    for i in range(n):
        task = wait_random(max_delay)
        temp_1.append(task)

    for task in asyncio.as_completed((temp_1)):
        delay = await task
        temp_2.append(delay)

    return temp_2
