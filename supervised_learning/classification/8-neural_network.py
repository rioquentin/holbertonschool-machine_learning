#!/usr/bin/env python3

"""
Task 8 Define Neural Network class
"""

import numpy as np


class NeuralNetwork:
    """
    NeuralNetwork Class
    """

    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0
        self.W2 = np.random.randn(nodes, nx)
        self.b2 = np.zeros((nodes, 1))
        self.A2 = 0
