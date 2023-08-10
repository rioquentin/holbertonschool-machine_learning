#!/usr/bin/env python3

"""
Task 6 - Initialize Normal class
"""


class Normal:
    """
    Normal class
    """

    pi = 3.1415926536
    e = 2.7182818285

    def __init__(self, data=None, mean=0., stddev=1.):
        if stddev <= 0:
            raise ValueError("stddev must be a positive value")

        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))
            self.stddev = float(
                (sum((x - self.mean)**2 for x in data) / len(data)) ** 0.5)

    def z_score(self, x):
        """
        Function to calculate the z-score
        """

        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Function to calculate the x-score
        """

        return self.mean + z * self.stddev

    def pdf(self, x):
        """
        Function to calculate pdf
        """
        sqrt_2_pi = (2 * self.pi) ** 0.5
        coefficient = 1 / (self.stddev * sqrt_2_pi)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        pdf_value = coefficient * (self.e ** exponent)
        return pdf_value

    def cdf(self, x):
        """
        Function to calculate the CDF
        """
        value = (x - self.mean) / (self.stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (self.pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + erf)
        return cdf
