---
tags: #50.004
---

# 50.004 Homework Set 1
## Cassie Chong (1005301) Cohort 01
### Qn 1
![[Pasted image 20220128100714.png]]
#### i)
![[Pasted image 20220128101028.png]]
We have $f(n) = O(g(n))$.
This means there exists positive constants $c$ and $n_0$ such that $0 \leq f(n) \leq cg(n) \forall n \geq n_0$.

Suppose $2^{f(n)} = O(2^{g(n)})$ is true.
This implies there exists positive constants $c$ and $n_0$ such that $0 \leq 2^{f(n)} \leq c2^{g(n)} \ \forall \  n \geq n_0$.
That is, $2^{f(n)} \leq c2^{g(n)}$ should be true for positive $c$ and $n$.

Raise $f(n) = 3n$ and $g(n) = n$ as example.
$f(n) = O(g(n))$ is true as $3n = O(n)$.
Check $2^{3n} \leq c 2^{n}$:
$$\begin{align}
\Rightarrow \dfrac{2^{3n}}{2^n} &\leq c \\
2^{2n} &\leq c
\end{align}
$$
There is no constant $c$ that can make this true as $n \to \infty$.
**Hence this statement is ==False==.**

#### ii)
![[Pasted image 20220128101107.png]]
We have $f(n) = O(g(n))$ and $g(n) = O(h(n))$.
This means there exists positive constants $c$ and $n_0$ such that $0 \leq f(n) \leq c_0g(n) \forall n \geq n_0$, and $0 \leq g(n) \leq c_1h(n) \forall n \geq n_0$.
Hence, 
$$
\begin{align}
&0 \leq f(n) \leq c_0 g(n) \leq c_0c_1h(n)&, \forall n \geq n_0 \\
&\Rightarrow 0 \leq f(n) \leq c_3h(n)&, \text{where } c_3 = c_1 \cdot c_2, \forall n \geq n_0
\end{align}
$$
**Thus** $f(n) = O(h(n))$ **hence the statement is ==True==**

#### iii)
![[Pasted image 20220128101117.png]]
$\Omega$ is a lower bound.
All algorithms take time, at least a constant time, so the lower bound running time is always at least $\Omega(1)$.
**Statement is ==True==.**

#### iv)
![[Pasted image 20220128101128.png]]
Big Theta suggests that the growth of functions $f$ and $g$ are as fast as $n$ and $2n$ respectively.
Coefficients are insignificant compared to the degree of $n$ when looking at the rate of growth when $n$ turns arbitrarily large.
With the same degree of $n$, the two functions will not be bound by one another in anyway and will be similar as $n \to \infty$.
**Hence statement is ==False==**.

#### v)
![[Pasted image 20220128101143.png]]
$$\log{n} \leq n \ \forall n \geq 0$$
Since upper bound of $f(n)$ is always larger than the upper bound of $g(n)$, we can conclude that the worst-case running time of B is lower than A.
However, this does not imply that B must always be faster than A for all $n$, only when $n \to \infty$. A might be faster than B for some small $n$ which we have no information about.
**Statement is ==False==.**

### Qn 2
![[Pasted image 20220128101153.png]]
#### i)
![[Pasted image 20220128101210.png]]
$$f(n) = 0 + 1^3 + 2^3 + \cdots + n^3$$
Lower bound 0 when $i = 0$
Upper bound $n^3$ or higher order
Adam True (discrete), Beatrice False, Colin True, Diana True
==**Ans: c**==

#### ii)
![[Pasted image 20220128101221.png]]
**==Ans: d==**

#### iii)
![[Pasted image 20220128101239.png]]
**==Ans: c==**

#### iv)
![[Pasted image 20220128101249.png]]
(edit: Errata: What is the ***biggest*** possible value of $k$...)
**==Ans: a==**

#### v)
![[Pasted image 20220128101302.png]]
**==Ans: d==**

### Qn 3
![[Pasted image 20220128101312.png]]
#### i)
![[Pasted image 20220128101323.png]]

**==Ans: ==**$T(n) = \Theta(n^4)$

#### ii)
![[Pasted image 20220128101331.png]]
(Edit: Errata: last line is `print(f(n))`)
**==Ans: ==**$T(n) = \Theta(1)$

#### iii)
![[Pasted image 20220128101341.png]]
**==Ans: ==**$T(n) = \Theta(n^3)$

#### iv)
![[Pasted image 20220128101350.png]]
**==Ans: ==** $T(n) = \Theta(\log_k{n})$

