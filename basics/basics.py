import numpy as np

z = np.zeros(4)
print(z)

np.random.seed(0)
y = np.random.randint(10, size=14)
print(y)

avg_y = np.average(y)
med_y = np.median(y)
print(avg_y)
print(med_y)
