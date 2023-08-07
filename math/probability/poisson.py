#!/usr/bin/env python3

"""
Task 0 - nitialize Poisson
"""


class Poisson:
    """
    Poisson class
    """

    e = 2.7182818285

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

    def factorial(self, i):
        """
        Function to calculate the factorial of a number
        """

        return 1 if i == 0 else i * self.factorial(i - 1)

    def pmf(self, k):
        """
        Function to calculate the pmf of the data
        """

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        factorial_k = self.factorial(k)
        return (self.e ** (-self.lambtha) * self.lambtha ** k) / factorial_k

    def cdf(self, k):
        """
        Function to calculate the cdf of the data
        """

        cdf = 0

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        for i in range(0, k + 1):
            factorial_i = self.factorial(i)
            cdf += (self.e ** (-self.lambtha) *
                    (self.lambtha ** i)) / factorial_i
        return cdf
