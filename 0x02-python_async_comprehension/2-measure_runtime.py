#!/usr/bin/env python3
""" Async Generator """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time

async def measure_time() -> float:
    """ measure_time
        measure the total runtime and return it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start