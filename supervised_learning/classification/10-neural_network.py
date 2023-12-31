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

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
        Getter for W1
        """
        return self.__W1

    @property
    def b1(self):
        """
        Getter for b1
        """
        return self.__b1

    @property
    def A1(self):
        """
        Getter for A1
        """
        return self.__A1

    @property
    def W2(self):
        """
        Getter for W2
        """
        return self.__W2

    @property
    def b2(self):
        """
        Getter for b2
        """
        return self.__b2

    @property
    def A2(self):
        """
        Getter for A2
        """
        return self.__A2

    def sigmoid(self, x):
        """
        Activation function
        """
        return 1 / (1 + np.exp(-x))

    def forward_prop(self, X):
        """
        Function
        """

        Z1 = np.dot(self.W1, X) + self.b1
        self.__A1 = self.sigmoid(Z1)
        Z2 = np.dot(self.W2, self.A1) + self.b2
        self.__A2 = self.sigmoid(Z2)
        return self.__A1, self.__A2
