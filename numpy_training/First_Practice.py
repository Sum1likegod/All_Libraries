import numpy as np

# arr_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(arr_1[:,2:4])

# print(*range(1, 10, 2),)


##29-06 Arange function is used to create an array of evenly spaced values within a given interval. It takes three parameters: start, stop, 
#and step. The start parameter specifies the starting value of the sequence, the stop parameter specifies the end value (exclusive), and
#the step parameter specifies the difference between each consecutive value in the sequence.
# print(np.arange(2, 10, 2))


##30-06 -1 can be used in reshape to automatically calculate the size of that dimension based on the size of the original array and the other
# specified dimensions. It allows you to reshape an array without explicitly specifying the size of that dimension, making it more flexible
# and convenient when working with arrays of varying sizes.
# 
# 
# 
# 
# 
# print(np.arange(2, 17, 2).reshape(-1,4))         #Output:[[ 2  4  6  8] 
#                                                         [10 12 14 16]]



# To create a array of zeros, you can use the np.zeros() function. Here's an example:

# print(np.zeros((3, 4)))



# To create an array of random numbers, you can use the np.random.rand() function. Here's an example:

# print(np.random.random((3, 4)))

#To create an array of random integers, you can use the np.random.randint() function. Here's an example:

# print(np.random.randint(1, 10, size=(3, 4)))

arr_1 = np.arange(10,dtype=float).reshape(2,-1)
# print(arr_1)


#To change the data type of an array, you can use the astype() method. Here's an example:
# print(arr_1.astype(int))

# print(np.mean(arr_1,axis=0))  #Output: [2.5 3.5 4.5 5.5 6.5]   average of each column


# print(np.mean(arr_1), np.std(arr_1))     #standard deviation is a measure of the amount of variation or dispersion in a set of values. It 
# quantifies how much the individual values in a dataset deviate from the mean (average) value.


arr_2 = np.arange(10, 20, dtype=float).reshape(2,-1)
# print(arr_2)

# print(np.dot(arr_1, arr_2)) #dot product of two arrays is a mathematical operation that takes two arrays and produces a new array by
#multiplying corresponding elements and summing the results. It is commonly used in linear algebra and various applications involving vectors
#and matrices.


# 01-07-2026

# To print every element of an array, you can use a loop or the np.nditer() function. Here's an example using a loop:

# print("Elements of arr_1:")
# for i in np.nditer(arr_1):
#     print(i)

# print(arr_2.ravel())   # ravel() function is used to flatten a multi-dimensional array into a one-dimensional array. It returns a new array
# that contains all the elements of the original array in a single dimension.


# 02-07-2026

# print(np.vstack((arr_1, arr_2)))  #vstack() function is used to vertically stack arrays. It takes a sequence of arrays as input and stacks 
# them along the vertical axis (row-wise) to create a new array. The resulting array will have the same number of columns as the input arrays,
# and the number of rows will be the sum of the rows of the input arrays.

# print(np.hstack((arr_1, arr_2)))  #hstack() function is used to horizontally stack arrays. It takes a sequence of arrays as input and stacks
# them along the horizontal axis (column-wise) to create a new array. The resulting array will have the same number of rows as the input
# arrays, and the number of columns will be the sum of the columns of the input arrays.

# arr_3 = np.arange(1, 16).reshape(5, 3)

# print(np.split(arr_3, 3, axis = 1))  #split() function is used to split an array into multiple sub-arrays along a specified axis. It takes the input 
# array and the number of splits as arguments and returns a list of sub-arrays. The resulting sub-arrays will have the same shape as the 
# original array, but they will be divided into smaller sections based on the specified number of splits.
