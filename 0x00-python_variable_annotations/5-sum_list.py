#!/usr/bin/env python3
"""
This module contains a function 'sum_list'
that calculates the sum of a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    :param input_list: A list of float numbers
    :return: The sum of the float numbers in the list
    """
    return sum(input_list)
