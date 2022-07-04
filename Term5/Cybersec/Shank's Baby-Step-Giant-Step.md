---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]
[[Discrete logarithm problem]]

[[Diffie-Hellman key exchange]] is based on this.

An attacker can obtain the key if he can solve the [[Discrete logarithm problem]], that is to find $x$ in $\alpha ^x = \beta$, where $1 \leq x \leq p - 1$. So, $\alpha$ , $\beta$ are the inputs, we want to find $x$.

We can also write the problem as $x = \log_\alpha{\beta}$.

To do this, the problem is written in a 2 digit representation:$$x=x_gm-x_b  \hspace{2em} ,0 \leq x_g , x_b$$
In this way, we can write the exponentiation as:
$$\begin{align}
\beta = &\alpha^x = a^{x_gm-x_b}\\
\beta\alpha^{x_b}&= a^{x_gm}
\end{align}
$$
## Overview
This is a meet in the middle algo for computing the [[Discrete logarithm problem|discrete logarithm]] or order of an element in a finite abelian group. The algo is based on a space-time tradeoff. It is a fairly simple modification of trial multiplication, the naive method of finding discrete logarithms.

Given a cyclic [[Group]] $G$ of order $n$, a generator $\alpha$ of the group and a group element $\beta$, find an integer $x$ such that $\alpha^x = \beta$.

The algorithm is based on rewriting $x$:
$$
\begin{align}
x &= im + j\\
m &= \left\lceil\sqrt{n}\ \right\rceil\\
0 &\leq  i < m \\
0 &\leq j < m
\end{align}
$$
Therefore:
$$
\begin{align}
\alpha^x &= \beta\\
\alpha^{im+j} &= \beta\\
\alpha^j &= \beta(\alpha^{-m})^i
\end{align}
$$
The algo precomputes $\alpha^j$ for several values of $j$. Then it fixes an $m$ and tries values of $i$ in the RHS of the congruence above, in the manner of trial multiplication. It tests to see of the congruence is satisfied for any value of $j$, using the precomputed values of $\alpha^j$.

## Algo
![[Pasted image 20220624222630.png]]

## In practice
Best way to speed up tihs is to use an efficient table lookup scheme. Best is [[Hash Table]]. Hashing is done on the second component, and perform the check in step 1 of the main loop. $\gamma$ is hashed and the resulting memory address checked. Since hash tables can retrieve and add elements in $O(1)$ time, and this does not slow down the overall algo.

Running time and space complexity is $$O(\sqrt{n})$$, faster than $O(n)$ in naive brute force calculation.

This algo is often used to solve for the shared key in the [[Diffie-Hellman key exchange]], when the modulus is a prime number. If modulus is not prime, the [[Pohlig-Hellman]] algo has a smaller algo complexity, and solves the same problem.

## Notes
- Generic, works for every finite cyclic [[Group]].
- Not necessary to know order of group in advance. Algo still works if $n$ is merely an upper bound on the group order
- Usually used for groups whose order is prime. If order is composite then [[Pohlig-Hellman]] is more efficient.
- Needs $O(m)$ memory. Use less by choosing a smaller $m$ in the first step. This increases time, which is $O(n/m)$. Alternatively use [[Pollard's Rho]] algo for logarithms, which has same running time as baby-step giant-step, but only a small memory requirement.
- There exists optimised versions of the original algo, such as using the collision-free truncated lookup tables or negation maps and Montgomery's simultaneous modular inversions.