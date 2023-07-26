#!/usr/bin/env python3

"""
Task 8 - Ridin’ Bareback
"""


def mat_mul(mat1, mat2):
    """
    Multiply two matrices
    """

    result = [[0 for a in range(len(mat2[0]))] for b in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat1[0])):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
