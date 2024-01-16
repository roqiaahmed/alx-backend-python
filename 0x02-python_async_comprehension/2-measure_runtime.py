#!/usr/bin/env python3

""" Async Comprehension """

import asyncio
import time

async_comp = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Async Comprehension"""
    start = time.time()
    await asyncio.gather(async_comp(), async_comp(), async_comp(), async_comp())
    end = time.time()
    return end - start
