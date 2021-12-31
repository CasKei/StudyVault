---
aliases: regression, simple linear regression
tags: #regression, #data, #ML
---
Back to [[Data Driven World|DDW]]
Back to [[Term 3]]
# Linear Regression
## Introduction
Linear regression is a machine learning algorithm dealing with a continuous data and is considered a supervised machine learning algorithm. Linear regression is a useful tool for predicting a quantitative response. Though it may look just like another statistical methods, linear regression is a good jumping point for newer approaches in machine learning.

In linear regression we are interested if we can model the relationship between two variables.
The linear regression algorithm will try to model the relationship between these two variables as a straight line equation $y=mx+c$.  The model consists of the two coefficients $m$ and $c$. Once we know these two coefficients, we will be able to predict the value of $y$ for any $x$.

## Hypothesis

^5181e5

We can make our straight line equation as our hypothesis.
$$y=\beta_0 + \beta_1 x$$
The purpose of our learning algorithm is to find an estimate for $\beta_0$ and $\beta_1$ given the values of $x$ and $y$.

In machine learning, we call $\beta_0$ and $\beta_1$ as the model _coefficents_ or _parameters_. What we want is to use our training data set to produce estimates $\hat{\beta_0}$ and $\hat{\beta_1}$ for the model coefficients. In this way, we can **predict** future resale prices by computing
$$\hat{y} = \hat{\beta_0} + \hat{\beta_1}x$$
where $\hat{y}$ indicates a prediction of $Y$. Note that we use the _hat_ symbol to denote the estimated value for an unknown parameters or coeffcient or to denote the predicted value. The predicted value is also called a hypothesis.
## Cost Function
In order to find the values of $\hat{\beta_0}$ and$\hat{\beta_1}$, we will apply optimization algorithm that minimizes the error. The error caused by the difference between our predicted value $\hat{y}$ and the actual data $y$ is captured in a _cost function_. Let's find our cost function for this linear regression model.

We can get the error by taking the difference between the actual value and our hypothesis and square them. The square is to avoid cancellation due to positive and negative differences. This is to get our absolute errors. For one particular data point $i$, we can get the error square as follows.
$$e^i = (\hat{y}(x^i)-y^i)^2$$
Assume we have $m$ data points, we can then sum over all data points to get the Residual Sum Square (RSS) of the errors.
$$RSS = \sum^m_{i=0}(\hat{y}(x^i)-y^i)^2$$
We can then choose the following as our cost function.
$$J(\hat{\beta_0}, \hat{\beta_1})=\dfrac{1}{2m}\sum^m_{i=0}(\hat{y}(x^i)-y^i)^2$$
The division by $m$ is to get an average over all data points. The constant $2$ in the denominator is make the derivative easier to calculate.
The learning algorithm will then try to obtain the constants $\beta s$  that minimizes the cost function.
## Gradient Descent
One of the algorithm that we can use to find the constants by minimizing the cost function is called _gradient descent_. The algorithm starts by some initial guess of the constants and use the gradient of the cost function to make a prediction where to go next to reach the bottom or the minimum of the function. In this way, some initial value of $\hat{\beta_0}$ and$\hat{\beta_1}$, we can calculate the its next values using the following equation.
$$\hat{\beta_i} = \hat{\beta_i} - \alpha \dfrac{\delta}{\delta\hat{\beta_i}}J(\hat{\beta_0}, \hat{\beta_1})$$
So calculating, (workings [here](https://github.com/CasKei/10.020DDW-CasKei/blob/main/d2w_notes-master/LinearRegression.ipynb), we have
$$
\begin{align}
\hat{\beta_0} &= \hat{\beta_0} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)\\
\hat{\beta_1} &= \hat{\beta_1} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x^i
\end{align}
$$
## Matrix Operations
### Hypothesis

^9e397c

Our predicted value for 1 data point was $\hat{y}(x^i)=\hat{\beta_0}+\hat{\beta_1}x^i$.
If we have $m$ data points, we will have a set of equations from $i=1$ to $i=m$.
We can rewrite this in terms of matrix.

Independent variable $x$ as column vector:
$$
\begin{bmatrix}
x^1\\
x^2\\
\vdots\\
x^m
\end{bmatrix}
$$
To write system of equations, add a column of contant 1s:
$$X=
\begin{bmatrix}
1 &x^1\\
1 &x^2\\
\vdots &\vdots\\
1 &x^m
\end{bmatrix}
$$
Constants as a column vector:
$$\hat{b}=
\begin{bmatrix}
\hat\beta_0\\
\hat\beta_1
\end{bmatrix}
$$
Our system of equations is then:
$$\hat{y}=X \times \hat{b}$$
The result is a column vector of $m \times 1$.

### Cost Function
[[Linear Regression#Cost Function|Recall]]
$$J(\hat{\beta_0}, \hat{\beta_1})=\dfrac{1}{2m}\sum^m_{i=0}(\hat{y}(x^i)-y^i)^2$$
Writing as matrix multiplication,
$$
J(\hat{\beta_0}, \hat{\beta_1})=\dfrac{1}{2m}(\hat{y} - y)^T \times (\hat{y} - y)
$$
### Gradient Descent
[[#Gradient Descent|Recall]]
$$
\begin{align}
\hat{\beta_0} &= \hat{\beta_0} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)\\
\hat{\beta_1} &= \hat{\beta_1} - \alpha \dfrac{1}{m}\sum^m_{i=1}(\hat{y}(x^i)-y^i)x^i
\end{align}
$$
So in matrix
$$
\begin{align}
\hat{b} &= \hat{b} - \alpha \dfrac{1}{m}X^T \times (\hat{y}-y)\\
\hat{b} &= \hat{b} - \alpha \dfrac{1}{m}X^T \times (X \times \hat{b}-y)
\end{align}
$$
and [[#Hypothesis|recall]]
$$X=
\begin{bmatrix}
1 &x^1\\
1 &x^2\\
\vdots &\vdots\\
1 &x^m
\end{bmatrix}
$$
where transposed is
$$X^T=
\begin{bmatrix}
1 &1 &\cdots &1\\
x^1 & x^2 &\cdots &x^m
\end{bmatrix}
$$
## Metrics
After we build our model, we usually want to evaluate how good our model is. We use metrics to evaluate our model or hypothesis. To do this, we should split the data into two:
-   training data set
-   test data set

The training data set is used to build the model or the hypothesis. The test data set, on the other hand, is used to evaluate the model by computing some metrics.
### Mean Squared Error
$$MSE =\dfrac{1}{n}\sum^n_{i=1}(y^i - \hat{y}^i)^2$$
where $n$ is the number of predicted data points in the test data set,  $y^i$ is the actual value in the test data set, and $\hat{y}^i$ is the predicted value obtained using the hypothesis and the independent variable $x^i$ in the test data set.
### R2 Coefficient of Determination
$$r^2 = 1-\dfrac{SS_{res}}{SS_{tot}}$$
where $SS_{res}=\sum^n_{i=1}(y_i-\hat{y}_i)^2$ 
and $SS_{tot}=\sum^n_{i=1}(y_i-\bar{y})^2$, 
where $\bar{y}=\dfrac{1}{n}\sum^n_{i=1}y_i$ 
and $n$ is the number of target values.

This coefficient gives you how close the data is to a straight line.
The closer it is to a straight line, the closer the value is to 1.0.
This means there is a correlation between the independent variable and the dependent variable.
When there is n correlation, the value will be close to 0.