#!/usr/bin/env python3

"""
Task 24 - One-Hot Encode
"""

import numpy as np


def one_hot_encode(Y, classes):
    if not isinstance(Y, np.ndarray) or len(Y.shape) != 1:
        return None
    if not isinstance(classes, int) or classes <= 0:
        return None
    if classes < 2:
        return None
    if not isinstance(Y, np.ndarray) or len(Y.shape) != 1:
        return None
    if not isinstance(classes, int) or classes <= 0:
        return None

    if np.max(Y) >= classes:
        return None

    m = Y.shape[0]
    one_hot_matrix = np.zeros((classes, m))
    one_hot_matrix[Y, np.arange(m)] = 1

    return one_hot_matrix
