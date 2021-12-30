---
aliases: seaborn, data, matplotlib, data visualisation
tags: #seaborn, #data, #matplotlib
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Visualization
Seaborn works on top of Matplotlib and you will need to import both packages in most of the cases.
Reference:
-   [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
-   [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
```
Import the dataset to work with
```py
file_url = 'https://www.dropbox.com/s/jz8ck0obu9u1rng/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv?raw=1'
df = pd.read_csv(file_url)
```
## Categories of Plots
![[Pasted image 20211230102250.png]]
## Histogram and Boxplot
One of the first thing we may want to do in understanding the data is to see its distribution and its descriptive statistics.
We can use `histplot` to show the histogram of the data and `boxplot` to show the five-number summary of the data.

### Histplot
```py
#Check what are the towns listed
np.unique(df['town'])
#Get data for Tampines only
df_tampines = df.loc[df['town'] == 'TAMPINES',:]

# Plot resale price distribution
sns.histplot(x='resale_price', data=df_tampines)
```
![[Pasted image 20211230104419.png]]
We can change the plot if we want to show it vertically.
```py
sns.set()
sns.histplot(y='resale_price', data=df_tampines)
```
![[Pasted image 20211230104504.png]]
**Notice that the background changes**. This is because we have called `sns.set()` which set Seaborn default setting instead of using Matplotlib's setting. For example, Matplotlib uses whitebackground and no grid. Seaborn by default displays some white grid on gray background.

By default, the `bins` argument is `auto` and Seaborn will try to calculate how many bins should be used. But we can specify this manually.
```py
sns.histplot(y='resale_price', data=df_tampines, bins=10)
```

### Boxplot
We can also use the `boxplot` to see some descriptive statistics of the data.
See [documentation on boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html)
```py
sns.boxplot(x='resale_price', data=df_tampines)
```
![[Pasted image 20211230113256.png]]
See [Understanding Boxplot](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51) for more detail. But the figure in that website summarizes the different information given in a boxplot.
![[Pasted image 20211230113314.png]]
The box gives you the 25th percentile and the 75th percentile boundary. The line inside the box gives you the median of the data. As we can see the median is about $400k to $500k. The difference between the 75th percentile (Q3) and the 25th percentile (Q1) is called the _Interquartile Range_ (IQR). This definition is needed to understand what defines **outliers**. The minimum and the maximum here is not the minimum and the maximum value in the data, but rather is capped at
$$
\begin{align}
min&=Q1−1.5 \times IQR \\ 
max&=Q3+1.5 \times IQR
\end{align}
$$
Anything below or above these "minimum" and "maximum" are considered an outlier in the box plot. In the figure above, for example, we have quite a number of outliers on the high end of the resale price.
## Modifying Labels and Titles
We can use some of Matplotlib functions to change the figure's labels and title. For example, we can change the histogram's plot x and y labels and its titles using `plt.xlabel()`, `plt.ylabel()`, and `plt.title`. You can access these Matplotlib's functions by first storing the output of your Seaborn plot.
```py
myplot = sns.histplot(y='resale_price', data=df_tampines, bins=10)
```
![[Pasted image 20211230120709.png]]
Once you obtain the handle, you can call Matplotlib's function by adding the word `set_` in front of it. For example, if the Matplotlib's function is `plt.xlabel()`, you call it as `myplot.set_xlabel()`.
```py
myplot = sns.histplot(y='resale_price', data=df_tampines, bins=10)
myplot.set_xlabel('Count', fontsize=16)
myplot.set_ylabel('Resale Price', fontsize=16)
myplot.set_title('HDB Resale Price in Tampines', fontsize=16)
```
![[Pasted image 20211230122237.png]]
## Using Hue
Seaborn has an argument called `hue` to specify which data column you want to use to colour this.
```py
myplot = sns.histplot(y='resale_price_1000', hue='flat_type', data=df_tampines, bins=10)
myplot.set_xlabel('Count', fontsize=16)
myplot.set_ylabel('Resale Price in $1000', fontsize=16)
myplot.set_title('HDB Resale Price in Tampines', fontsize=16)
```
![[Pasted image 20211230122324.png]]
```py
myplot = sns.histplot(y='resale_price_1000', hue='storey_range', data=df_tampines, bins=10)
myplot.set_xlabel('Count', fontsize=16)
myplot.set_ylabel('Resale Price in $1000', fontsize=16)
myplot.set_title('HDB Resale Price in Tampines', fontsize=16)
```
![[Pasted image 20211230122352.png]]
The above colouring is not so obvious because they are on top of one another, one way is to change the settings in such a way that it is stacked. We can do this by setting the `multiple` argument for the case when there are multiple data in the same area.
```py
myplot = sns.histplot(y='resale_price_1000', hue='storey_range', 
                      multiple='stack',
                      data=df_tampines, bins=10)
myplot.set_xlabel('Count', fontsize=16)
myplot.set_ylabel('Resale Price in $1000', fontsize=16)
myplot.set_title('HDB Resale Price in Tampines', fontsize=16)
```
![[Pasted image 20211230125417.png]]
## Scatter Plot and Line Plot
We use scatter plot and line plot to visualize relationship between two or more data.
```py
myplot = sns.scatterplot(x='floor_area_sqm', y='resale_price_1000', data=df_tampines)
myplot.set_xlabel('Floor Area ($m^2$)')
myplot.set_ylabel('Resale Price in $1000')
```
![[Pasted image 20211230125452.png]]
You can again use the `hue` argument to see any category in the plot.
```py
myplot = sns.scatterplot(x='floor_area_sqm', y='resale_price_1000', 
                         hue='flat_type',
                         data=df_tampines)
myplot.set_xlabel('Floor Area ($m^2$)')
myplot.set_ylabel('Resale Price in $1000')
```
![[Pasted image 20211230125516.png]]
## Pair Plot
One useful plot is called Pair Plot in Seaborn where it plots the relationship on multiple data columns.
```py
myplot = sns.pairplot(data=df_tampines)
```
![[Pasted image 20211230125550.png]]
The above plots immediately plot different scatter plots and histogram in a matrix form. The diagonal of the plot shows the histogram of that column data. The rest of the cell shows you the scatter plot of two columns in the data frame. From these, we can quickly see the relationship between different columns in the data frame.