#!/usr/bin/env python3
"""Write basic async function."""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Write basic async function."""
    temp = random.random() * max_delay
    await asyncio.sleep(temp)
    return temp
