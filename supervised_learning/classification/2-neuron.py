#!/usr/bin/env python3

"""
Task 0 - Write a class Neuron
"""

import numpy as np


class Neuron:
    """
    Neuron class
    """

    def __init__(self, nx):
        """
        Class constructor
        """

        if not isinstance(nx, int):
            raise TypeError("nx must be an integer or a float")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        # Array of each weight of each input features
        self.__W = np.random.randn(1, nx)
        self.__b = 0  # Bias
        self.__A = 0  # Activate output of the neuron

    @property
    def W(self):
        """
        Getter for W
        """
        return self.__W

    @property
    def b(self):
        """
        Getter for b
        """
        return self.__b

    @property
    def A(self):
        """
        Getter for A
        """
        return self.__A

    def sigmoid(self, x):
        """
        Activation function
        """
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        """
        Function to calculate the forward propagation
        where X is a matrix X(nx, m) -->
        nx = number of input feature and m = numbers of examples
        """
        z = np.dot(self.W, X) + self.b
        self.__A = self.sigmoid(z)
        return self.__A
