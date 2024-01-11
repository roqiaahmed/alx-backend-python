#!/usr/bin/env python3

"""Define variables with type annotations."""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats."""
    return sum(mxd_lst)
