#!/usr/bin/env python3

"""
Task 6 - Initialize Binomial class
"""


class Binomial:
    """
    Binomial Class
    """

    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            self.p = 1 - (variance / mean)
            self.n = int(round(mean / self.p))
            self.p = mean / self.n

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
        binomial_coeff = self.factorial(
            self.n) / (self.factorial(k) * self.factorial(self.n - k))
        return binomial_coeff * (self.p ** k) * ((1 - self.p) ** (self.n - k))
