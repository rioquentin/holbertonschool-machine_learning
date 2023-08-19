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

        for i in range(1, len(layers)):
            # Number of input units for the current layer
            fan_in = layers[i - 1]
            # Number of output units for the current layer
            fan_out = layers[i]
            weight_shape = (fan_out, fan_in)

            # He initialization
            stddev = np.sqrt(2.0 / fan_in)
            weights = np.random.normal(0, stddev, size=weight_shape)
            biases = np.zeros((fan_out, 1))  # Initialize biases to zeros

            self.weights['W' + str(i)] = weights
            self.weights['b' + str(i)] = biases
