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

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for l in range(1, self.L + 1):
            if not isinstance(layers[l - 1], int) or layers[l - 1] <= 0:
                raise TypeError("layers must be a list of positive integers")
            W = np.random.randn(layers[l - 1], nx) * np.sqrt(2/nx)
            b = np.zeros((layers[l - 1], 1))
            self.weights['W' + str(l)] = W
            self.weights['b' + str(l)] = b
            nx = layers[l - 1]

    @property
    def L(self):
        """
        Getter for L
        """
        return self.__L

    @property
    def cache(self):
        """
        Getter for cache
        """
        return self.__cache

    @property
    def weights(self):
        """
        Getter for weights
        """
        return self.__weights

    def sigmoid(self, x):
        """
        Activation function
        """
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        """
        Function
        """
        self.__cache = {'A0': X}

        L = self.L
        for i in range(1, L + 1):
            Z = self.__weights['W' + str(i)].dot(
                self.__cache['A' + str(i - 1)]) + self.__weights['b' + str(i)]
            self.__cache['A' + str(i)] = self.sigmoid(Z)

        return self.__cache['A' + str(L)], self.__cache
