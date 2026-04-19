import numpy as np
from scipy.stats import skew
import matplotlib.pyplot as plt 
print(skew(np.random.randn(1000)))
plt.hist((np.random.randn(1000)),bins=30)
plt.show()