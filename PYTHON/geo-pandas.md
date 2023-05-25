---
title: Pandas e GeoPandas
tags: studies, programação
use: Documentation
languages: Python
dependences: Python, pandas
---
> [Python Roadmap](./README.md)

<details> <summary>Table of Contents</summary>

- [Introduction](#introduction)
  - [Geting Started](#geting-started)
    - [Installation of Pandas](#installation-of-pandas)
    - [Import Pandas](#import-pandas)
  - [Series](#series)
    - [Labels](#labels)
    - [Key/Value Objects as Series](#keyvalue-objects-as-series)
  - [DataFrames](#dataframes)
    - [Indexing and selecting data](#indexing-and-selecting-data)
  - [Analyse Data](#analyse-data)
    - [Read `.csv`](#read-csv)
    - [Read `JSON`](#read-json)
      - [Dictionary as JSON](#dictionary-as-json)
    - [Viewing the Data](#viewing-the-data)
- [Cleaning Data](#cleaning-data)
  - [Clean Empty Cells](#clean-empty-cells)
    - [Replacing Empty Values](#replacing-empty-values)
    - [Remove Wrong Data](#remove-wrong-data)
  - [Remove Duplicates](#remove-duplicates)
- [Advanced](#advanced)
  - [Correlations](#correlations)
    - [Finding Relationships](#finding-relationships)
    - [Perfect Correlation:](#perfect-correlation)
    - [Good Correlation:](#good-correlation)
    - [Bad Correlation:](#bad-correlation)
  - [Plotting](#plotting)
    - [Scatter Plot](#scatter-plot)
    - [Histogram](#histogram)
- [References](#references)

</details>

---

# Introduction

- **What is**
	Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

- **Why use**
	Pandas allows us to analyze big data and make conclusions based on statistical theories. Pandas can clean messy data sets, and make them readable and relevant. Relevant data is very important in data science.

- **What Can Pandas Do?**
	Pandas gives you answers about the data. Like:
	-   Is there a correlation between two or more columns?
	-   What is average value?
	-   Max value?
	-   Min value?

- [Codebase](https://github.com/pandas-dev/pandas)

- **When to use?**
  > [Xukrao](https://stackoverflow.com/questions/45285743/when-to-use-pandas-series-numpy-ndarrays-or-simply-python-dictionaries)
  > **Use the simplest data structure that still satisfies your needs**.
  > First consider [Dictionaries](../Other/ds_hash_table.md) / [Lists](../Other/ds_array.md). If these allow you to do all data operations that you need, then all is fine. If not, start considering numpy arrays. Some typical reasons for moving to numpy arrays are:
  >  -   Your data is 2-dimensional (or higher). Although nested dictionaries/lists can be used to represent multi-dimensional data, in most situations numpy arrays will be more efficient.
  >  -   You have to perform a bunch of numerical calculations. As already pointed out by _zhqiat_, numpy will give a significant speed-up in this case. Furthermore numpy arrays come bundled with a large amount of [mathematical functions](https://docs.scipy.org/doc/numpy/reference/routines.math.html).
  > Then there are also some typical reasons for going beyond numpy arrays and to the more-complex but also more-powerful pandas series/dataframes:
  >  -   You have to merge multiple data sets with each other, or do reshaping/reordering of your data. [This diagram](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf) gives a nice overview of all the 'data wrangling' operations that pandas allows you to do.
  >  -   You have to import data from or export data to a specific file format like Excel, HDF5 or SQL. Pandas comes with convenient [import/export functions](https://pandas.pydata.org/pandas-docs/stable/io.html) for this.

## Geting Started

### Installation of Pandas

If you have [Python](https://www.w3schools.com/python/default.asp) and [PIP](https://www.w3schools.com/python/python_pip.asp) already installed on a system, then installation of Pandas is very easy.
Install it using this command:
```bash
pip install pandas
```

If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

### Import Pandas

Once Pandas is installed, import it in your applications by adding the `import` keyword:

```python
import pandas
```

As any Library, the import name can be modified using `as`, usually imported under the `pd` alias.
Now that Pandas is imported and ready to use. See example:
```python
import pandas as pd  
  
mydataset = {  
  'cars': ["BMW", "Volvo", "Ford"],  
  'passings': [3, 7, 2]  
}
myvar = pd.DataFrame(mydataset)
# Print
print(myvar)
```

## Series

A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.
Works like a filter wich will list all the given indexes and values linked to them.

> i.e. Create a simple Pandas Series from a list:
```python
import pandas as pd  

a = [1, 7, 2]  
myvar = pd.Series(a)  
# Print
print(myvar)
```

### Labels

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc. This label can be used to access a specified value.

> i.e. Return the first value of the Series:

```python
print(myvar[0])
```

With the `index` argument, you can name your own labels. And when you have created labels, you can access an item by referring to the label.

```python
import pandas as pd  
  
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x","y","z"])  
# Print
print(myvar) # full series
print(myvar["y"]) # series item
```

### Key/Value Objects as Series

You can also use a key/value object, like a dictionary, when creating a Series.

```python
import pandas as pd  
  
calories = {"day1": 420, "day2": 380, "day3": 390}  
myvar = pd.Series(calories)  
# Print
print(myvar)
```

## DataFrames

A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

<img src="https://pandas.pydata.org/docs/_images/01_table_dataframe.svg" alt="Df Structure" style="background-color:white" width="400">


```python
import pandas as pd  
  
data = {  
  "calories": [420, 380, 390],  
  "duration": [50, 40, 45]  
}  
#load data into a DataFrame object:  
df = pd.DataFrame(data) 
print(df)

# Or define the columns before receiving the data
col = ['day', 'excercise', 'calories', 'duration']
df_workout = pd.DataFrame(columns=col)
df_workout = pd.DataFrame(data)
print(df_workout)
```

There´s another way to add data in the DF, is using loops and [`.append(_other_, _ignore_index=False_, _verify_integrity=False_, _sort=False_)`](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.append.html) method:

Parameters

- **other** (*DataFrame or Series/dict-like object, or list of these*), the data to append.

- **ignore_index** (*bool, default False*), if True, the resulting axis will be labeled 0, 1, …, `n-1`.

- **verify_integrity** (*bool, default False*), if True, raise ValueError on creating index with duplicates.

- **sort** (*bool, default False*), sort columns if the columns of self and other are not aligned.

```python
new_row = {'day': 1, 'excercise': "burple", 'calories': 1500, 'duration': 5,}

df_workout = df_workout.append(new_row, ignore_index=True)
```

Please note that **the `return` is a new DataFrame**, so if you want to add to an existing one, you have to reassign.

> From [version 2.0.0 changes](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html#removal-of-prior-version-deprecations-changes) the `.append()` method was removed.
> *Removed deprecated `Series.append()`, `DataFrame.append()`, use `concat()` instead ([GH35407](https://github.com/pandas-dev/pandas/issues/35407))*

The [`.concat(_objs_, _*_, _axis=0_, _join='outer'_, _ignore_index=False_, _keys=None_, _levels=None_, _names=None_, _verify_integrity=False_, _sort=False_, _copy=None_)`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat) with the following parameters:
- **objs**: *a sequence or mapping of Series or DataFrame objects*, If a mapping is passed, the sorted keys will be used as the keys argument, unless it is passed, in which case the values will be selected (see below). Any None objects will be dropped silently unless they are all None in which case a ValueError will be raised.

- **axis**: *{0/’index’, 1/’columns’}, **default** 0*, the axis to concatenate along.

- **join**: *{‘inner’, ‘outer’}, **default** ‘outer’*, how to handle indexes on other axis (or axes).

- **ignore_index**: *bool, **default** False*, if True, do not use the index values along the concatenation axis. The resulting axis will be labelled 0, …, n - 1.

- **keys**: *sequence, **default** None*, if multiple levels passed, should contain tuples. Construct hierarchical index using the passed keys as the outermost level.

- **levels**: *list of sequences, **default** None*, specific levels (unique values) to use for constructing a MultiIndex. Otherwise they will be inferred from the keys.

- **names**: *list, **default** None*, names for the levels in the resulting hierarchical index.

- **verify_integrity**: *bool, **default** False*, check whether the new concatenated axis contains duplicates. This can be very expensive relative to the actual data concatenation. 

- **sort**: *bool, **default** False*, sort non-concatenation axis if it is not already aligned.

- **copy**: *bool, **default** True*, if False, do not copy data unnecessarily.

And returns a object witch is a `Series` or a `DataFrame`.
An usage code example:

```python
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
```

### Indexing and selecting data

The axis labelling information in pandas objects serves many purposes:

-   Identifies data (i.e. provides _metadata_) using known indicators, important for analysis, visualization, and interactive console display.
-   Enables automatic and explicit data alignment.
-   Allows intuitive getting and setting of subsets of the data set.

Object selection has had a number of user-requested additions in order to support more explicit location based indexing. pandas now supports three types of multi-axis indexing.

-   `.loc` is primarily label based, but may also be used with a boolean array. `.loc` will raise `KeyError` when the items are not found. Allowed inputs are:
  -   A **single label**
	  - e.g. `5` or `'a'` (Note that `5` is interpreted as a _label_ of the index. This use is **not** an integer position along the index.).
  -   A **list or array of labels**
	  - `['a', 'b', 'c']`.
  -   A **slice object with labels** 
	  - `'a':'f'` (Note that contrary to usual Python slices, **both** the start and the stop are included, when present in the index! See [Slicing with labels](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing#indexing-slicing-with-labels) and [Endpoints are inclusive](https://pandas.pydata.org/docs/user_guide/indexing.html#indexingadvanced.html#advanced-endpoints-are-inclusive))
  -   A boolean arrays 
	  - (any `NA` values will be treated as `False`).
  -   A **`callable` function with one argument** (the calling Series or DataFrame) and that returns valid output for indexing (one of the above)
> See more at [Selection by Label](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing#indexing-label).

-   `.iloc` is primarily integer position based (from `0` to `length-1` of the axis), but may also be used with a boolean array. `.iloc` will raise `IndexError` if a requested indexer is out-of-bounds, except _slice_ indexers which allow out-of-bounds indexing. (this conforms with Python/NumPy _slice_ semantics). Allowed inputs are:
  -   An **integer**
	  - e.g. `5`.
  -   A **list or array of integers**
	  - `[4, 3, 0]`.
  -   A **slice object with ints** 
	  - `1:7`.
  -   A **boolean array** (any `NA` values will be treated as `False`).
  -   A **`callable` function with one argument** (the calling Series or DataFrame) and that returns valid output for indexing (one of the above).
> See more at [Selection by Position](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing#indexing-integer), [Advanced Indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexingadvanced.html#advanced) and [Advanced Hierarchical](https://pandas.pydata.org/docs/user_guide/indexing.html#indexingadvanced.html#advanced-advanced-hierarchical).

-   `.loc`, `.iloc`, and also `[]` indexing can accept a `callable` as indexer. 
> See more at [Selection By Callable](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing#indexing-callable).

## Analyse Data

### Read `.csv`

CSV files can be read by Pandas and converted to a DataFrame.
> If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows. Use `to_string()` to print the entire DataFrame.

```python
import pandas as pd
# Read file
df = pd.read_csv('data.csv')
# Print
print(df.to_string())
```

### Read `JSON`

Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

```python
import pandas as pd  
# Read file
df = pd.read_json('data.json')  
# Print
print(df.to_string())
```

#### Dictionary as JSON

> **JSON = Python Dictionary**
> JSON objects have the same format as Python dictionaries.

If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

```python
import pandas as pd  
  
data = {  
  "Duration":{  
    "0":60,  
    "1":60,  
    "2":60,  
    "3":45,  
    "4":45,  
    "5":60  
  },  
  "Pulse":{  
    "0":110,  
    "1":117,  
    "2":103,  
    "3":109,  
    "4":117,  
    "5":102  
  },  
  "Maxpulse":{  
    "0":130,  
    "1":145,  
    "2":135,  
    "3":175,  
    "4":148,  
    "5":127  
  },  
  "Calories":{  
    "0":409,  
    "1":479,  
    "2":340,  
    "3":282,  
    "4":406,  
    "5":300  
  }  
}  
# Read
df = pd.DataFrame(data)  
# Print
print(df)
```

### Viewing the Data

One of the most used method for getting a quick overview of the DataFrame, is the `head()` method.

The `head(n)` method returns the headers and a specified number (`n`) of rows, starting from the top.
> If the number of rows is not specified, the `head()` method will return the top 5 rows.

```python
import pandas as pd  
# Read file
df = pd.read_csv('data.csv')  
# Print
print(df.head(10))
```

Same as head, there is also a `tail()` method for viewing the _last_ rows of the DataFrame.
The `tail()` method returns the headers and a specified number of rows, starting from the bottom.

The DataFrames object has a method called `info()`, that gives you more information about the data set.
- RangeIndex - number of rows
- Data columns - number of columns
- columns names, non-null elements and types
- dtypes
- memory usage

```python
print(df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   Duration  169 non-null    int64  
#  1   Pulse     169 non-null    int64  
#  2   Maxpulse  169 non-null    int64  
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
# None
```

# Cleaning Data

Data cleaning means fixing bad data in your data set.

Bad data could be:

-   Empty cells
-   Data in wrong format
-   Wrong data
-   Duplicates 

<details> <summary>E.g. Dataset info</summary>

  <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
    .tg .tg-0lax{text-align:left;vertical-align:top}
  </style>
  <table class="tg">
    <thead>
      <tr>
        <th class="tg-0pky"></th>
        <th class="tg-0pky">Duration</th>
        <th class="tg-0pky">Date</th>
        <th class="tg-0pky">Pulse</th>
        <th class="tg-0pky">Maxpulse</th>
        <th class="tg-0pky">Calories</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="tg-0pky">0</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/01'</td>
        <td class="tg-0pky">110</td>
        <td class="tg-0pky">130</td>
        <td class="tg-0pky">409.1</td>
      </tr>
      <tr>
        <td class="tg-0pky">1</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/02'</td>
        <td class="tg-0pky">117</td>
        <td class="tg-0pky">145</td>
        <td class="tg-0pky">479.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">2</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/03'</td>
        <td class="tg-0pky">103</td>
        <td class="tg-0pky">135</td>
        <td class="tg-0pky">340.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">3</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">'2020/12/04'</td>
        <td class="tg-0pky">109</td>
        <td class="tg-0pky">175</td>
        <td class="tg-0pky">282.4</td>
      </tr>
      <tr>
        <td class="tg-0pky">4</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">'2020/12/05'</td>
        <td class="tg-0pky">117</td>
        <td class="tg-0pky">148</td>
        <td class="tg-0pky">406.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">5</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/06'</td>
        <td class="tg-0pky">102</td>
        <td class="tg-0pky">127</td>
        <td class="tg-0pky">300.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">6</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/07'</td>
        <td class="tg-0pky">110</td>
        <td class="tg-0pky">136</td>
        <td class="tg-0pky">374.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">7</td>
        <td class="tg-0pky">450</td>
        <td class="tg-0pky">'2020/12/08'</td>
        <td class="tg-0pky">104</td>
        <td class="tg-0pky">134</td>
        <td class="tg-0pky">253.3</td>
      </tr>
      <tr>
        <td class="tg-0pky">8</td>
        <td class="tg-0pky">30</td>
        <td class="tg-0pky">'2020/12/09'</td>
        <td class="tg-0pky">109</td>
        <td class="tg-0pky">133</td>
        <td class="tg-0pky">195.1</td>
      </tr>
      <tr>
        <td class="tg-0pky">9</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/10'</td>
        <td class="tg-0pky">98</td>
        <td class="tg-0pky">124</td>
        <td class="tg-0pky">269.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">10</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/11'</td>
        <td class="tg-0pky">103</td>
        <td class="tg-0pky">147</td>
        <td class="tg-0pky">329.3</td>
      </tr>
      <tr>
        <td class="tg-0pky">11</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/12'</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">120</td>
        <td class="tg-0pky">250.7</td>
      </tr>
      <tr>
        <td class="tg-0pky">12</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/12'</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">120</td>
        <td class="tg-0pky">250.7</td>
      </tr>
      <tr>
        <td class="tg-0pky">13</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/13'</td>
        <td class="tg-0pky">106</td>
        <td class="tg-0pky">128</td>
        <td class="tg-0pky">345.3</td>
      </tr>
      <tr>
        <td class="tg-0pky">14</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/14'</td>
        <td class="tg-0pky">104</td>
        <td class="tg-0pky">132</td>
        <td class="tg-0pky">379.3</td>
      </tr>
      <tr>
        <td class="tg-0pky">15</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/15'</td>
        <td class="tg-0pky">98</td>
        <td class="tg-0pky">123</td>
        <td class="tg-0pky">275.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">16</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/16'</td>
        <td class="tg-0pky">98</td>
        <td class="tg-0pky">120</td>
        <td class="tg-0pky">215.2</td>
      </tr>
      <tr>
        <td class="tg-0pky">17</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/17'</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">120</td>
        <td class="tg-0pky">300.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">18</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">'2020/12/18'</td>
        <td class="tg-0pky">90</td>
        <td class="tg-0pky">112</td>
        <td class="tg-0pky">NaN</td>
      </tr>
      <tr>
        <td class="tg-0pky">19</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/19'</td>
        <td class="tg-0pky">103</td>
        <td class="tg-0pky">123</td>
        <td class="tg-0pky">323.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">20</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">'2020/12/20'</td>
        <td class="tg-0pky">97</td>
        <td class="tg-0pky">125</td>
        <td class="tg-0pky">243.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">21</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/21'</td>
        <td class="tg-0pky">108</td>
        <td class="tg-0pky">131</td>
        <td class="tg-0pky">364.2</td>
      </tr>
      <tr>
        <td class="tg-0pky">22</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">NaN</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">119</td>
        <td class="tg-0pky">282.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">23</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/23'</td>
        <td class="tg-0pky">130</td>
        <td class="tg-0pky">101</td>
        <td class="tg-0pky">300.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">24</td>
        <td class="tg-0pky">45</td>
        <td class="tg-0pky">'2020/12/24'</td>
        <td class="tg-0pky">105</td>
        <td class="tg-0pky">132</td>
        <td class="tg-0pky">246.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">25</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/25'</td>
        <td class="tg-0pky">102</td>
        <td class="tg-0pky">126</td>
        <td class="tg-0pky">334.5</td>
      </tr>
      <tr>
        <td class="tg-0pky">26</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">20201226</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">120</td>
        <td class="tg-0pky">250.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">27</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/27'</td>
        <td class="tg-0pky">92</td>
        <td class="tg-0pky">118</td>
        <td class="tg-0pky">241.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">28</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/28'</td>
        <td class="tg-0pky">103</td>
        <td class="tg-0pky">132</td>
        <td class="tg-0pky">NaN</td>
      </tr>
      <tr>
        <td class="tg-0pky">29</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/29'</td>
        <td class="tg-0pky">100</td>
        <td class="tg-0pky">132</td>
        <td class="tg-0pky">280.0</td>
      </tr>
      <tr>
        <td class="tg-0pky">30</td>
        <td class="tg-0pky">60</td>
        <td class="tg-0pky">'2020/12/30'</td>
        <td class="tg-0pky">102</td>
        <td class="tg-0pky">129</td>
        <td class="tg-0pky">380.3</td>
      </tr>
      <tr>
        <td class="tg-0lax">31</td>
        <td class="tg-0lax">60</td>
        <td class="tg-0lax">'2020/12/31'</td>
        <td class="tg-0lax">92</td>
        <td class="tg-0lax">115</td>
        <td class="tg-0lax">243.0</td>
      </tr>
    </tbody>
  </table>
</details>

> The data set contains 
> - some empty cells ("Date" in row 22, and "Calories" in row 18 and 28).
> - wrong format ("Date" in row 26).
> - wrong data ("Duration" in row 7).
> - duplicates (row 11 and 12).

## Clean Empty Cells

Empty cells can potentially give you a wrong result when you analyze data. **By default, the `dropna()` method returns a _new_ DataFrame, and will not change the original.**
> If you want to change the original DataFrame, use the `inplace = True` argument.

```python
import pandas as pd  

df = pd.read_csv('data.csv')  
# New DF
new_df = df.dropna()  
print(new_df.to_string())
# Update old DF
df.dropna(inplace = True)
print(df.to_string())
```

### Replacing Empty Values 

Another way of dealing with empty cells is to insert a _new_ value instead. This way you do not have to delete entire rows just because of some empty cells. The `fillna()` method allows us to replace **all** the empty cells with a value:

```python
import pandas as pd  

df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
```

As the replacement could be a number, there´s a possibility to use the `mean()` `median()` and `mode()` methods to calculate the respective values.
- **Mean** = the average value (the sum of all values divided by number of values).
- **Median** = the value in the middle, after you have sorted all values ascending.
- **Mode** = the value that appears most frequently.

Or replace **only** in a defined column, ypu'll need to specify the _column name_ for the DataFrame:

```python
import pandas as pd 

df = pd.read_csv('data.csv')
df["Calories"].fillna(130, inplace = True)
```

Other way is to set the format of the columns to the same, e.g. in the row `22` in the given data, the date info isn't matching with the others, so we can use the [`to_datetime(_arg_, _errors='raise'_, _dayfirst=False_, _yearfirst=False_, _utc=False_, _format=None_, _exact=_NoDefault.no_default_, _unit=None_, _infer_datetime_format=_NoDefault.no_default_, _origin='unix'_, _cache=True_)`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) (*condensed info, for more see the full doc.*) method, as below:

```python
import pandas as pd  

df = pd.read_csv('data.csv')  
df['Date'] = pd.to_datetime(df['Date'])  
#print
print(df.to_string())
```

> The result is `26        60  '2020/12/26'    100       120     250.0`

**Parameters**
- **arg** (*`int`, `float`, `str`, `datetime`, `list`, `tuple`, `1-d array`, `Series`, `DataFrame`/`dict-like`*)
- **errors** (*{‘ignore’, ‘raise’, ‘coerce’}, **default** ‘raise’*)
- **dayfirst** (*`bool`, **default** False*)
- **yearfirst** (*`bool`, **default** False*)
- **utc** (*`bool`, **default** False*)
- **format** (*`str`, **default** None*)
- **exact** (*`bool`, **default** True*)
- **unit** (*`str`, **default** ‘ns’*)
- **infer_datetime_format** (*`bool`, **default** False*)

**Returns**
- datetime, If parsing succeeded. Return type depends on input :
	-   scalar: [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
	-   array-like: [`DatetimeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.DatetimeIndex.html#pandas.DatetimeIndex "pandas.DatetimeIndex")
	-   Series: [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") of `datetime64` dtype
	-   DataFrame: [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series") of `datetime64` dtype

**Raises**
- **ParserError**, When parsing a date from string fails.
- **ValueError**, When another datetime conversion error happens. For example when one of ‘year’, ‘month’, day’ columns is missing in a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame"), or when a Timezone-aware [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.11)") is found in an array-like of mixed time offsets, and `utc=False`.

### Remove Wrong Data

In the example the line wasn't in the right format, but in the line `22` the value stored in Date was Nota a Number (`NaN`) before and now is Not a Time (`NaT`) and can be handled as a NULL value, and we can remove the row by using the [`dropna(_*_, _axis=0_, _how=_NoDefault.no_default_, _thresh=_NoDefault.no_default_, _subset=None_, _inplace=False_, _ignore_index=False_)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html) method (*condensed info, for more see the full doc.*) .

```python
df.dropna(subset=['Date'], inplace = True)
```

**Parameters**
- **axis** ({`0` or `index`, `1` or `columns`}, **default** 0), Determine if rows or columns which contain missing values are removed.
- **how** ({`any`, `all`}, **default** `any`), Determine if row or column is removed from DataFrame, when we have at least one `NA` or all.
- **thresh** (`int`, **optional**), Require that many non-NA values. Cannot be combined with how.
- **subset** (column label or sequence of labels, **optional**), Labels along other axis to consider, e.g. if you are dropping rows these would be a list of columns to include.
- **inplace** (`bool`, **default** False), Whether to modify the DataFrame rather than creating a new one.
- **ignore_index** (`bool`, **default** `False`), If `True`, the resulting axis will be labeled 0, 1, …, n - 1.

**Returns**
- DataFrame or None
- DataFrame with `NA` entries dropped from it or None if `inplace=True`.

## Remove Duplicates

By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
To discover duplicates, we can use the [`duplicated(_subset=None_, _keep='first'_)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html) method. 

```python
print(df.duplicated())
```

**Parameters**
- **subset**: *column label or sequence of labels, optional*, only consider certain columns for identifying duplicates, by default use all of the columns.
- **keep**: *{‘first’, ‘last’, False}, **default** ‘first’*, determines which duplicates (if any) to mark.

The `duplicated()` method returns a Boolean Series: `True` for every row that is a duplicate, otherwise `False`.

**To remove duplicates**, use the [`drop_duplicates(_subset=None_, _*_, _keep='first'_, _inplace=False_, _ignore_index=False_)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) method. 

```python
df.drop_duplicates(inplace = True)
```

**Parameters**
- **subset**: *column label or sequence of labels, **optional***, only consider certain columns for identifying duplicates, by default use all of the columns.
- **keep**: *{‘first’, ‘last’, `False`}, **default** ‘first’*, determines which duplicates (if any) to keep.
- **inplace**: *`bool`, **default** `False`*, whether to modify the DataFrame rather than creating a new one.
- **ignore_index**: *`bool`, **default** `False`*, if `True`, the resulting axis will be labeled 0, 1, …, n - 1.

The method returns a DataFrame with duplicates removed or None if `inplace=True`.

# Advanced

## Correlations
> The examples (from W3schools) uses a CSV file called: '[data.csv](https://www.w3schools.com/python/pandas/data.csv.txt)'.

### Finding Relationships

A great aspect of the Pandas module is the `corr()` method.
The [`corr(_method='pearson'_, _min_periods=1_, _numeric_only=False_)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html) method calculates the relationship between each column in your data set and **returns a Correlation matrix.**

**Parameters**
- **method**: *{‘pearson’, ‘kendall’, ‘spearman’} or callable*
- **min_periods**: *`int`, **optional***, minimum number of observations required per pair of columns to have a valid result. Currently only available for Pearson and Spearman correlation.
- **numeric_only**: *`bool`, **default** False*, include only float, int or boolean data.

```python
df.corr()

 #           Duration     Pulse  Maxpulse  Calories
 # Duration  1.000000 -0.155408  0.009403  0.922721
 # Pulse    -0.155408  1.000000  0.786535  0.025120
 # Maxpulse  0.009403  0.786535  1.000000  0.203814
 # Calories  0.922721  0.025120  0.203814  1.000000
```
> *The `corr()` method ignores "not numeric" columns.*

The result  is a table with numbers (**from -1 to 1**) that represents how well the relationship is between two columns. 

- `1` means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.
- `0.9` is also a good relationship, and if you increase one value, the other will probably increase as well. 
- `-0.9` would be just as good relationship as 0.9, but if you increase one value, the other will probably go down. 
- `0.2` means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

> **What is a good correlation?** It depends on the use, but I think it is safe to say you have to have at least `0.6` (or `-0.6`) to call it a good correlation.

### Perfect Correlation:

We can see that "Duration" and "Duration" got the number `1.000000`, which makes sense, each column always has a perfect relationship with itself.

### Good Correlation:

"Duration" and "Calories" got a `0.922721` correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out.

### Bad Correlation:

"Duration" and "Maxpulse" got a `0.009403` correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa.

## Plotting
> The examples uses a CSV file called: '[data.csv](https://www.w3schools.com/python/pandas/data.csv.txt)'.

![plot|500](https://www.w3schools.com/python/pandas/img_pandas_plot.png)


Pandas uses the [`plot(_*args_, _**kwargs_)`]() method to create diagrams. We can use **Pyplot**, a submodule of the **Matplotlib** library to visualize the diagram on the screen.
> Read more about in [Matplotlib Tutorial](https://www.w3schools.com/python/matplotlib_intro.asp).

**Parameters**
- **data**: `Series` or `DataFrame`, the object for which the method is called.
- there's a lot of parameters...

```python
import pandas as pd  
import matplotlib.pyplot as plt  
  
df = pd.read_csv('data.csv')
df.plot()  
plt.show()
```


### Scatter Plot

Specify that you want a scatter plot with the `kind` argument:

`kind = 'scatter'`

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this:

`x = 'Duration', y = 'Calories'`

```python
import pandas as pd  
import matplotlib.pyplot as plt  
  
df = pd.read\_csv('data.csv')  
  
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')  
  
plt.show()
```

![scatter|500](https://www.w3schools.com/python/pandas/img_pandas_plot_scatter.png)
> **Remember:** In the previous example, we learned that the correlation between "Duration" and "Calories" was `0.922721`, and we concluded with the fact that higher duration means more calories burned.

### Histogram

Use the `kind` argument to specify that you want a histogram:

`kind = 'hist'`

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

In the example below we will use the "Duration" column to create the histogram:

```python
df["Duration"].plot(kind = 'hist')
```

![histogram|500](https://www.w3schools.com/python/pandas/img_pandas_plot_hist.png)
> **Note:** The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.
---

# References

- [pydata](https://pandas.pydata.org/)
- [w3schools](https://www.w3schools.com/python/pandas/default.asp)