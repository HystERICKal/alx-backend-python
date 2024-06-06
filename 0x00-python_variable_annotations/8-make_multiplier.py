#!/usr/bin/env python3
"""Make fucntion that multiplies."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make fucntion that multiplies."""
    return lambda x: x * multiplier
