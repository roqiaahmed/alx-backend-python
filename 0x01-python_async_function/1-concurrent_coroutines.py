#!/usr/bin/env python3


wait_random = __import__("0-basic_async_syntax").wait_random
""" 1. Let's execute multiple coroutines at the same time with async """ ""


async def wait_n(n, max_delay):
    """Asynchronous coroutine that takes in an integer argument"""
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    for i in range(0, len(delays)):
        for j in range(i + 1, len(delays)):
            if delays[i] > delays[j]:
                temp = delays[i]
                delays[i] = delays[j]
                delays[j] = temp
    return delays
