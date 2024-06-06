#!/usr/bin/env python3
"""Deal with complex types."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Deal with complex types."""
    return (k, float(v**2))
