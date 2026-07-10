import numpy as np
import pandas as pd


arr_1 = np.arange(1, 11)

# print(arr_1.shape)

# In pandas, a Series is a one-dimensional labeled array capable of holding any data type. It can be created from a list, numpy array, or
#  dictionary. In this case, we are creating a pandas Series from a numpy array. And we are also specifying the index for the Series to be a
# range from 1 to 10.

series_1 = pd.Series(data = arr_1, index = ["Aman", "Bala", "Chitra", "Deepak", "Esha", "Farhan", "Gita", "Hari", "Isha", "Jatin"])
# print(series_1) # series_1 is a pandas Series object created from the numpy array arr_1, with an index ranging from 1 to 10. The output will
# display the values of the series along with their corresponding indices.


# print(series_1[0]) # Wrong way to access the first element of the series. It will raise a KeyError in future because the index is not 
# integer-based but label-based. The correct way to access the first element is by using the label "Aman".


series_nan = pd.Series(data = [1, 2, 1.5, 4, 5], dtype = "float32")

series_2 = pd.to_numeric(series_nan, errors = 'coerce') # The pd.to_numeric() function is used to convert the series_nan to a numeric data type.
# The errors='coerce' argument specifies that any non-numeric values (like NaN) should be converted to NaN. The resulting series_2 will have
# the same values as series_nan, but with any non-numeric values replaced by NaN.

print(series_2)

