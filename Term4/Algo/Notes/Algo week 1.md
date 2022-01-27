# L01.01 Complexity
## Why study algo
1. You want algo to terminate with correct output
2. Speed matters: speed is time, money, productivity

## Grading
- 6 weekly hw (15%)
- 2 prob sets (20%) due wk 5 and wk 11
- 2 tests (30%)
- 2D project (5%)
- Final exam (30%) wk 14
- Survey (2%)

## Basic definitions
> Algorithm: any well-defined computational procedure that takes some value, or set of values, as input and performs some action and/or produces some value, or set of values, as output.

Thus, an algo is a sequence of computational steps that transforms the input.
Like software, hardware, UI, etc, is a kind of technology.
--> Algo is a procedure for solving problems.

> Correct algorithm: for every input, it halts with the correct output or the correct action performed

Incorrect algo may not halt on some inputs, or halt with incorrect output or action performed
Incorrect algo can sometimes be useful if we can control their error rate, but we shall normally be concerned with correct algorithms.

> Algo Efficiency: the resources needed to run an algorithm on a computer

Resources: time, computer's memory, computer's hardware, etc
The differences between algos can be much more significant than differences due to hardware and software


## More basic definitions
> Computational problem: a function that maps an input to an output

Given x we want to compute f(x)
A good algo can compute f(x) quickly and correctly.

> Input space: set of possible inputs

> Output space: set of possible outputs

> Input instance: a particular input of a problem instance

## Exercise 1
Define input + output space & give example of input instance for
1. Integer multiplication
	1. input: integers
	2. output: integers
2. Find if given integer k is in a list of n integers [k1, k2...kn]
	1. input: the set of integers
	2. output: k is in the set or not, 0 or 1, yes or no.
3. sort a list of n integers in increasing order
	1. input: the set of n integers to be sorted, or any set of n integers
	2. output: the sorted list

What is the size of input instance in each case?
1. 2 (2 integers)
2. 1 (1 integer k)
3. n (n integers)

## Definitions
> Algorithm: procedure for solving acomputational problem

Usually a finite sequence of operations
- described in flow charts
- described in structured english
- written in pseudocode or real code.

## Property of algo
### Size
$$|x| = size = n$$
$$T(n) = \text{number of steps to solve the problem as a function of its size}$$
## A good algo
- Correct
- Fast: T(n) should increase 'slowly' as n grows
## Asymptotic Complexity
> Asymptotic complexity: describes T(n), as n grows to infinity

In this course we talk about 3 types of asymptotic complexity
- Big Theta
	- "grows asymptotically ="
	- Grows as fast as...
	- Example: $n^2=\Theta(n^2)$
		- When n increases, n^2 grows in the same level of speed as n^2
		- $0.1n^2 - 100n^{1.9} + 5 = \Theta(n^2)$
	- $F(x) = \Theta(G(x))$ means "F grows equally as G, when x grows to infinity"
- Big O
	- "grows asymptotically <="
	- Grows at most as fast as...
	- Example: $n^2=O(n^{1000})$
		- $2n^3 + 100n^2 + 5 = O(n^{30000})$
	- $F(x) = O(G(x))$ means "F grows at most as fast as G, when x grows to infinity"
- Big Omega
	- "grows asymptotically >="
	- Grows at least as fast as...
	- Example: $n^{9999} = \Omega(1)$
		- When n increases, n^2 grows in the same level of speed as n^2
		- $2n^{9999} + 100n^{33} + 5 = \Omega(n^2)$
	- $F(x) = \Theta(G(x))$ means "F grows at least as fast as G, when x grows to infinity"

