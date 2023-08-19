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
        
        for i in range(1, self.L):
            # Initialize weights using He et al. initialization
            self.weights["W{}".format(i)] = np.random.randn(layers[i], layers[i - 1]) * np.sqrt(2.0 / layers[i - 1])
            
            # Initialize biases to zeros
            self.weights["b{}".format(i)] = np.zeros((layers[i], 1))