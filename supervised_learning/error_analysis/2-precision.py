#!/usr/bin/env python3

"""_summary_

    Returns:
        _type_: _description_
    """
import numpy as np


def precision(confusion):
    """ calculates the precision for each class in a confusion matrix """
    return np.diagonal(confusion) / np.sum(confusion, axis=0)
