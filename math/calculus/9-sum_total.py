#!/usr/bin/env python3

"""Function to perform sigma sum

Returns:
    result
"""
import numpy as np


def summation_i_squared(n):
    """
    Create an array from 1 to n and then sum it up with **2
    """
    if not isinstance(n, int) or n < 1:
        return None
    return np.sum((np.arange(1, n + 1)) ** 2)
