#!/usr/bin/env python3

"""
Task 5 - Across The Planes
"""

matrix_shape = __import__('2-size_me_please').matrix_shape


def add_matrices2D(mat1, mat2):
    """
    add matrices
    """

    if mat1 is None or mat2 is None:
        return None

    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        res = []
        for x in range(len(mat1[0])):
            res.append(mat1[i][x] + mat2[i][x])
        result.append(res)

    return result
