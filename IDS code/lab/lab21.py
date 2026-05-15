# write a python program  to plot the normal distribution for a given mean and standard deviation

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = float(input("Enter mean value: "))
std_dev = float(input("Enter standard deviation: "))

x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

y = norm.pdf(x, mean, std_dev)

# Plot graph
plt.plot(x, y)
plt.title("Normal Distribution Curve")
plt.xlabel("Values")
plt.ylabel("Probability Density")
plt.grid()

plt.show()