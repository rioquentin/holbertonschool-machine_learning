#!/usr/bin/env python3

import numpy as np
Neuron = __import__('0-neuron').Neuron

try:
    nn = Neuron(2.0)
    print('FAIL')
except TypeError as e:
    if str(e) == 'nx must be an integer':
        print('OK', end='')
    else:
        print('FAIL')