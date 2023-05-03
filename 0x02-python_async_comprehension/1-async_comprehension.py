#!/usr/bin/env python3
""" Async Comprehensions 
    Write a coroutine called async_comprehension that takes no arguments.
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> float:
    """ collect 10 random numbers using an async 
        comprehensing over async_generator
    """
    result = [i async for i in async_generator()]
    return result