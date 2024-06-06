#!/usr/bin/env python3
"""Augment the following code."""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Augment the following code."""
    if lst:
        return lst[0]
    else:
        return None
