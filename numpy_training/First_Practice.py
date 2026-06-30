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
print(arr_1)


#To change the data type of an array, you can use the astype() method. Here's an example:
# print(arr_1.astype(int))

# print(np.mean(arr_1,axis=0))  #Output: [2.5 3.5 4.5 5.5 6.5]   average of each column


# print(np.mean(arr_1), np.std(arr_1))     #standard deviation is a measure of the amount of variation or dispersion in a set of values. It 
# quantifies how much the individual values in a dataset deviate from the mean (average) value.


arr_2 = np.arange(10, 20, dtype=float).reshape(-1,2)
print(arr_2)

print(np.dot(arr_1, arr_2)) #dot product of two arrays is a mathematical operation that takes two arrays and produces a new array by
#multiplying corresponding elements and summing the results. It is commonly used in linear algebra and various applications involving vectors
#and matrices.




