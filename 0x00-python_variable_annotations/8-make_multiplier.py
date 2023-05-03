#!/usr/bin/env python3
"""Task 8's module.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a multiplier function.
    """
    def multiply(number: float) -> float:
        """Multiplies a number by a multiplier.
        """
        return number * multiplier