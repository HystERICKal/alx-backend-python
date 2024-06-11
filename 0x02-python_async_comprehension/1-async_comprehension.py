#!/usr/bin/env python3
"""Write Async Comprehensions."""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Write Async Comprehensions."""
    outcomes = [x async for x in async_generator()]
    return outcomes
