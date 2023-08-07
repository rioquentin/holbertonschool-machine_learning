#!/usr/bin/env python3

"""
Task 0 - nitialize Poisson
"""


class Poisson:
    """
    Poisson class
    """

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = sum(data) / len(data)
            
    def pmf(self, k):
        e = 2.7182818285
        factorial_k = 1
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        for i in range(1, k + 1):
            factorial_k *= i
        return (e ** (-self.lambtha) * self.lambtha ** k) / factorial_k
    