---
aliases: complexity, asymptotic notation
tags: #50.004
---
[[Document Distance]]
[[Algo]]
# L01.01 Complexity

## Why study algo

1.  You want algo to terminate with correct output
2.  Speed matters: speed is time, money, productivity

## Grading

-   6 weekly hw (15%)
-   2 prob sets (20%) due wk 5 and wk 11
-   2 tests (30%)
-   2D project (5%)
-   Final exam (30%) wk 14
-   Survey (2%)

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

Given $x$ we want to compute $f(x)$ 
A good algo can compute $f(x)$ quickly and correctly.

> Input space: set of possible inputs

> Output space: set of possible outputs

> Input instance: a particular input of a problem instance

## Exercise 1

Define input + output space & give example of input instance for

1.  Integer multiplication
    1.  input: integers
    2.  output: integers
2.  Find if given integer $k$ is in a list of n integers $[k1, k2...kn]$
    1.  input: the set of integers
    2.  output: $k$ is in the set or not, `0` or `1`, yes or no.
3.  sort a list of $n$ integers in increasing order
    1.  input: the set of $n$ integers to be sorted, or any set of $n$ integers
    2.  output: the sorted list

What is the size of input instance in each case?

1.  2 (2 integers)
2.  1 (1 integer k)
3.  n (n integers)

## Definitions

> Algorithm: procedure for solving acomputational problem

Usually a finite sequence of operations

-   described in flow charts
-   described in structured english
-   written in pseudocode or real code.

## Property of algo

### Size
$$|x| = size = n$$
$$T(n) = \text{number of steps to solve the problem as a function of its size}$$

## A good algo

-   Correct
-   Fast: $T(n)$ should increase 'slowly' as n grows

## Asymptotic Complexity

> Asymptotic complexity: describes $T(n)$, as $n$ grows to infinity

In this course we talk about 3 types of asymptotic complexity

-   Big Theta
    -   "grows asymptotically ="
    -   Grows as fast as...
    -   Example: $n^2=\Theta(n^2$)
        -   When $n$ increases, $n^2$ grows in the same level of speed as $n^2$
        -   $0.1n^2 - 100n^{1.9} + 5 = \Theta(n^2)$
    -   $F(x) = \Theta(G(x))$ means "F grows equally as G, when x grows to infinity"
-   Big O
    -   "grows asymptotically <="
    -   Grows at most as fast as...
    -   Example: $n^2=O(n^{1000})$
        -   $2n^3 + 100n^2 + 5 = O(n^{30000})$
    -   $F(x) = O(G(x))$ means "F grows at most as fast as G, when x grows to infinity"
-   Big Omega
    -   "grows asymptotically >="
    -   Grows at least as fast as...
    -   Example: $n^{9999} = \Omega(1)$
        -   When n increases, $n^2$ grows in the same level of speed as $n^2$
        -   $2n^{9999} + 100n^{33} + 5 = \Omega(n^2)$
    -   $F(x) = \Omega(G(x))$ means "F grows at least as fast as G, when x grows to infinity"

## Exact Definitions
$$f(n) = O(g(n)) \Leftrightarrow \exists D>0, n_0 \text{ such that } |f(n) \leq D(g(n))| \text{ for } n \geq n_0$$
-> Intuition: I am $g(n)$ and you are $f(n)$. If I am faster than you, then no matter how far I am behind you now, one day I will surpass you.  
$f(n)$ and $g(n)$ should be asymptotically non-negative. That means when n is large enough, $f(n)$ and $g(n)$ should all >= 0.

$$f(n) = \Omega(g(n)) \Leftrightarrow \exists D>0, n_0 \text{ such that } |f(n) \geq D(g(n))| \text{ for } n \geq n_0$$
-> Intuition: I am $g(n)$ and you are $f(n)$. If you are faster than me, then no matter how far I am ahead of you now, one day you will surpass me.

$$f(n) = \Theta(g(n)) \Leftrightarrow \exists D_1,D_2>0, n_0 \text{ such that } D_1|g(n)|\geq|f(n)|\geq D_2|g(n)| \text{ for } n \geq n_0$$
![Pasted image 20220124144114.png](app://local/C%3A%5CUsers%5Ccassi%5CWorkspace%5CStudyVault%5CAttachments%5CPasted%20image%2020220124144114.png?1643006474023)  
> **Theorem** **3.1**
For any 2 functions $f(n)$ and $g(n)$, we have $f(n) = \Theta(g(n))$ iff $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$  
![Pasted image 20220124144714.png](app://local/C%3A%5CUsers%5Ccassi%5CWorkspace%5CStudyVault%5CAttachments%5CPasted%20image%2020220124144714.png?1643006834504)  
![Pasted image 20220124145149.png](app://local/C%3A%5CUsers%5Ccassi%5CWorkspace%5CStudyVault%5CAttachments%5CPasted%20image%2020220124145149.png?1643007109378)