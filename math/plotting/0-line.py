#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y as a line graph with solid red line
plt.plot(np.arange(0, 11), y, 'r-')  # 'r-' specifies a solid red line

# Set the x-axis range from 0 to 10
plt.xlim(0, 10)

# Add labels and title for better visualization
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Function')

# Display the plot
plt.show()