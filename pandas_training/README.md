> **Note**: *In Pandas, data is structured as a two-dimensional grid where features (or variables) are represented as columns, and observations (or data points) are represented as rows.*

# 📌 Table of Contents
1. [Understanding the getitem FutureWarning](#-1-understanding-the-getitem-futurewarning)
    - [The Solution: .loc vs .iloc](#-the-solution-loc-vs-iloc)





## 🔮 1. Understanding the getitem FutureWarning
> 📅 Date Learned: 05-07-2026

When working with a Pandas Series, accessing data using standard bracket notation `[]` with an integer can cause ambiguity if your Series uses non-integer labels. Pandas will soon deprecate this behavior to align with how DataFrames work.

⚠️ **Warning**: Relying on `series[0]` when you have custom labels is considered bad practice in production code because it can lead to silent data retrieval errors if your index changes.

```python
import pandas as pd

# Creating a series with string labels
my_series = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

# THE OLD WAY (Triggers the FutureWarning):
print(my_series[0])
# Output: 100 
# (Will eventually break or return an error in future Pandas versions)
```

### 💡 The Solution: .loc vs .iloc
> 📅 Date Learned: 05-07-2026

To write clean, future-proof Pandas code, always explicitly declare how you are searching for your data using `.iloc` (Index Location) or `.loc` (Location).

💡 **Pro-Tip**: An easy way to remember this for technical interviews:

- `.iloc` stands for **I**nteger **LOC**ation (Position-based).

- `.loc` stands for **L**abel **LOC**ation (Name-based).

```python
import pandas as pd

my_series = pd.Series([100, 200, 300], index=['x', 'y', 'z'])

# THE RIGHT WAY - By Position (iloc)
print(my_series.iloc[0])
# Output: 100

# THE RIGHT WAY - By Label (loc)
print(my_series.loc['x'])
# Output: 100
```


