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

    def cost(self, Y, A):
        """
        Return the cost of the operation
        """

        epsilon = 1.0000001
        m = Y.shape[1]
        L = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(epsilon - A))
        return L

    def evaluate(self, X, Y):
        """
        Evaluate
        """
        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)
        predicted_labels = (A2 >= 0.5).astype(int)
        return predicted_labels, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
        Perform a gradient descent
        """

        m = Y.shape[1]
        dZ2 = A2 - Y
        dW2 = 1 / m * dZ2.dot(A1.T)
        db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)

        dZ1 = np.dot(self.W2.T, dZ2) * A1 * (1 - A1)
        dW1 = 1 / m * dZ1.dot(X.T)
        db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)
        self.__W1 -= alpha * dW1
        self.__b1 -= alpha * db1
        self.__W2 -= alpha * dW2
        self.__b2 -= alpha * db2

        return self.__W1, self.__b1, self.__W2, self.__b2

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """
        Function to train the model
        """

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            A1, A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, A1, A2, alpha)

        return self.evaluate(X, Y)
