---
aliases: categorical regression
tags: #regression, #data, #ML
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Logistic Regression for Classification
## Introduction
The problem of classification deals with _categorical_ data.
In this problem, we wish to identify a set of data whether they belong to a particular class of category.
In this section we will learn logistic regression to solve this classification problem.
## Hypothesis Function
We need a function where we can model the data in a step wise manners and fulfills the following:
$$0≤p(x)≤1$$
where $p(x)$ is the probability that a data point with feature $x$ is a certain category.

One of the function that we can use that have this step-wize shape and the above properties is a logistic function. A logistic function can be written as.
$$y=\dfrac{1}{1+e^{-z}}$$
which looks like 
![[Pasted image 20211230203005.png]]
So we can write our hypothesis as:
$$p(x)=\dfrac{1}{1+e^{-z(x)}}$$
where $z$ is a function of $x$.
What is this $z(x)$ function?
We can use our linear model of a straight line and transform it into a logistic function if we use the following transformation:
$$z(x) = \beta_0x_0 + \beta_1x_1$$
where if $x_0 = 1$, then this is simply [[Linear Regression|simple linear regression]].

This is the case with only one feature.
If we have more than one feature,
$$z(x)=\beta_0x_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n$$
Note that in this notes we tend to omit the _hat_ symbol to indicate it is the estimated parameters as in the previous notes. We will just indicate the estimated parameters as $\beta$ instead of $\hat{\beta}$.

The above relationship shows that we can map the value of linear regression into a new function with a value from $0$ to $1$. This new function $p(x$)$ can be considered as _an estimated probability_ that $y=1$ on input $x$.

We can then use the following boundary conditions:
-  $y = 1$  if $p(x)≥0.5$
-   $y = 0$ if $p(x)<0.5$

