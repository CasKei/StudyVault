---
aliases: mod operation, mod
tags:50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]

## History
In the past we only have symmetric crypto, but after the 1970s, public-key cryptography made this math more important.

This stuff is Abstract Algebra.
***
Where is this used?
- S-Box in [[AES]]
- MixColumns in [[AES]]
- XOR or + for [[Stream ciphers|One-Time Pad]]
- [[RSA]]
***
Why is modular arithmetic needed?
- Important part of number theory
- Computing resources are finite
	- Integers have limited number of bits
	- Go over the range --> wrap around
- Example: [[Substitution ciphers|Caesar's cipher]]
	- $c_i = (p_i + k)\ mod\ 26$
***
## Mod operation
Example: $8\%5 = 3$
- 3 is the remainder of 8 mod 5

**Congruence:** $3\equiv 8\ mod\ 5$

> $a \equiv b\ mod\ m$ for $a, b, m \in \mathbb{Z}$
> - Remainder of a modulus $m$ is the same as of $b\ mod\ m$
> - Infinitely many solutions to this congruence
> 	- $3 \equiv -2 \equiv -7 \equiv \cdots \equiv 13\ mod\ 5$

## Sets
Remainders are non-negative.
- Remainders modulo $m$ forms a finite set
	- $\mathbb{S} = \set{0,1,2,3,\dots ,m-1}$
- We want to do arithmetics with elements in set $\mathbb{S}$.

Algebraic structure consists of:
- A set of elements
- Operations performed on these elements (e.g. addition, multiplication, etc)

## Algebraic Structures
- [[Group]]
- [[Ring]]
- [[Field]]

[[GF(pn) arithmetics]]
[[Multiplicative Inverse]]
Finite structures are useful for arithmetics on computers. They allow us to translate XOR and similar operators to arithmetics.

## Modular exponentiation?
- There is no "exponentiation" instruction on CPU
- There is no "take modular remainter" instruction on CPU
- An efficient algorithm: square and multiply
> Square and multiply algorithm (MSB first, i.e., bits are read from left to right)
> ```python
> def squAndMult(m, k, n):
> 	res = 1
> 	for i in bin(k)[2:]: # step bitwise through key
> 		res = res * res % n
> 		if (i == '1'):
> 			res = res * m % n
> 	return res
> ```

Example: $5^{23} \text{ mod }11$

### Additional Resources
-   [Galois Fields, Polynomial Algebra and more](https://link.springer.com/content/pdf/bbm%3A978-3-642-54649-5%2F1.pdf)
-   [Modular Arithmetic, lecture by Christof Paar](https://www.youtube.com/watch?v=W1SY6qKZrUk&ab_channel=IntroductiontoCryptographybyChristofPaar)
-   [Introduction to Galois Fields, lecture by Christof Paar](https://www.youtube.com/watch?v=x1v2tX4_dkQ&ab_channel=IntroductiontoCryptographybyChristofPaar)
