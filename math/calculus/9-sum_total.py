#!/usr/bin/env python3

"""Function to perform sigma sum

Returns:
    result
"""


def summation_i_squared(n):
    """
    Create an array from 1 to n and then sum it up with **2
    """
    if not isinstance(n, int) or n < 1:
        return 0
    return n**2 + summation_i_squared(n - 1)
