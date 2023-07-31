#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line graph of y = x^3')
plt.grid(True)
plt.show()
