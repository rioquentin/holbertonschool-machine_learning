#!/usr/bin/env python3

"""
Task 6 - Initialize Normal class
"""


class Normal:
    """
    Normal class
    """

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

            self.mean = round(float(sum(data) / len(data)), 10)
            self.stddev = round(
                (sum((x - self.mean)**2 for x in data) / (len(data) - 1)) ** 0.5, 10)
