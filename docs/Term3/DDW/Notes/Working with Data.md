---
aliases: pandas, data
tags: #pandas, #data, #ML
---
Back to [[Data Driven World|DDW]]
# Working with Data
## Short Introduction to Machine Learning
We will look into how computation can learn from data in order to make a new computation.
This new computation is often called a **prediction**.
We focus on what is called as **supervised machine learning**.
The word supervised machine learning indicates that the computer learns from some existing data on how to compute the prediction.
Supervised machine learning assumes that we have some existing data that is **labelled**.
Using this labelled data (supervised), the computer can predict the category given some new data.
## Reading Data
One common source is a text file in the form of CSV format (comma separated value). Another common format is Excel spreadsheet. The data can be from some databases or some server. Different data sources will require different ways of handling it. But in all those cases we will need to know how to read those data.
For this purpose we will use [Pandas](https://pandas.pydata.org/) library to read our data. We import the data into our Python code by typing the following code.
```py
import pandas as pd
```
Now we can use Pandas functions to read the data. For example, if we want to read a CSV file, we can simply type:
```py
df = pd.read_csv('mydata.csv')
```
The output of `read_csv()` function is in Pandas' `DataFrame` type.
```py
type(df)
```
> pandas.core.frame.DataFrame

`DataFrame` is Pandas' class that contains attributes and methods to work with a tabular data as shown above.
Recall that we can create our own custom data type using the keyword `class` and define its attributes and methods.
We can even override some of Python operators to work with our new data type. This is what Pandas library does with `DataFrame`.
This `DataFrame` class provides some properties and methods that allows us to work with tabular data.

For example, we can get all the name of the columns in our data frame using `df.columns` properties.
We can also get the index (the names on the rows) using `df.index`.
We can also treat this data frame as a kind of matrix to find its shape using `df.shape`.

What we want to predict is called the **target**.
The others are called **features**.

The idea supervised machine learning is that using the given data such as shown above, the computer would like to predict what is the _target_ give a new set of _features_. The computer does this by _learning_ the existing labelled data.

In order to understand the data, it is important to be able to manipulate and work on the data frame.
## Data Frame Operations
Pandas has two data structures:

-   [Series](https://pandas.pydata.org/docs/user_guide/dsintro.html#series)
-   [DataFrame](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)

You can consider `Series` data as one-dimensional labelled array while `DataFrame` data as two-dimensional labelled data structure.
### Getting Rows and Columns as Series
You can access the column data as series using the square bracket operator.
```py
df[column_name]
```
```py
print(df['resale_price'])
print(type(df['resale_price']))
```
> 0        232000.0
1        250000.0
2        262000.0
3        265000.0
4        265000.0
...
95853    650000.0
95854    645000.0
95855    585000.0
95856    675000.0
95857    625000.0
Name: resale_price, Length: 95858, dtype: float64
<class 'pandas.core.series.Series'>

You can also get some particular row by specifying its `index`.
You can also access the column using the `.loc[index, column]` method. In this method, you need to specify the labels of the index.
For example, to access all the rows for a particular column called `resale_price`, we can do as follows. Notice that we use `:` to access all the rows. Moreover, we specify the name of the columns in the code below.
```py
print(df.loc[:, 'resale_price'])
print(type(df.loc[:, 'resale_price']))
```
> 0        232000.0
1        250000.0
2        262000.0
3        265000.0
4        265000.0
...   
95853    650000.0
95854    645000.0
95855    585000.0
95856    675000.0
95857    625000.0
Name: resale_price, Length: 95858, dtype: float64
<class 'pandas.core.series.Series'>

In the above code, we set the index to access all rows by using `:`. Recall that in Python's list slicing, we also use `:` to access all the element. Similarly here, we use `:` to access all the rows. In a similar way, we can use `:` to access all the columns, e.g. `df.loc[:, :]` will copy the whole data frame.

Recall that all these data are of the type `Series`. You can create a Data Frame from an existing series just like when you create any other object by instantiating a `DataFrame` object and passing on an argument as shown below.
```py
df_row0 = pd.DataFrame(df.loc[0, :])
df_row0
```
![[Pasted image 20211228155430.png]]
### Getting Rows and Columns as DataFrame
The operator `:` works similar to Python's slicing. This means that you can get some rows by slicing them. For example, you can access the first 10 rows as follows.
```py
print(df.loc[0:10, :])
print(type(df.loc[0:10, :]))
```
Notice, however, that the slicing in Pandas' data frame is **inclusive** of the ending index unlike Python's slicing.
The other thing to note about is that the output data type is no longer a series but rather a `DataFrame`. The reason is that now the data is two-dimensionsional.
You can specify both the rows and the columns you want as shown below.
```py
df.loc[0:10,'month':'remaining_lease']
```
The index is not always necessarily be an integer. Pandas can take strings as the index of a data frame. But there are times, even when the index is not an integer, we still prefer to locate using the position of the rows to select. In this case, we can use `.iloc[position_index, position_column]`.
```py
columns = [1, 3, -1]
df.iloc[0:10, columns]
```
### Selecting Data Using Conditions
We can use conditions with Pandas' data frame to select particular rows and columns using either `.loc[]` or `.iloc[]`. The reason is that these methods can take in boolean arrays.
Let's say we want to see those sales where the price is greater than $500k. We can put in this condition in filtering the rows.
```py
df.loc[df['resale_price'] > 500_000, columns]
```
Note: Python ignores the underscores in between numeric literals and you can use it to make it easier to read.

We can use the AND operator `&` to have more than one conditions.
```py
df.loc[(df['resale_price'] >= 500_000) & (df['resale_price'] <= 600_000), columns]
```
**Note: the parenthesis separating the two AND conditions are compulsory.**
## Series and DataFrame Functions
### Creating DataFrame and Series
We can create a new DataFrame from other data type such as dictionary, list-like objects, or Series. For example, given a `Series`, you can convert into a `DataFrame` as shown below.
```py
price = df['resale_price'] #this is a series
price_df = pd.DataFrame(price) #this is now a dataframe
```
Similarly, you can convert other data to a `Series` by using its contructor. In the example below, we create a new series from a list of integers from 2 to 100.
```py
new_series = pd.Series(list(range(2,101)))
```
### Copying
One useful function is to copy a data frame to another dataframe. We can use `df.copy()`.
This function has an argument `deep` which by default is `True`. If it is true, it will do a deep copy of the Data Frame. Otherwise, it will just do a shallow copy. See [documention](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html).
```py
df2 = df.copy()
```
### Statistical Functions
We can get some descriptive statistics about the data using some of Pandas functions. For example, we can get the five point summary using `.describe()` method.
```py
df.describe()
```
![[Pasted image 20211228195600.png]]
 Pandas will only try to get the statistics of the columns that contain numeric numbers. We can also get the individual statistical functions as shown below.
```py
print(df['resale_price'].mean())
print(df['resale_price'].std())
print(df['resale_price'].min())
print(df['resale_price'].max())
print(df['resale_price'].quantile(q=0.75))
```
You can change the way the statistics is computed. Currently, the statistics is calculated over all the rows in the vertical dimension.
This is what is considered as `axis=0` in Pandas.
You can change it to compute over all the columns by specifying `axis=1`.
```py
df.mean(axis=1)
```
### Transposing Data Frame
You can also change the rows into the column and the column into the rows.
You can transpose the data using the `.T` property.
```py
df_row0_transposed = df_row0.T
```
### Vector Operations
One useful function in Pandas is `.apply()` (see [documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)) where we can apply some function to all the data in the column or row or Series in a vectorized manner.
In this way, we need not iterate or loop the data one at a time to apply this computation.
```py
def divide_by_1000(data):
    return data / 1000

df['resale_price_in1000'] = df['resale_price'].apply(divide_by_1000)
```
The method `.apply()` takes in a function that will be processed for every data in that Series. Instead of creating a named function, we can make use of Python's lambda function to do the same.
```py
df['resale_price_in1000'] = df['resale_price'].apply(lambda data: data/1000)
```
Notice that the argument in `divide_by_1000()` becomes the first token after the keyword `lambda`. The return value of the function is provided after the colon, i.e. `:`.

You can use this to process and create any other kind of data. For example, we can create a new categorical column called "Pricey" and set any sales above $500k is considered as pricey otherwise is not. If it is pricey, we will label it as 1, otherwise, as 0.
```py
df['pricey'] = df['resale_price_in1000'].apply(lambda price: 1 if price > 500 else 0 )
```
We use the if _expression_ to specify the return value for the lambda function. It follows the following format:
```py
expression_if_true if condition else expression_if_false
```
There are many other Pandas functions and methods. It is recommended that you look into the documentation for further references.
## References
-   [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
-   [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
## Normalization
 Each column in the dataset may have different scales, so we need to normalise the data, both features and the target.
 We usually need to normalize the data before doing any training for our machine learning model.
 There are two common normalization types:
-   z normalization
-   minmax normalization
### Z Normalization
Move the mean of the data distribution to 0 and its standard deviation to 1.
$$\hat{x} = \dfrac{x - \mu}{\sigma}$$
### Min-Max Normalization
Scale the data in such a way that the maximum value in the distribution is 1 and its minimum value is 0.
$$\hat{x} = \dfrac{x - min}{max - min}$$
## Splitting Dataset
One common pre-processing operations that we normally do in machine learning is to split the data into:
-   **training** dataset
-   **test** dataset

The idea of splitting the dataset is simply because we should **NOT** use the same data to verify the model which we train.
If we only have one dataset, we cannot use the same data to verify the accuracy with the ones we use to train the model. This bias would obviously create high accuracy.
To overcome this, we should split the data into two. One set is used to train the model while the other one is used to verify the model.
One important note is that the split must be done **randomly**. This is to avoid systematic bias in the split of the dataset.
There are times in machine learning, we need to experiment with different parameters and find the optimum parameters. In these cases, the dataset is usually split into three:
-   **training** dataset, which is used to build the model
-   **validation** dataset, which is used to evaluate the model for various parameters and to choose the optimum parameter
-   **test** dataset, which is used to evaluate the model built with the optimum parameter found previously