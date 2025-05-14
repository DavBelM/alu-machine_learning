#!/usr/bin/env python3
# filepath: /home/mitali/ALU-Respository/alu-machine_learning/math/plotting/1-scatter.py
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# Create scatter plot with magenta points
plt.scatter(x, y, color='magenta')

# Set labels for axes
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')

# Set title
plt.title("Men's Height vs Weight")

# Display the plot
plt.show()