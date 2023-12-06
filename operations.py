import numpy as np
import matplotlib.pyplot as plt  # used for visualization purpose

arr = np.array(np.arange(1, 11, 1), ndmin = 3)
print(arr, type(arr))

# size function
mulArr = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(mulArr)
print("Total size : ", np.size(mulArr), mulArr.size)
print("Rows       : ", np.size(mulArr, 0)) # Total number of rows in arr
print("Columns    : ", np.size(mulArr, 1)) # Total number of columns in arr

print(mulArr.shape)
print(mulArr.dtype)
print(mulArr.ndim)

arr1 = np.zeros(shape = (4, 5), dtype=int) # by default dtype is float
print(arr1, arr1.dtype)

arr2 = np.ones(shape = (5, 3), dtype = int)
print(arr2, arr2.dtype)

# eye function return 2-D array where 1 is at the diagonal and zero elsewhere
print(np.eye(5, dtype=int))

# Empty function same as zeroes
emp = np.empty(shape = (5, 4))
print(type(emp), emp)

# Random function
print(np.random.rand(4, 3)) # Generates array of given shape with random value between 0-1

print(np.random.randint(low = 1, high = 11, size = 15)) # Returns an array from value 1-10 of size 15

# Creates an array of specified shape and fills it with random values as per standard normal distribution
print(np.random.randn(10))                            
print(plt.hist(np.random.randn(10)))

# logSpace function
print("Log Space function: ")
print(np.logspace(2, 4, 10))
print("-"*75)
print(np.logspace(2,4,10,base=2))

# Copy function
arr1 = np.arange(1, 11, 1)
arr2 = arr1
print(arr1, id(arr1))
print(arr2, id(arr2))

arr2 = np.copy(arr1)
print(arr1, id(arr1))
print(arr2, id(arr2))

# Seed function will return random numbers but if we execute again we will get same set of random numbers
np.random.seed(1)
arr = np.random.randint(1, 16, (4, 3))
print(arr)

# Mean, variance and standard deviation
np.random.seed(1)
arrr = np.random.randint(1, 15, 10)
print("arrr: ", arrr)
print(np.mean(arrr))
print(np.var(arrr))
print(np.std(arrr))

arr1 = np.arange(1, 10, 1)
print(arr1)
arr1[arr1 > 5] = 100
print(arr1)

# Creating transpose array
np.random.seed(11)
arr2 = np.random.randint(1, 25, (4, 5))
print(arr2)
print(arr2.transpose())