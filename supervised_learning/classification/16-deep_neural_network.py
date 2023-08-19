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
        if not isinstance(layers, list) or not layers:
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for l in range(1, self.L + 1):
            if not isinstance(layers[l - 1], int) or layers[l - 1] <= 0:
                raise TypeError("layers must be a list of positive integers")
            self.weights['W' +
                         str(l)] = np.random.randn(layers[l - 1], nx) * np.sqrt(2/nx)
            self.weights['b' + str(l)] = np.zeros((layers[l - 1], 1))
            nx = layers[l - 1]
