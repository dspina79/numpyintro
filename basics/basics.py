import numpy as np

def print_array_details(y):
    print("")
    print(y)
    print("The sum of the array is ", np.sum(y))
    print("The mean of the array is ", np.mean(y))
    print("The median of the array is ", np.median(y))
    print("The average of the array is ", np.average(y))
    print("The standard deviation of the array is ", np.std(y))
    print("The variance of the array is ", np.var(y))
    print("Remember, the standard deviation is the square root of the variance.")
    print("The min of the array is ", np.min(y))
    print("The max of the array is ", np.max(y))
    print("The index of the min of the array is ", np.argmin(y))
    print("The index of the min of the array is ", np.argmax(y))



z = np.zeros(4)
print(z)

np.random.seed(0)
y = np.random.randint(10, size=25)

print_array_details(y)

arr = np.array([34,234,123,4352,3,345,345,345,3245,3245,234])
print_array_details(arr)