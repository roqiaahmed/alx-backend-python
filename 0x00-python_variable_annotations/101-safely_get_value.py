#!/usr/bin/env python3

"""Define variables with type annotations."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[Union[T, None]]
) -> Union[Any, T]:
    """Augment the following code with the correct duck-typed annotations:"""
    if key in dct:
        return dct[key]
    else:
        return default
