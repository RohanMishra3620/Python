import matplotlib.pyplot as plt
x=['A','B','C','D','E']
y=[10,20,30,25,15]

plt.figure(figsize=(5,10))
ax1=plt.subplot()
ax1.bar(x,y,color=['r','g'])
plt.show()
