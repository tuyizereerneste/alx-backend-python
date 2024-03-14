#!/usr/bin/env python3
"""Module for task 9
"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Fuction that Creates a list of tuples
    Parameters:
        @lst: list of strings to process
    Return:
        List[Tuple[str, int]]
    """
    return [(i, len(i)) for i in lst]
