#!/usr/bin/env python3
""" Module for task 7
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Fuction that prints a tuple for str, int or float
    Parameters:
    @v: str
    @k: int or float
    Return: tuple of str and int or float
    """
    return (k, (v * v))
