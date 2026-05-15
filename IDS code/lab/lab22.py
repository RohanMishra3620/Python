import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a non-normal population (uniform distribution)
population = np.random.uniform(low=0, high=100, size=10000)

# Step 2: Take multiple samples and compute their means
sample_size = 30
num_samples = 1000

sample_means = []

for i in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# Step 3: Plot histogram of sample means
plt.hist(sample_means, bins=30, density=True)

plt.title("Central Limit Theorem Demonstration")
plt.xlabel("Sample Means")
plt.ylabel("Frequency")

plt.grid()
plt.show()