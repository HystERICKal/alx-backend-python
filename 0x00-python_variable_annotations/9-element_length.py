#!/usr/bin/env python3
"""Calculate the length."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Calculate the length."""
    return [(i, len(i)) for i in lst]
