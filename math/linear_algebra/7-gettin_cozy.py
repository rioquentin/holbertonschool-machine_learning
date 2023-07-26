#!/usr/bin/env python3

"""
Task 7 - Gettin’ Cozy
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate matrices by axis
    """

    if axis == 0:
        return mat1 + mat2
    else:
        result = []
        for i in range(len(mat1)):
            result.append(mat1[i] + mat2[i])
        return result
