---
aliases: 
tags:50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]

https://en.wikipedia.org/wiki/Multiplicative_inverse
**Division**
$$\dfrac{A(x)}{B(x)} = A(x) * B(x)^{-1} \text{ mod } P(x)$$
Example: S-box of [[AES]]

## S-box in [[AES]]
Each substitution box:
- Take 8-bit inputs
- Produce 8-bit outputs
	1. Compute the [[Multiplicative Inverse]] of input in $GF(2^8)$
	2. Using $P(x) = x^8 + x^4 + x^3 + x + 1$
	3. Then apply [[Affine mapping]] in $GF(2)$
The inversion is non-linear, and mapping adds additional distortion.

## Affline mapping
[[Affine mapping]]

## Computation
Multiplicative inverse: given $a$, find $b$ such that $a*b=1$
For a [[Galois Field|finite field]], multiplicativve inverse **must exist** (for all but the 0 element)
How to compute $b$?

### Brute force
- Try all possible elements
- How many attempts?
- no

### Euler's theorem
> For a prime $p$ and any $a$
> $$a^{p-1} \equiv 1 \text{ mod } p$$

For a [[Field]] $GF(p)$ and element $a$:
$$a^{-1} = a^{p-2} \text{ mod } p$$
How to quickly compute $a^{p-2} \text{ mod }p$ for large $p$?

### Euclid's algorithm
$gcd(a,b)$
Input: $a,b \in \mathbb{Z}$
Output: $d = gcd(a,b)$

```php
if b = 0:
	return a
else:
	return gcd(b, a mod b)
```

### Bezout's lemma
> For any integer $a,b$, there exists $s, t$ such that
> $$gcd(a,b) = as + bt$$

- Given $GF(p)$ and element $a$
- $gcd(p,a) = xp + ya = 1$
- OR
- $ya = 1 - xp = 1 \text{ mod } p$
- So, given $p,a$ if we can compute $x,y$ then $y$ is the multiplicative inverse of $a$ in $GF(p)$

### Extended Euclid's Algorithm
Input: $a,b \in \mathbb{Z}$
Output: $d,x,y$ with $d=gcd(a,b)$, $ax+by=d$

```php
if b|a:
	return b, 0, 1
else:
	compute a = qb + r
	d, x, y = egcd(b, r)  // (xb + yr = d)
	return (d, y, x - yq)
```

## Examples
- Consider $GF(17)$, what is inverse of 2?
$$\begin{align}egcd(17,2)\\
a = 8(2) + 1\\
d, x, y = egcd(2, 1)\\
return (d, y, x-yq) = 2, 0, 1\\
\\

\end{align}$$
- Consider $GF(2^4)$ with reduction polynomical $P(x) = x^4 + x + 1$. What is the inverse of $x^3 + x^2 + 1$?
$$\begin{align}&egcd(x^4 + x + 1 , x^3 + x^2 + 1)\\
&\text{Long division:}\\
&\underbrace{x^4 + x + 1}_{a} = \underbrace{(x+1)}_q \underbrace{(x^3+x^2+1)}_b + \underbrace{x^2}_r\\
&d, x, y = ecgd(x^3 + x^2 + 1 , x^2) &= 1, 1, -(x+1)\\
&return (d, y, x-yq) &=  1, -(x+1), 1 - (x+1)(x+1)\\
&&= 1 , -(x+1), 1 - (x+1)^2
\\
&ecgd(x^3 + x^2 + 1 , x^2)\\
&\text{Long division:}\\
&\underbrace{x^3 + x^2 + 1}_a = \underbrace{(x + 1)}_q \underbrace{(x^2)}_b + \underbrace{1}_r \\
&d, x, y = egcd(x^2 , 1) &= 1, 0, 1\\
&return (d, y, x-yq) &= 1, 1, -(x+1)
\\
&&\text{recursion backtrack}\\
&d, x, y = 1, -(x+1), 1-(x+1)^2\\
&y = 1-(x+1)^2 = x^2 + 2x + 2\\
&= x^2 \text{ (since binary (remove all 2))}
\end{align}$$