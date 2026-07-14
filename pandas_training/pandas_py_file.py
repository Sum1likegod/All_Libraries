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

series_nan = pd.Series([1, 2, 3, np.nan, 5, np.nan, 7, 8, 9, 10], dtype = float)

# series_2 = pd.to_numeric(series_nan, errors = 'coerce') # The pd.to_numeric() function is used to convert the series_nan to a numeric data type.
# The errors='coerce' argument specifies that any non-numeric values (like NaN) should be converted to NaN. The resulting series_2 will have
# the same values as series_nan, but with any non-numeric values replaced by NaN.

# print(series_2)

# print(series_1.loc(1))# throws an error because loc is used to access elements by label, and the correct syntax is series_1.loc["Aman"] 
# to access the value associated with the label "Aman".

# print(series_2.info())


dataframe_1 = pd.DataFrame(np.arange(1,11).reshape(5,2), columns = ["Column_1", "Column_2"], index = ["Row_1", "Row_2", "Row_3", "Row_4", "Row_5"])

print(dataframe_1)