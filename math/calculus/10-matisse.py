#!/usr/bin/env python3

"""
Task 10 - Derive happiness in oneself from a good day's work
"""


def poly_derivative(poly):
    """
    Derivate a polynomial function based in it's list of coeficient
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivative = []

    for power, coefficient in enumerate(poly[1:], start=1):
        if not isinstance(coefficient, (int, float)):
            return None
        derivative.append(power * coefficient)

    return derivative
