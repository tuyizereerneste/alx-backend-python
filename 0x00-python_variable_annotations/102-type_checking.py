#!/usr/bin/env python3
""" Module for task 12
"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Function that zooms in on the elements of a tuple.

    Parameters:
        lst (Tuple): The tuple to zoom in on.
        factor (Union[int, float], optional):
        The factor by which to zoom in on the tuple.
        Defaults to 2.

    Returns:
        List: A list containing the zoomed-in elements of the tuple.
    """
    zoomed_in = [
        item for item in lst
        for i in range((factor))
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, int(3.0))
