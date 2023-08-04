#!/usr/bin/env python3

"""
Task 17 - Integrate
"""


def poly_integral(poly, C=0):
    """
    Yeet
    """
    if not isinstance(poly, list):
        return None

    def is_valid(coeff):
        return isinstance(coeff, (int, float)) or \
               (isinstance(coeff, int) and coeff.is_integer())

    if not all(is_valid(coeff) for coeff in poly) or not isinstance(C, int):
        return None

    integral_coeffs = [coeff / (i + 1) for i, coeff in enumerate(poly)]
    while integral_coeffs and integral_coeffs[-1] == 0:
        integral_coeffs.pop()

    integral_coeffs_with_condition = []
    for coeff in integral_coeffs:
        if coeff.is_integer():
            integral_coeffs_with_condition.append(int(coeff))
        else:
            integral_coeffs_with_condition.append(coeff)

    return [C] + integral_coeffs_with_condition
