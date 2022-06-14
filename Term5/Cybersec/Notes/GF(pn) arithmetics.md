---
aliases: 
tags:50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]

## $GF(p^n)$ arithmetics
- Recall that order of a [[Galois Field|finite field]] can only be $p$ or $p^n$ for a prime $p$
For a [[Galois Field|finite field]] $GF(p^n)$, we have $|GF(p^n)| = p^n$

The **characteristic** of a [[Field]] is the *smallest positive integer* such that
$$\underbrace{1 + 1 + \dots + 1}_{k} = 0$$
where $1$ is multiplicative [[Identity]], $0$ is the additive [[Identity]]

For $GF(p^n)$, **characteristic** is $p$.

## $GF(2)$ arithmetics
Different to integer arithmetics.

Addition: XOR
| +   | 0   | 1   |
| --- | --- | --- |
| 0   | 0   | 1   |
| 1   | 1   | 0    |

Multiplication: AND
| *   | 0   | 1   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 1   | 0   | 1   |

## $GF(2^8)$ arithmetics
- Elements of $GF(2^8)$ are coefficients of the [[Polynomial]] of degree 7.
- Coefficients are in $GF(2)$

**Addition and subtraction** of [[Polynomial]]s:
$$P(x) + P'(x) = (a_7 + a'_7)x^7 + (a_6 + a'_6) x^6 + \dots + (a_0 + a'_0)$$
Both are bit-wise XORing of the coefficients

## $GF(2^n)$ arithmetics
- All elements are [[Polynomial]]s of degree $<n$
- **Multiplication** follows textbook.
- Then take modulo $P(x)$ where $P(x)$ is a reduction polynomial
	- $P(x)$ is irreducible and of degree $n$
	- So the result is within the [[Field]]

Assume **multiplication** result is $A(x)$.
After reduction, it becomes $R(x)$, where
$$A(x) = B(x) * P(x) + R(x)$$

Match coefficient to bit.