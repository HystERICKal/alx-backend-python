#!/usr/bin/env python3
"""Add type annotations to the function."""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """Add type annotations to the function."""
    if key in dct:
        return dct[key]
    else:
        return default
