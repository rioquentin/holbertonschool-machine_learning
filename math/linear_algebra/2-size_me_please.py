#!/usr/bin/env python3


"""
Task 2 - Find matric shape
"""

def matrix_shape(matrix):
    """
    This calculate the shape of a matrix using 
    isinstance function in case there is nested list
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
