#!/usr/bin/env python3
# filepath: /home/mitali/ALU-Respository/alu-machine_learning/math/plotting/2-change_scale.py
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Create line plot
plt.plot(x, y)

# Set x-axis range
plt.xlim(0, 28650)

# Set logarithmic scale for y-axis
plt.yscale('log')

# Add labels and title
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')
plt.title('Exponential Decay of C-14')

# Display the plot
plt.show()