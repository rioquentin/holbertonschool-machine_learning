#!/usr/bin/env python3

import numpy as np

"""
Task 25 -  One-Hot Decode
"""


def one_hot_decode(one_hot):
    """
    Decode
    """

    if not isinstance(one_hot, np.ndarray) or len(one_hot.shape) != 2:
        return None

    return np.argmax(one_hot, axis=0)