The above conditions also means that we can classify $y=1$ when $\beta^Tx≥0$ and $y=0$ when $\beta^Tx<0$. We can draw these boundary conditions.
![[Pasted image 20211231095820.png]]
Aim is to find the value of the parameters, same as before.
$\beta^Tx=0$ can be written as $\beta_0+\beta_1x = 0$.
## Cost Function
We will have to minimize some cost function using optimization algorithm.
For logistic regression, we will choose the following cost function.
$$J(\beta) = \dfrac{1}{m}
\sum^m_{i=1}
\begin{cases}
\begin{align}
&-\log{(p(x))} &\text{if }y=1\\
&-\log{(1-p(x))} &\text{if }y=0
\end{align}
\end{cases}
$$
We can write the overall cost function for all the data points from $i=1$ to $m$ as follows.
$$J(\beta) = -\dfrac{1}{m}
\left[
\sum^m_{i=1}
y^i
\log{(p(x^i))}
+(1-y^i)\log{(1-p(x^i))}
\right]
$$
Notice how the function is reduced when $y^i$ is 1 or 0.
## Gradient Descent
We need the gradient descent algorithm to perform $min_\beta J(\beta)$.
The update functions for the parameters are given by $\beta_j = \beta_j - \alpha \dfrac{\delta}{\delta\beta_j}J(\beta)$.
The derivative of the cost function is given by $\dfrac{\delta}{\delta\beta_j}J(\beta)= \dfrac{1}{m}\sum^m_{i=1}\left(p(x)-y^i\right)x_j^i$ 
[[#Derivation of Logistic Regression Derivative|Refer to this for derivation.]]
Now substitute this in to get the update function:
$$\beta_j = \beta_j - \alpha\dfrac{1}{m}\sum^m_{i=1}\left(p(x)-y^i\right)x_j^i$$
## Matrix Notation
The above equations can be written in matrix notation so that we can perform a vectorized computation.
### Hypothesis Function
[[#Hypothesis Function|Recall]]
$p(x)=\dfrac{1}{1+e^{-z(x)}}$ where $z(x)=\beta_0x_0 + \beta_1x_1 + \beta_2x_2 + \dots + \beta_nx_n$.
Rewriting as vector multiplication, $z=b^Tx$
So $p(x)=\dfrac{1}{1+e^{-b^Tx}}$, where $b=\begin{bmatrix}\hat{\beta_0}\\\hat{\beta_1}\\\vdots\\\hat{\beta_n}\\\end{bmatrix}$ and $x=\begin{bmatrix}1\\x_1\\x_2\\\vdots\\x_n\\\end{bmatrix}$.
Recall that this is for a single data with $n$ features. The result of this vector multiplication $z$ is a single number for that one single data with $n$ features.

If we have more than one data, say $m$ rows of data, we rewrite the $x$ vector as a matrix $X$.
$$X=
\begin{bmatrix}
1 &x_1^1 &x_2^1 &\cdots &x_n^1\\
1 &x_1^2 &x_2^2 &\cdots &x_n^2\\
\vdots &\vdots &\vdots &\ddots &\vdots\\
1 &x_1^m &x_2^m &\cdots &x_n^m\\
\end{bmatrix}$$
In this notation we put features as columns androws as different rows in the matrix.
With $m$ rows of data, our $z$ values is now a vector $\textbf{z}$.
Row vector form:
$$z=b^TX^T$$
Column vector form (transpose it or have X before b):
$$z = (b^TX^T)^T\\
=Xb$$
Now hypothesis for $m$ rows of data can be $p(x)=\dfrac{1}{1+e^{-Xb}}$.
### Cost Function
[[#Cost Function|Recall]]
$$J(\beta) = -\dfrac{1}{m}
\left[
\sum^m_{i=1}
y^i
\log{(p(x^i))}
+(1-y^i)\log{(1-p(x^i))}
\right]$$
Vectorise this computation in Python with Numpy function `np.where()`, which we can use if we have more than one computation depending on certain conditions.
[NumPy Documentation for .where](https://numpy.org/doc/stable/reference/generated/numpy.where.html)
[Numpy Documentation for .sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html?highlight=sum#numpy.sum)
### Gradient Descent Update
[[#Gradient Descent|Recall]]
$$\beta_j = \beta_j - \alpha\dfrac{1}{m}\sum^m_{i=1}\left(p(x)-y^i\right)x_j^i$$
where hypothesis is $p(x)=\dfrac{1}{1+e^{-Xb}}$ for $m$ data points.
As we have the summation of some multiplication terms, it is a good candidate for matrix multiplication.

Similarly, $y$ which is the actual target value from the training set can be written as a column vector of size $m \times 1$. Therefore, we can do the calculation element-wise for the following term
$$p-y$$
and the result is also a column vector.

The features matrix can be arranged like
$$X=
\begin{bmatrix}
1 &x_1^1 &x_2^1 &\cdots &x_n^1\\
1 &x_1^2 &x_2^2 &\cdots &x_n^2\\
\vdots &\vdots &\vdots &\ddots &\vdots\\
1 &x_1^m &x_2^m &\cdots &x_n^m\\
\end{bmatrix}$$
and we can do the multiplication and summation as a matrix multiplication of $X(p-y)$.
The rest of the computation is just a multiplication of some constants, so we can write our update function as follows
$$b = b - \alpha\dfrac{1}{m}X(p-y)$$
## Multi-Class (One-VS-All)
Since Logistic function's output range only from 0 to 1, does it mean that it can only predict binary classification, i.e. classification problem involving only two classes? The answer is no. We can extend the technique to apply to multi-class classification by using a technique called one-versus-all.
The idea of one-versus-all technique is to reduce the multi-class classification problem to binary classification problem. Let's say we have three class and we would like to predict between cat, dog, and fish images. We can treat this problem as binary classification by predicting if an image is a cat or no cat. In this first instance, we treat both dog and fish images as a no-cat image. We then repeat the same procedures and try to predict if an image is a dog or a no-dog image. Similarly, we do the same with the fish and no-fish image.

To facilitate this kind of prediction, instead of having **one** target column in the **training set** , we will be preparing **three** target columns, each column for each class. We need to prepare something like the following data set.
![[Pasted image 20211231141956.png]]
We can then train the model **three times** and obtain the coefficients for **each class**. In this example, we would have **three sets** of beta coefficients, one for the cat versus no-cat, another one for dog versus no-dog, and the last one for fish versus no-fish. We can then use these coefficients to calculate the probability for each class and produce the probability

We can then construct three columns where each column contains the probability for the particular binary classification relevant to the column target.
Recall that our [[#Hypothesis Function|hypothesis function]] $p(x)=\dfrac{1}{1+e^{-Xb}}$ returns a probability between 0 to 1.
![[Pasted image 20211231142124.png]]
In the above example, the first two rows have cat class as their highest probability. Therefore, we set "cat" as the predicted class in the last column. On the other hand, the third and the last row have "dog" as their highest probability and therefore, they are predicted as "dog". Similarly, with "fish" in the second last row.
# Appendix
## Derivation of Logistic Regression Derivative
![[Pasted image 20211231142157.png]]
![[Pasted image 20211231142213.png]]