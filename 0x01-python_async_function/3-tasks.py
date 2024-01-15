#!/usr/bin/env python3

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

""" 3. Tasks """


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Asynchronous coroutine that takes in an integer argument (max_delay,n)"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
