#!/usr/bin/env python3
"""Task 11's module.
"""
from typing import Dict, TypeVar

T = TypeVar('T')
V = TypeVar('V')

def safely_get_value(dct: Dict[T, V], key: T, default: V = None) -> V:
    """Given a dictionary and a key, returns the value of the key.
    """
    if key in dct:
        return dct[key]
    else:
        return default