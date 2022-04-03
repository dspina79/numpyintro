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

# more mathematical functions
print("The sum of the array is ", np.sum(y))
print("The mean of the array is ", np.mean(y))
print("The average of the array is ", np.average(y))
print("The standard deviation of the array is ", np.std(y))
print("The variance of the array is ", np.var(y))
print("Remember, the standard deviation is the square root of the variance.")
print("The min of the array is ", np.min(y))
print("The max of the array is ", np.max(y))
print("The index of the min of the array is ", np.argmin(y))
print("The index of the min of the array is ", np.argmax(y))
