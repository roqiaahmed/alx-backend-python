#!/usr/bin/env python3

import time

wait_n = __import__("1-concurrent_coroutines").wait_n
""" 2. Measure the runtime """


def measure_time(n, max_delay):
    """Function that measures the total execution time for wait_n"""
    start = time.time()

    wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    return total_time / n
