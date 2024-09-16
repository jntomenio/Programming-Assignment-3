[![Up to Date](https://github.com/ikatyang/emoji-cheat-sheet/workflows/Up%20to%20Date/badge.svg)](https://github.com/ikatyang/emoji-cheat-sheet/actions?query=workflow%3A%22Up+to+Date%22)

<!-- ![Build Status](https://travis-ci.org/yourusername/yourproject.svg?branch=main) -->

# :bookmark_tabs: PA3 - PYTHON DATA ANALYSIS (*PANDAS*)

> [!NOTE]
> :open_book: *Python Data Analysis (Pandas)* - core Python library that provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
> ###### :heavy_check_mark: Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet.
> ###### :heavy_check_mark: Ordered and unordered (not necessarily fixed-frequency) time series data.
> ###### :heavy_check_mark: Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels.
> ###### :heavy_check_mark: Any other form of observational/statistical data sets.

## 📖 Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

 ### :bookmark: Types of Pandas Data Structure:
- **Data Series** - is a one-dimensional labeled array capable of holding any data type. 
- **Data Frames** - two-dimensional labeled data structure with columns of different data types.

### :bulb: How to save a Python file?
**1.** You can download a copy of the python as a `.py` script from `FILE` menu in the upper left corner.
![image](https://github.com/user-attachments/assets/6b0e27db-bffc-4eef-b09d-03d9acd30c4c)

**2.** To save the existing python notebook as python file **using python command code**. Introducing one of the *Python File Modes*:
- **Write Mode ('w')**: Overwrites existing content or creates a new file.
  - When you open a file in write mode, you are indicating that you want to write data to the file.
  - If the file already exists, it will be truncated (i.e., all existing content will be deleted) before writing new date.
  - If the file does not exist, a new file will be created.
> [!NOTE]
> :bangbang: used this at the bottommost of your code. 
```python

# Define the code to be saved as a string
ipnyb_to_py = """

CODE CONTENT - copy all the code inputs from your notebook/file

"""

# Specify the filename you want
filename = 'Surname_Pandas-P1.py'

# Open the file in write mode and save the code
with open(filename, 'w') as file:
    file.write(ipnyb_to_py)
```

> [!IMPORTANT]
> :file_folder: Save this DataFrame to your default user folder by downloading this [link](http://bit.ly/Cars_file).
> - ###### This file folder (***cars.csv***) will be used for both Python problems.[^1]

[^1]: http://bit.ly/Cars_file 
---

### Python Demo 1: *Problem 1*
- In this demonstration, we will display the first five and last five rows of the resulting cars using the Pandas DataFrame Methods.
- :floppy_disk: Save your file as `Surname_Pandas-P1.py`

#### :mag_right: *The head() Method*
- it returns a specified number of rows, *string from the top*.
- if a number is not specified, it returns the first five rows.

#### :mag_right: *The tail() Method*
- this method returns a specified number of *last rows*. 
- if a number is not specified, it returns the last 5 rows.

### CODE IMPLEMENTATION
##### :keyboard: *Input:*
```python
import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')
cars
```
##### :computer: *Output:*
- To display the **first five rows** of DataFrame, use the *head()* method.
``` python
print("First five rows:")
cars.head()
```

- To display the **last five rows** of DataFrame, use the *tail()* method.
``` python
print("Last five rows:")
cars.tail()
```

---
### Python Demo 2: *Problem 2*
- In this demonstration, using the DataFrame cars in problem 1, extract the following information using *subsetting*, *slicing*, and *indexing* operations.
- :floppy_disk: Save your file as `Surname_Pandas-P2.py`

> [!NOTE]
> `.loc[]` allows you to select rows and columns by their labels (i.e., the names of the index and columns).
>
> `.iloc[]` - This is a pandas method used for integer-location based indexing. It allows you to select rows and columns by their integer positions.
>
> `:` - The first colon indicates that you want to select all rows from the DataFrame.
>
> `::2` - This slice notation selects every second column from the DataFrame, starting from the first column (index 0). The `2` indicates the step size, meaning it will skip every other column.

#### :mag_right: *Subsetting*
- In data analytics, the term subsetting means getting a ***certain element (1)*** in a data structure, in our case the DataFrame, by using the data structure's index.

 #### :mag_right: *Slicing*
- getting a portion of your data structure by specifying a ***certain range***.

 #### :mag_right: *Indexing*
- similar to subsetting but using a ***certain conditional expression*** as its index.


### CODE IMPLEMENTATION
##### :keyboard: *Input:*
``` python
import pandas as pd

# Load the CSV file into a DataFrame
cars = pd.read_csv('cars.csv')
cars
```

##### :computer: *Output:*
**A.** Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars. This process is form of `slicng`.
``` python
# Selects all rows and odd-numbered columns
cars.iloc[:5,1::2]
# Print
row
```

- Display the row that contains the ‘Model’ of ‘Mazda RX4’. This output is a process of `indexing`.
``` python
# Filter the DataFrame 'cars' to find rows where the 'Model' column matches 'Mazda RX4'
cars.loc[cars['Model'] == 'Mazda RX4']
```

- How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have. This output is a process of `indexing`.
``` python
# Filter the 'cars' DataFrame to select rows where the 'Model' column is equal to 'Camaro Z28'
# and return only the 'Model' and 'cyl' columns for those rows
cars.loc[cars['Model'] == 'Camaro Z28',['Model','cyl']]
```

- Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have. This process is a form `indexing`.
``` python
# Filter the DataFrame 'cars' to include only specific car models
cars.loc[
    (cars['Model'] == 'Mazda RX4 Wag') | 
    (cars['Model'] == 'Ford Pantera L') | 
    (cars['Model'] == 'Honda Civic')
# Return the 'cyl' and 'gear' columns for the filtered rows
] [['Model', 'cyl', 'gear']]
```


## Author
Julian Bernice Kristoffer Tomenio
- @jntomenio — https://github.com/jntomenio


## 🔑 Version History
- 1.03
  - Amended and completed the ReadMe file.

- 1.02
  - Added the ReadMe file.

- 1.01
  - Added the supplemental files

- 1.00 
  - Repository has been established
