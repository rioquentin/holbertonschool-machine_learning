#!/usr/bin/env python3

"""
Task 5 - Across The Planes
"""


def add_matrices2D(mat1, mat2):
    """
    add matrices
    """

    if not mat1 or not mat2:
        return None

    matrix_shape = __import__('2-size_me_please').matrix_shape
    
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    result = []

    for i in range(len(mat1)):
        res = []
        for x in range(len(mat1[0])):
            res.append(mat1[i][x] + mat2[i][x])
        result.append(res)

    return result
