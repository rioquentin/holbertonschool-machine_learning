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
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

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
