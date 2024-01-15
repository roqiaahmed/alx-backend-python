#!/usr/bin/env python3

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random
""" 1. Let's execute multiple coroutines at the same time with async """ ""


async def task_wait_n(n, max_delay):
    """Asynchronous coroutine that takes in an integer argument (max_delay,n)"""
    delays = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        delays.append(await task)

    for i in range(0, len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                temp = delays[i]
                delays[i] = delays[j]
                delays[j] = temp
    return delays
