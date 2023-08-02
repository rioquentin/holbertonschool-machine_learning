#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
people = ['Farrah', 'Fred', 'Felicia']

fig, ax = plt.subplots()
width = 0.5
bottom = np.zeros(len(people))

for i in range(len(fruits)):
    ax.bar(people, fruit[i], label=fruits[i], color=colors[i], width=width, bottom=bottom)
    bottom += fruit[i]
    
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_yticks(np.arange(0, 81, 10))
ax.legend()

plt.show()
