---
aliases: master method
tags: #50.004
---
[[Algo]]
[[Algo week 2]]
[[Master Theorem, Divide and Conquer, Peak Finding]]
# Master Method for Solving Recurrences
For recurrences of the form $T(n) = aT(n/b) + f(n)$,
where $a \geq 1$ and $b > 1$ are constants and $f(n)$ is an asymptotically positive function.

This describes the running time of an algorithm that divides a problem of size $n$ into $a$ subproblems, each of size $n/b$.
The $a$ subproblems are solved recursively, each in time $T(n/b)$.
The function $f(n)$ encompasses the cost of dividing the problem and combining the results of the subproblems.

## Technicalities
- $\dfrac{n}{b}$ might not be an integer.
- Just conveniently omit floors and ceilings as they don't usually affect the asymtotic behavior of the recurrence.

## Master Theorem
---
Let $a \geq 1$ and $b > 1$ be constants, let $f(n)$ be a function, and let $T(n)$ be defined on the non-negative integers by the recurrence $$T(n) = aT(n/b) + f(n)$$ where we interpret $\dfrac{n}{b}$ to mean either $\lfloor{n/b}\rfloor$ or $\lceil{n/b}\rceil$.
Then $T(n)$ has the following asymptotic bounds:
1. If $f(n) = O\left(n^{\log_b{a} - \epsilon}\right)$ for some constant $\epsilon > 0$, then $T(n) = \Theta\left(n^{\log_b{a}}\right)$.
2. If $f(n) = \Theta\left(n^{\log_b{a}}\right)$, then $T(n) = \Theta(n^{\log_b{a}} \lg{n}) = \Theta(f(n)\lg{n})$.
3. If $f(n) = \Omega\left(n^{\log_b{a} + \epsilon}\right)$ for some constant $\epsilon > 0$, and if $af(n/b) \leq cf(n)$ for some constant $c<1$, then $T(n) = \Theta(f(n))$.
---
What it says:
- In each case, we compare $f(n)$ with $n^{\log_b{a}}$.
- Intuitively, the larger of the two functions determines the solution to the recurrence.
- Case 1:
	- $n^{\log_b{a}}$ larger: solution is $\Theta(n^{\log_b{a}})$
- Case 2:
	- Same size
	- Multiply by a logarithmic factor
	- Solution is $T(n) = \Theta(n^{\log_b{a}}) = f(n) \lg{n}$
- Case 3:
	- $f(n)$ larger: solution is $\Theta(f(n))$
### Gaps
- If $f(n) = O(n^{\log_b{a-\epsilon}})$, $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b{a}})$?
- If $f(n) = \Theta(n^{\log_b{a}})$, $\epsilon > 0$, then $T(n) = \Theta(\log{n} \cdot n^{\log_b{a}})$?
- If $f(n) = \Omega(n^{\log_b{a+\epsilon}})$, $\epsilon > 0$, and if $af(n/b) \leq cf(n)$ where $c<1$ for all sufficiently large $n$, $T(n) = \Theta(f(n))$?

Gaps:
- $f(n) = O(n^{\log_b{a}})$ but not $f(n) = O(n^{\log_b{a-\epsilon}})$
- $f(n) = \Omega(n^{\log_b{a}})$ but not $f(n) = \Omega(n^{\log_b{a+\epsilon}})$
- $f(n) = \Omega(n^{\log_b{a+\epsilon}})$ but does not satisfy regularity condition

Go back to recursion tree or substitution method or exact definitions