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