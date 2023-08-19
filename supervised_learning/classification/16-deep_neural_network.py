#!/usr/bin/env python3

"""
Task 16 - DeepNeuralNetwork
"""

import numpy as np


class DeepNeuralNetwork:
    """
    DeepNeuralNetwork Class
    """

    def __init__(self, nx, layers):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx <= 0:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or layers is None:
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(0, self.L):
            self.weights["W{}".format(
                i + 1)] = np.random.randn(layers[i], layers[i - 1])
            self.weights["b{}".format(i + 1)] = np.zeros((layers[i], 1))
