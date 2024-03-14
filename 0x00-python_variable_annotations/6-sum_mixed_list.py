#!/usr/bin/env python3
""" Module for task 6
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function to process a list of mixed integers and floats.

    Parameters:
        @mxd_list: (List[Union[int, float]])
        A list containing a mix of integers and floats.

    Returns:
        float: sum of mxd_list
    """
    return sum(mxd_list)
