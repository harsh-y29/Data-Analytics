import numpy as np

lst = [1,2,3]
arr = np.array(lst)
print(lst)
print(type(lst))
print(arr)
print(type(arr))

#finding dimension of an array
print(arr.ndim)

# finding shape of the array
print(arr.shape)

# size of the array
print(arr.size)

# data type of array element
print(arr.dtype)

# 2-D array
lst1 = [[1,2,3], [4,5,6], [7,8,9]]
arr1 = np.array(lst1)
print(lst1)
print(type(lst1))
print(arr1)
print(type(arr1))
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1.dtype)

# Creating array with zeroes and ones
zeros = np.zeros((3,5))
ones = np.ones((5,4))
print(zeros)
print(ones)