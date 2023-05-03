#!/usr/bin/env python3
"""Task 10's module.
"""
from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
