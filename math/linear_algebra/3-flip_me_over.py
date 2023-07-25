#!/usr/bin/env python3

"""
Task 3 - Flip Me Over
"""


def matrix_transpose(matrix):
    """
    A function to transpose a matrix
    """
    result = []
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    for i in range(columns):
        transposed_row = []
        for j in range(rows):
            transposed_row.append(matrix[j][i])
        result.append(transposed_row)

    return result
