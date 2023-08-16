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

    def cost(self, Y, A):
        """
        Log Loss function
        """
        epsilon = 1.0000001
        m = Y.shape[1]
        L = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(epsilon - A))
        return L

    def evaluate(self, X, Y):
        """
        Evaluate
        """
        predicted_labels = self.forward_prop(X)
        cost = self.cost(Y, predicted_labels)
        predicted_labels = (predicted_labels >= 0.5).astype(int)
        return predicted_labels, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Perform a gradient descent
        """

        dw = 1 / Y.shape[1] * np.dot(X, (A - Y).T)
        db = 1 / Y.shape[1] * np.sum(A - Y)
        self.__W = self.__W - alpha * dw
        self.__b = self.__b - alpha * db

        return self.__W, self.__b
