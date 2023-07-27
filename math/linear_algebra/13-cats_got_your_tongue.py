#!/usr/bin/env python3

import numpy as np

"""
Task 13 - Cat's Got Your Tongue
"""


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate with numpy with an axis
    """

    return np.concatenate((mat1, mat2), axis)
