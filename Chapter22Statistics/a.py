import numpy as np
data=np.random.randn(1000)
mean=np.mean(data)
n=len(data)
num=np.sum((data-mean)**3)/n
dem=(np.sum((data-mean)**2)/n)**(3/2)
skewness=num/dem
print("Mean",mean)
print("Skeness",skewness)