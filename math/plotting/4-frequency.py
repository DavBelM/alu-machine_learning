#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create histogram
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')

# Add labels and title
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')

# Set x-axis range to cover all possible grades
plt.xlim(0, 100)

# Display the plot
plt.show()