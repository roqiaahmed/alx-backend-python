#!/usr/bin/env python3

""" Async Comprehension """

import asyncio
import time

as_comp = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Async Comprehension"""
    start = time.time()
    await asyncio.gather(as_comp(), as_comp(), as_comp(), as_comp())
    end = time.time()
    return end - start
