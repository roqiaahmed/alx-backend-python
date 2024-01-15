#!/usr/bin/env python3

""" 4. Tasks """

import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Asynchronous coroutine that takes in an integer argument"""
    delays = []
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
