#!/usr/bin/env python3
""" Module for task 8
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that prints takes a float and prints
    a float function
    Parameter:
        @multiplier: float

    Return:
        multiplication of multiplier
    """
    return lambda m: m * multiplier
