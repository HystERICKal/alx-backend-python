#!/usr/bin/env python3
"""Call task_wait_random."""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call task_wait_random."""
    temp = []
    temp_1 = []

    for i in range(n):
        temp_2 = task_wait_random(max_delay)
        temp.append(temp_2)

    for j in asyncio.as_completed((temp)):
        delay = await j
        temp_1.append(delay)

    return temp_1
