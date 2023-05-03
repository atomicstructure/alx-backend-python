#!/usr/bin/env python3
"""Task 9's module.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Computes the length of a list of sequences.
    """
    return [(i, len(i)) for i in lst]
