# All_Libraries
This rep consists all of the libraries that I have till now.



# NumPy Basics & Core Concepts

A structured reference guide covering the fundamental operations of NumPy in Python, based on daily learning notes.

---

## 📌 Table of Contents
1. [Array Slicing](#1-array-slicing)
2. [Array Creation & Range Generation](#2-array-creation--range-generation)
3. [Reshaping Arrays & The `-1` Trick](#3-reshaping-arrays--the--1-trick)
4. [Specialized Array Initialization](#4-specialized-array-initialization)
5. [Data Type Conversion](#5-data-type-conversion)
6. [Statistical Operations & Axes](#6-statistical-operations--axes)
7. [Matrix Mathematics (Dot Product)](#7-matrix-mathematics-dot-product)

---

## 1. Array Slicing
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


## 2. Array Creation & Range Generation
Understanding standard Python ranges versus NumPy's optimized range function.

### Python Native Range
1. `range(start, stop, step)` generates a sequence of integers.
2. The `*` operator unpacks the sequence.


```python
print(*range(1, 10, 2))  # Output: 1 3 5 7 9
```