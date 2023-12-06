import numpy as np

# Generating random numbers
randNum = np.random.random((3,3))
print(randNum)

# Generating a range of values
seq = np.arange(1, 10, 1)
print(seq)
print(type(seq))

# linspace function. Third parameter tells how many values we want in between
# The difference between the values that we get will be same
lins = np.linspace(1, 10, 5)
print(lins)

# reshaping a array
arr = np.random.random((3,4))
print(arr)
reshape = np.reshape(arr, (6, 2)) # The size of both should be same i.e. 3 * 4 == 6 * 2
print(reshape)

# Converting an array of any Dimension to a 1-D array 
arr = arr.flatten()
print(arr)