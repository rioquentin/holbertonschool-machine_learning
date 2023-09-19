#!/usr/bin/env python3

"""_summary_

Returns:
    _type_: _description_
"""
import numpy as np

def sensitivity(confusion):
    """ calculates the sensitivity for each class in a confusion matrix """
    return np.diagonal(confusion) / np.sum(confusion, axis=1)