## Exact Definitions
$$f(n) = O(g(n)) \Leftrightarrow \exists D>0, n_0 \text{ such that } |f(n) \leq D(g(n)| \text{ for } n \geq n_0$$
Intuition: I am g(n) and you are f(n). If I am faster than you, then no matter how far I am behind you now, one day I will surpass you.
f(n) and g(n) should be asymptotically non-negative. That means when n is large enough, f(n) and g(n) should all >= 0.

$$f(n) = \Omega(g(n)) \Leftrightarrow \exists D>0, n_0 \text{ such that } |f(n) \geq D(g(n)| \text{ for } n \geq n_0$$
Intuition: I am g(n) and you are f(n). If you are faster than me, then no matter how far I am ahead of you now, one day you will surpass me.

$$f(n) = \Theta(g(n)) \Leftrightarrow \exists D_1,D_2>0, n_0 \text{ such that } D_1|g(n)|\geq|f(n)|\geq D_2|g(n)| \text{ for } n \geq n_0$$
![[Pasted image 20220124144114.png]]
Theorem 3.1
For any 2 functions $f(n)$ and $g(n)$, we have $f(n) = \Theta(g(n))$ iff $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$
![[Pasted image 20220124144714.png]]
![[Pasted image 20220124145149.png]]

# L01.02 Document Distance
## How to read code and find its T(n)
Need to read code, but not really write code in this course.
Pseudo:
```
if a is divisible by 3
	print "oh yeah"
```
Code:
```
if (a%3 == 0)
	print("oh yeah")
```
Pseudo is enough for this course.
### How to read code
#### Constants
```print("great")```
This takes T(n) = 1
i.e. the number of steps required to comlete this program is 1
This code has complexity $\Theta(1)$
```
print("great")
print("great")
print("great")
print("great")
```
This takes T(n) = 4
i.e. the number of steps required to complete this program is 4
This code has complexity $\Theta(1)$
#### Loops
```
for (i=0; i<5; i++)
	print('great')
```
i = 0 to 4
T(n) = 5
i.e. the number of steps required to complete this program is 5
This code has complexity $\Theta(1)$
```
for (i=0; i<n; i++)
	print('great')
```
i = 0 to n-1
T(n) = n
i.e. the number of steps required to complete this program is n
This code has complexity $\Theta(n)$
```
for (int i=0; i<n; i++)
	for (int j=0; j<n; j++)
		print('great')
```
T(n) = n^2
i.e. the number of steps required to complete this program is n^2
This code has complexity $\Theta(n^2)$
```
for (int i=0; i<n; i++)
	for (int j=0; j<n; j++)
		print('great')
for (k=0; k<n; k++)
	print('great')
```
T(n) = n^2 + n
This code has complexity $\Theta(n^2)$
```
for (i=0; i<n^0.5; i++)
	print('hi')
```
$T(n) = \Theta(\sqrt{n})$ 
```
for (i=0; i<n^0.5; i++)
	for (j=0; j<n^0.5; j++)
		print('great')
```
$T(n) = \Theta(\sqrt{n} \cdot \sqrt{n}) = \Theta(n)$
```
for (i=0; i<n; i++)
	for (j=0; j<=i; j++)
		print('hi')
```
![[Pasted image 20220125111411.png]]
![[Pasted image 20220125154704.png]]
### Worst-case and average-case analysis
## The cost model of code
## Document Distance
## How do we implement document distance in python (not required)
# C01
### Problem 1
![[Pasted image 20220125155603.png]]

|f(n)| 1s| 1min| 1hr| 1day| 1mth| 1yr| 1century|
|---|---|---|---|---|---|---|---|
|lg n|$2^{10^6}$|||||||
|$n^{0.5}$  |$10^{12}$|||||||
|n|$10^6$|||||||
|n lgn||||||||
|n^2|$10^3$|||||||
|n^3|$10^2$|||||||
|2^n||||||||
|n!||||||||

### Problem 2
$$
\begin{align}
f(x) &= x\\
g(x) &= x+2
\end{align}
$$
$f \in O(g)$?: True
$g \in \Omega(f)$?: True
$g \in O(f)$?: True

### Problem 3
$$x+2 \leq x \cdot ?$$
Any constant greater than 1.
$$g \in O(f)?$$
### Problem 4
$$
\begin{align}
f(x) &= x^2 \\
g(x) &= x^2 + 2 \\
h(x) &= x^2 + 3x + 2
\end{align}
$$
$f \in O(g)$?: True
$f \in O(h)$?: True
$f \in \Omega(g)$?: True
$f \in \Omega(h)$?: True

### Problem 5
$$
\begin{align}
f(x) &= x^2 \\
g(x) &= 1000x^2 + 500x + 100 \\
\end{align}
$$
$f \in \Omega(g)$?: True
$100x^2 + 500x + 100 \in \Theta(x^2)$

### Problem 6
$1000x^2 \in \Theta(x^3)$?: False

### Problem 7
$$
\begin{align}
f(x) &= 1000x^2 \\
g(x) &= x^3 \\
\end{align}
$$
$g \in O(f)$?: False
$g \in \Omega(f)$?: True
$f \in O(g)$?: True
$f \in \Omega(g)$?: False
$f \in \Theta(g)$?: False
$g \in \Theta(f)$?: False

### Problem 8
$$
\begin{align}
f(x) &= x \\
g(x) &= \log_2{x} \\
\end{align}
$$
$f \in O(g)$?: False
$f \in \Omega(g)$?: True
$g \in O(f)$?: True
$g \in \Omega(f)$?: False
$f \in \Theta(g)$?: False

### Problem 8.1
$$
\begin{align}
f(x) &= x \\
g(x) &= (\log_2{x})^2 \\
\end{align}
$$
$f \in O(g)$?: False
$f \in \Omega(g)$?: True
$g \in O(f)$?: True
$g \in \Omega(f)$?: False
$f \in \Theta(g)$?: False
Same. Does not matter how many.

### Problem 9
$$\begin{align}
f(x) &= n \log_2{n} \\
g(x) &= n^2 \\
\end{align}$$
$f(n) \leq g(n)$ so
$f \in O(g)$?: True
$f \in \Omega(g)$?: False
$g \in O(f)$?: False
$g \in \Omega(f)$?: True
$f \in \Theta(g)$?: False

### Problem 10
$$
\begin{align}
g(n) &= n^2 \\
f(n) &= n\log_2{n} \\
h(n) &= n\\
b(n) &= \log_2{n}
\end{align}
$$
$g \in O(100f)$: False
$g \in \Omega(f)$: True
$b \in O(f)$: True
$b \in \Theta(f)$: False
$h \in O(b + h)$: True
$g \in \Omega(g + h)$: True
$g \in \Theta(g + h)$: True

### Problem 11
We are given that an algo has complexity $O(\log{n})$ in the given input size n.
Explain why the complexity for this is also $O(\log_b{n})$, regardless of the choice of any base $b > 1$ for the logarithm appearing in the expression.

Since big O notation, $0 \leq f(n) \leq c \cdot g(x)$, where $g(x) = \log{n}$.
We have $\log_b{n} = \dfrac{\log{n}}{\log{b}}$ where $\log{b} > 0$.
$$
\begin{align}
0 &\leq f(n) \leq c \cdot g(x)\\
0 &\leq \dfrac{f(n)}{\log{b{}}} \leq \dfrac{c \cdot \log{n}}{\log{b}} = \log_b{n}\\
0 &\leq f(n) \leq \log{b} \cdot c \cdot \log_b{n}
\end{align}
$$
Where $\log{b} \cdot c$ is $c_1$.

---

Interpreting the given complexity to have a base 2, applying change of base to base b, we have
$$
\begin{align}
O(\log_2{n})&=O\left(\dfrac{\log_b{n}}{\log_b{2}}\right)\\
&= O \left(\dfrac{1}{\log_b{2}} \cdot \log_b{n}
\right)\\
&= O \left(\log_b{n}\right)
\end{align}
$$
Since $O\left(\dfrac{1}{\log_b{2}}\right)$ is a constant and of lower order than $O(\log_b{n})$.

