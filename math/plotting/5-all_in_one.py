#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, grid = plt.subplots(nrows=3, ncols=2, figsize=(10, 8))

grid[0, 0].plot(y0, color='red')
grid[0, 0].set_title('Line graph of y = x^3', fontsize='x-small')
grid[0, 0].set_xlabel('X-axis', fontsize='x-small')
grid[0, 0].set_ylabel('Y-axis', fontsize='x-small')

grid[0, 1].scatter(x1, y1, color='magenta', s=10)
grid[0, 1].set_title('Men\'s Height vs Weight', fontsize='x-small')
grid[0, 1].set_xlabel('Height (in)', fontsize='x-small')
grid[0, 1].set_ylabel('Weight (lbs)', fontsize='x-small')

grid[1, 0].set_yscale('log')
grid[1, 0].plot(x2, y2)
grid[1, 0].set_title('Exponential Decay of C-14', fontsize='x-small')
grid[1, 0].set_xlabel('Time (years)', fontsize='x-small')
grid[1, 0].set_ylabel('Fraction Remaining', fontsize='x-small')

grid[1, 1].plot(x3, y31, 'r--', label='C-14')
grid[1, 1].plot(x3, y32, 'g-', label='Ra-226')
grid[1, 1].set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
grid[1, 1].legend(loc='upper right')
grid[1, 1].set_xlabel('Time (years)', fontsize='x-small')
grid[1, 1].set_ylabel('Fraction Remaining', fontsize='x-small')

# Remove the empty subplot in the last cell
grid[2, 1].remove()

# Create a new GridSpec to adjust subplot positions
gs = GridSpec(3, 2)
gs.update(hspace=0.5, wspace=0.3)

# Adjust the position of the histogram subplot to take the whole space
grid[2, 0] = plt.subplot(gs[2, :])

grid[2, 0].hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
grid[2, 0].set_title('Project A', fontsize='x-small')
grid[2, 0].set_xlabel('Grades', fontsize='x-small')
grid[2, 0].set_ylabel('Number of Students', fontsize='x-small')
grid[2, 0].set_xticks(np.arange(0, 101, 10))


plt.tight_layout()
plt.show()