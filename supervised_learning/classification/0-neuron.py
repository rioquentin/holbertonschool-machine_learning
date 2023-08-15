#!/usr/bin/env python3

"""
Task 0 - Write a class Neuron
"""

import numpy as np


class Neuron:

    def __init__(self, nx):
        """
        Class constructor
        """

        if not isinstance(nx, int) and not isinstance(nx, float):
            raise TypeError("nx must be an integer or a float")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
