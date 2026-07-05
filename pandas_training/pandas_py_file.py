import numpy as np
import pandas as pd


arr_1 = np.arange(1, 11)

# print(arr_1.shape)

# In pandas, a Series is a one-dimensional labeled array capable of holding any data type. It can be created from a list, numpy array, or
#  dictionary. In this case, we are creating a pandas Series from a numpy array. And we are also specifying the index for the Series to be a
# range from 1 to 10.

series_1 = pd.Series(data = arr_1, index = ["Aman", "Bala", "Chitra", "Deepak", "Esha", "Farhan", "Gita", "Hari", "Isha", "Jatin"])
print(series_1) # series_1 is a pandas Series object created from the numpy array arr_1, with an index ranging from 1 to 10. The output will
# display the values of the series along with their corresponding indices.


print(series_1[0])
