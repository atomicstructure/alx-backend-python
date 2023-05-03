#!/usr/bin/env python3
""" Async Generator """
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time

async def measure_runtime():
    """ measure the start time
    """
    start = time.time()
    """ execute async_comprehension four times in parallel using asyncio.gather
    """
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    """measure the end time
    """
    end = time.time()
    """ return the total runtime
    """
    return end - start
