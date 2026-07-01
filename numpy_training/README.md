# NumPy Core Concepts & Data Science Fundamentals

A structured reference guide covering the fundamental operations of NumPy in Python. This repository serves as a daily learning log and a practical reference for handling numerical data efficiently.



## 📌 Table of Contents
1. [Array Slicing](#1-array-slicing)
2. [Array Creation & Range Generation](#2-array-creation--range-generation)
3. [Reshaping Arrays & The `-1` Trick](#3-reshaping-arrays--the--1-trick)
4. [Specialized Array Initialization](#4-specialized-array-initialization)
5. [Data Type Conversion](#5-data-type-conversion)
6. [Statistical Operations & Axes](#6-statistical-operations--axes)
7. [Matrix Mathematics (Dot Product)](#7-matrix-mathematics-dot-product)
8. [Iterating Through Arrays](#8-iterating-through-arrays)
9. [Flattening Arrays (Ravel)](#9-flattening-arrays-ravel)


---

## 🍕 1. Array Slicing
> 📅 **Date Learned:** 29-06-2026

Extracting specific rows and columns from multi-dimensional arrays using the `[rows, columns]` syntax.

```python
import numpy as np

arr_1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Syntax: [all rows, column index 2 up to 4 (exclusive)]
print(arr_1[:, 2:4])
# Output:
# [[3 4]
#  [7 8]]


```


## 🛠️ 2. Array Creation & Range Generation
> 📅 **Date Learned:** 29-06-2026

Understanding standard Python ranges versus NumPy's optimized range function.

### ↔️ Python Native Range
1. `range(start, stop, step)` generates a sequence of integers.
2. The `*` operator unpacks the sequence.

```python
print(*range(1, 10, 2))  # Output: 1 3 5 7 9
```

### 💯 NumPy `np.arange()`

Creates an array of evenly spaced values within a given interval.

- `start`: Starting value of the sequence.
- `stop`: End value (exclusive).
- `step`: The difference between each consecutive value.

```python
print(np.arange(2, 10, 2))  # Output: [2 4 6 8]
```

## 🔁 3. Reshaping Arrays & The `-1` Trick
> 📅 **Date Learned:** 30-06-2026

Changing the dimensions of an array without altering its underlying data.

Using `-1` in `.reshape()` tells NumPy to automatically calculate the exact size of that specific dimension based on the total length of the array and the other dimensions provided.

```python
# Creates 8 elements [2, 4, 6, 8, 10, 12, 14, 16]
# Reshapes to 4 columns, automatically calculating rows (-1 -> 2 rows)
print(np.arange(2, 17, 2).reshape(-1, 4))

# Output:
# [[ 2  4  6  8]
#  [10 12 14 16]]
```

## 🀠 4. Specialized Array Initialization
> 📅 **Date Learned:** 30-06-2026
### ℹ Initializing with Zeros
Creates an array filled entirely with `0.0` values of a specified shape tuple `(rows, columns)`.

```python
print(np.zeros((3, 4)))
```

### 🌀 Random Floats

Generates random floats uniformly distributed between `0.0` (inclusive) and `1.0` (exclusive).

```python
print(np.random.random((3, 4)))
```


### ༘⋆ Random Integers

Generates random integers within a specified range `(low, high, size)`.

```python
# Syntax: np.random.randint(low, high, size=(rows, cols))
print(np.random.randint(1, 10, size=(3, 4)))
```

## 💱 5. Data Type Conversion
> 📅 **Date Learned:** 30-06-2026

You can define an array's data type at creation using the `dtype` parameter, or change an existing array's type using the `.astype()` method.

```python
# Create a float array and reshape it (2 rows, columns calculated automatically)
arr_1 = np.arange(10, dtype=float).reshape(2, -1)
print(arr_1)
# Output: [[0. 1. 2. 3. 4.]
#          [5. 6. 7. 8. 9.]]

# Convert float array to integer array
print(arr_1.astype(int))
# Output: [[0 1 2 3 4]
#          [5 6 7 8 9]]
```

## 📈 6. Statistical Operations & Axes
> 📅 **Date Learned:** 30-06-2026

NumPy makes calculating descriptive statistics over whole arrays or specific axes simple.

`axis=0`: Performs operations downwards across rows (calculates stats for each individual column).

`axis=1`: Performs operations sideways across columns (calculates stats for each individual row).

### 😈 Mean (Average) Along an Axis

```python
# Calculates the mean of each column separately
print(np.mean(arr_1, axis=0))  
# Output: [2.5 3.5 4.5 5.5 6.5]
```

### 🌍 Global Statistics (Mean & Standard Deviation)

**Standard Deviation** `(np.std)`: A measure of the amount of variation or dispersion in a set of values. It quantifies how much the individual values in a dataset deviate from the mean (average) value.

```python
print("Mean:", np.mean(arr_1))
print("Std Dev:", np.std(arr_1))
```

## 🔢 7. Matrix Mathematics (Dot Product)
> 📅 **Date Learned:** 30-06-2026

The dot product is a fundamental linear algebra operation. For matrices, it performs matrix multiplication (multiplying rows by columns and summing the products).

⚠️ **Rule**: For `np.dot(A, B)` to work, the number of **columns in A** must match the number of **rows in B**.

```python
# Shape: (2, 5) -> 2 rows, 5 columns
arr_1 = np.arange(10, dtype=float).reshape(2, -1)

# Shape: (5, 2) -> 5 rows, 2 columns
arr_2 = np.arange(10, 20, dtype=float).reshape(-1, 2)

# Matrix Multiplied Result Shape: (2, 2)
print(np.dot(arr_1, arr_2))

# Output:
# [[ 130.  140.]
#  [ 430.  490.]]
```

### 🔑 Key Additions Made For Clarity (30-06-2026):
* **Axis Explanation:** Beginners often confuse `axis=0` and `axis=1`. I added a visual text note explaining that `axis=0` calculates column-wise averages.
* **Dot Product Warning:** Added a note about the dimension requirement for matrix dot products (`columns in A == rows in B`), which helps prevent the famous `ValueError` down the road.


---

## ⟳ 8. Iterating Through Arrays
> 📅 **Date Learned:** 01-07-2026

To efficiently loop through every single element of a multi-dimensional array (without needing nested `for` loops), use NumPy's `nditer()` function.

```python
# Assuming arr_1 is a multi-dimensional array
print("Elements of arr_1:")
for i in np.nditer(arr_1):
    print(i)
```

> ⚠️ **Warning:** By default, `nditer` treats the array as **read-only**. If you try to modify the elements while looping, you will get an error. To change values, you must explicitly tell NumPy by passing the `op_flags` argument:

```python
# To multiply every element by 2:
for i in np.nditer(arr_1, op_flags=['readwrite']):
    i[...] = i * 2

## 🏢 9. Flattening Arrays `(Ravel)`
> 📅 **Date Learned:** 01-07-2026

The `.ravel()` function is used to flatten a multi-dimensional array into a 1D (one-dimensional) array. It returns a new array that contains all the elements of the original array in a single sequence.

```python
# Assuming arr_2 is a 2D or 3D array
print(arr_2.ravel()) 
# Output: [x y z ...] (A clean 1D array)
```

> 💡 **Pro-Tip (`ravel` vs `flatten`):**
> * `.ravel()` creates a **view** of the original array. If you change a number in the raveled array, it **will permanently change** the original multi-dimensional array too! It is very fast but can be dangerous.
> * `.flatten()` creates a completely independent **copy**. Changes made to the flattened array will not affect your original data. Use this when you want to play it safe!