#!/usr/bin/env python3

"""
Task 17 - Integrate
"""


def poly_integral(poly, C=0):
    """
    function def poly_integral(poly, C=0):
    """

    if not isinstance(poly, list):
        return None
    if all(isinstance(coeff, (int, float)) for coeff in poly):
        return None
    if not isinstance(C, int):
        return None

    integral_coeffs = [coeff / (i + 1) for i, coeff in enumerate(poly)]
    integral_coeffs.insert(0, C)

    while integral_coeffs and integral_coeffs[-1] == 0:
        integral_coeffs.pop()

    return integral_coeffs
