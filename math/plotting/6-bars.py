#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Define people and fruit names
people = ['Farrah', 'Fred', 'Felicia']
fruit_names = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # Colors for each fruit

# Create positions for the bars
positions = np.arange(len(people))

# Create the stacked bar chart
fig, ax = plt.subplots()

# Initialize bottom position for stacking
bottom = np.zeros(3)

# Plot each fruit type as a bar, stacking them
for i in range(len(fruit_names)):
    ax.bar(positions, fruit[i], bottom=bottom, width=0.5, 
           color=colors[i], label=fruit_names[i])
    bottom += fruit[i]  # Update the bottom position for next stack

# Customize the plot
ax.set_xticks(positions)
ax.set_xticklabels(people)
ax.set_ylabel('Quantity of Fruit')
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.set_title('Number of Fruit per Person')
ax.legend()

plt.show()