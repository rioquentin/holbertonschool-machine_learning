#!/usr/bin/env python3

"""
Task 24 - One-Hot Encode
"""

import numpy as np


def one_hot_encode(Y, classes):
    """
    Function to convert data to One Hot encode 
    """

    Map = np.zeros((classes, classes))
    for i in range(0, len(Map)):
        Map[Y[i]][i] = 1

    return Map
