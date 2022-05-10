---
aliases: algo class 2
tags: #50.004, #practice
---
[[Algo]]
[[Sorting, solving recursion]]
[[Master Theorem, Divide and Conquer, Peak Finding]]

# Use master theorem
## Exercise 1
$$T(n) = 9T(n/3)+n$$
For this recurrence, we have $a=9$, $b=3$, $f(n) = n$.
Thus, we have $n^{\log_b{a}} = n^{\log_3{9}} = \Theta{(n^2)}$.
Since $f(n) = O(n^{\log_3{9-\epsilon}})$, where $\epsilon = 1$, we apply case 1 of master theorem and conclude that solution is
$T(n) = \Theta(n^2)$

## Exercise 2
(these are in textbook pg 116 on ipad books)

## Exercise 3
(tb)

## Exercise 4
$$T(n) = 4T(n/2) + n^2$$
$a = 4, b = 2, f(n) = n^2$.
$n^{\log_b{a}} = n^{\log_2{4}} = n^2 = \Theta(n^2)$.
$f(n) = \Theta(n^{\log_b{a}}) = n^2$ in case 2 of master theorem.
Thus we conclude that the solution is
$T(n) = \Theta(n^2 \log_2{n})$
## Exercise 5
$$T(n) = 7T(n/3) + \Theta(n^2)$$
$a = 7, b = 3, f(n) = \Theta(n^2)$
$n^{\log_b{a}} = n^{\log_3{7}} \approx 1.77 = \Omega(n^2)$.
Since $f(n) = \Omega(n^{\log_b{a+\epsilon}})$ where $\epsilon \approx 0.23$, case 3 applies if we can show the regularity condition for $f(n)$.
For sufficiently large $n$, we have that
$af(n/b) = $

## Exercise 6 *
