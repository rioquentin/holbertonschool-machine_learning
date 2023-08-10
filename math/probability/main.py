#!/usr/bin/env python3
import numpy as np
Binomial = __import__('binomial').Binomial

try:
    Binomial(n=0)
    print('FAIL')
except ValueError as e:
    print(e)
try:
    Binomial(n=-1)
    print('FAIL')
except ValueError as e:
    print(e)