#!/usr/bin/env python3

""" 1. Let's execute multiple coroutines at the same time with async """

import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """Asynchronous coroutine that takes in an integer argument"""
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
