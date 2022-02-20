---
aliases: multiple regression
tags: #regression, #data, #ML
---
Back to [[Data Driven World|DDW]]
# Multiple Linear Regression
## Introduction
[[Linear Regression|Previously]] we only have one independent variable or one feature.
In most cases of ML we want to include more than one feature, or have a hypothesis that is not simply a straight line.

With multiple linear regression we can [[#Hypothesis|include more than 1 feature]] and [[#Polynomial Model|model our equation beyond a simple straight line.]]
## Hypothesis
[[Linear Regression#Hypothesis|Recall in Linear regression the hypothesis is:]] $\hat{y}=\hat{\beta_0} + \hat{\beta_1}x$, where $x$ is the only independent variable or feature.
In multiple linear regression, we have more than one feature. Hypothesis becomes:
$$\hat{y}=\hat{\beta_0} + \hat{\beta_1}x_1 + \hat{\beta_2}x_2 + \dots + \hat{\beta_n}x_n$$
We have $n$ features. Note we assume $x_0=1$ with $\hat{\beta_0}$ as its coefficient.

Write this as a row vector to form the features term
$$X=\begin{bmatrix}
x_0 &x_1 &\cdots &x_n
\end{bmatrix}
\in \mathbb{R}^{n+1}
$$
Note that the dimension of the feature is $n+1$ because we have $x_0 = 1$ which is a constant of 1.

The parameters can be written as:
$$
\hat{b} =
\begin{bmatrix}
\hat{\beta_0}\\
\hat{\beta_1}\\
\vdots\\
\hat{\beta_n}
\end{bmatrix}
\in \mathbb{R}^{n+1}
$$

Our system of equations can now be written as:
$$
\begin{align}
\hat{y}(x^1)&=\hat{\beta_0} + \hat{\beta_1}x_1^1 + \hat{\beta_2}x_2^1 + \dots + \hat{\beta_n}x_n^1\\
\hat{y}(x^2)&=\hat{\beta_0} + \hat{\beta_1}x_1^2 + \hat{\beta_2}x_2^2 + \dots + \hat{\beta_n}x_n^2\\
&\vdots\\
\hat{y}(x^m)&=\hat{\beta_0} + \hat{\beta_1}x_1^m + \hat{\beta_2}x_2^m + \dots + \hat{\beta_n}x_n^m\\
\end{align}
$$
In the above equations, the superscript indicates the index for data points from 1 to $m$, assuming there are $m$ data points.

To write a hypothesis as a matrix we need the features as a matrix.
$$X=
\begin{bmatrix}
1 &x^1_1 &\cdots &x^1_n\\
1 &x^2 &\cdots &x^2_n\\
\vdots &\vdots &\ddots &\vdots\\
1 &x^m &\cdots &x^m_n
\end{bmatrix}
\in \mathbb{R}^{m \times (n+1)}
$$
Now with this the hypothesis as a matrix multiplication is:
$$\hat{y} = X \times \hat{b}$$
[[Linear Regression#^9e397c|Notice this is the same matrix equation as a simple linear regression.]]
What is different is that $\hat{b}$ contains more than 2 parameters.
Similarly, the matrix $X$ is now of dimention $m \times (n+1)$ where $m$ is the number of data points and $n+1$ is the number of parameters.
## Cost Function
[[Linear Regression#Cost Function|Recall]]
$$J(\hat{\beta_0}, \hat{\beta_1})=\dfrac{1}{2m}\sum^m_{i=0}(\hat{y}(x^i)-y^i)^2$$
Rewriting the square as a matrix multiplication,
$$J(\hat{\beta_0}, \hat{\beta_1})=\dfrac{1}{2m}(\hat{y} - y)^T \times (\hat{y} - y)$$
This is the same as in [[Linear Regression|simple linear regression]].
## Gradient Descent
[[Linear Regression#Gradient Descent|Recall]] in linear regression
$$\begin{align}
\hat{\beta_0} &= \hat{\beta_0} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)\\
\hat{\beta_1} &= \hat{\beta_1} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x^i
\end{align}$$
In multiple linear regression, we have more than one feature and have to differentiate for each.
So this results in a system of equations as follows:
$$\begin{align}
\hat{\beta_0} &= \hat{\beta_0} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x_0^i\\
\hat{\beta_1} &= \hat{\beta_1} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x_1^i\\
\hat{\beta_2} &= \hat{\beta_2} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x_2^i\\
\vdots \\
\hat{\beta_n} &= \hat{\beta_n} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x_n^i
\end{align}$$
where $x_0 = 1$ for all $i$.

Hence, same as before, gradient descent update function in matrix operations:
$$\begin{align}
\hat{b} &= \hat{b} - \alpha \dfrac{1}{m}X^T \times (\hat{y}-y)\\
\hat{b} &= \hat{b} - \alpha \dfrac{1}{m}X^T \times (X \times \hat{b}-y)
\end{align}$$
This means that all our equations have not changed and we just need to create the right parameter and feature matrices.
## Polynomial Model
There are times when, even with one feature, we may want a hypothesis that is not a straight line.
We can refer to the above multiple linear regression matrices and replace the different parameters with different degrees of the feature as required.
The parameters can be found using the same gradient descent that minimises the cost function.