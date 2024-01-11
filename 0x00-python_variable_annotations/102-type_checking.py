#!/usr/bin/env python3

"""Define variables with type annotations."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Augment the following code with the correct duck-typed annotations:"""
    zoomed_in: Tuple = [i for item in lst for i in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