#### v)
![[Pasted image 20220128101401.png]]
**==Ans: ==** $T(n) = \Theta(n)$

### Qn 4
![[Pasted image 20220128101413.png]]

|$f(n)$|$g(n)$|$f(n) = O(g(n))$|$f(n) = \Omega(g(n))$|$f(n) = \Theta(g(n))$|
|---|---|---|---|---|
|$n^k$|$c^n$      |    T   |   F   |  F     |
|$\log_2{n}$|$\log_8{n}$ |    T   |    T  |   T   |
|$8^n$|$4^n$      |    F   |    T  |    F  |
|$3^n$|$n2^n$     |    F    |   T    |   F    |
|$\log{(n!)}$|$n \log{n}$|    T    |    F    |    F   |

### Qn 5
![[Pasted image 20220128101430.png]]
#### i)
![[Pasted image 20220128101442.png]]
***Proof***: 
$T(n) = \Theta(f(n))$ implies that $c_1 \cdot f(n) \leq T(n) \leq c_2 \cdot f(n)$, where $c_1, c_2, n_0 \geq 0$.
Let $n$ be some value where $n > 0$. We have
$$\max{(f(n), g(n))} \leq f(n) + g(n)$$
since the maximum among $f$ and $g$ can never exceed their sum,
and
$$f(n) + g(n) \leq 2\max{(f(n), g(n))}$$
since the double of the maximum between $f$ and $g$ is sure to be more than the sum of $f$ and $g$.
Merging the two,
$$
\begin{align}
\max{(f(n) + g(n))} \leq f(n) + g(n) \leq 2\max{(f(n) + g(n))}
\end{align}
$$
As $f(n) + g(n)$ is bounded by different constant multiples of $\max{(f(n) + g(n))}$, namely $c_1 = 1$ and $c_2 = 2$, letting $n_0 = 1$, we satisfy the definition of $\Theta$ notation where $f(n) + g(n) = \Theta(\max{(f(n), g(n))})$. ==***QED***==


#### ii)
![[Pasted image 20220128101504.png]]
i) We have $T_A(n) = f(n)$ and $T_B(n) = \dfrac{n}{f(n)}$.
Hence, 
$$
\begin{align}
T_C(n) &= T_A(n) + T_B(n)\\
&= f(n) + \dfrac{n}{f(n)}\\
&= \dfrac{(f(n))^2+n}{f(n)}\\
\end{align}
$$
We want to run C in the shortest time, that is, we wish to minimise $T_C(n)$.
With knowledge of what function $f(n)$ is, we can differentiate $T_C(n)$ with respect to some parameter to be found, and equate it to $0$ to find its minima and maxima. I cannot assume that function $f(n)$ is a polynomial; it may be a logarithmic or exponential function, or some other, so I will not carry out the differentiation as it would yield different results from here.
Minimum can be verified with a second derivative.
Hence we find $f(n)$ by ==optimising== $T_C(n)$.

ii) Since algorithm D runs A and B simultaneously, the running time of D would be
$$\begin{align}
T_D(n) &= \max{(T_A(n), T_B(n))}\\
&= \max{\left(f(n), \dfrac{n}{f(n)}\right)}
\end{align}$$
This is evidently ==different== from the time complexity of C as it refers to the longer time complexity between A and B rather than their sum. C would definitely take longer than D as all time is positive and an addition would yield a higher time than picking out the maximum between them.

#### iii)
![[Pasted image 20220128101513.png]]
Given $T(n) = 2T\left(\dfrac{n}{2}\right) + \Theta(n)$, we observe that this algorithm does the following:
1. Half the input size so we have 2 sets of inputs to work with from each set
2. Recursively call the algorithm for each halved set of input
3. Combine the two-subproblems which is specified to run in $\Theta(n)$ time

From the above, analysing them part by part:
1. Dividing the problem takes a constant time $O(1)$ each. For a total of $n$ inputs, we consider it $\Theta(n)$
2. The problem of size $n$ can be halved a maximum of only $\log_2{n}$ times, as the entire input is iterated through. Thus this step takes $O(\log_2{n})$.
3. Combining takes $\Theta(n)$. The combine is done for all the subproblems, so combining with the step above, in total, we have $\Theta(n \log_2{n})$

Taking the above into consideration,
$$
\begin{align}
T(n) &= \Theta(n) + \Theta(n \log_2{n}) \\
&= \Theta(n\log_2{n})
\end{align}
$$
**==Solved==**.