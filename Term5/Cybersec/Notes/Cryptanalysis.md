---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## Goal & principle
Researchers try to break hash functions in 1 of 2 ways:
Two potential goals:
- Find [[Cryptographic properties for hash functions|preimages]]: finding the message that creates the digest of all 0s or all 1s
- Find [[Intro to hashing|collisions]]: finding 2 messages (usually single message blocks) that hash to the same digest

Collisions are much easier to find but less useful.

> If $f$ is **collision resistant**, then $H$ is **collision resistant**.

Try brute force?

### How many attempts before you can find a collision, for a hash function with $n$-bit outputs?
***
- $m$ balls are assigned to $n$ bins randomly 
- What is the probability of collisions (2 balls in same bin?)

How many ways to arrange $m$ balls into unique bins?
$$n \cdot (n-1) \cdot (\dots) \cdot n-m + 1)$$
How many ways to arrange $m$ balls into $n$ bins? 
$$n^m$$
Let $Pr(A)$ be probability of no collision
$$
\begin{align}
Pr(A) &= \dfrac{n(n-1)\cdots(n-m+1)}{n^m}\\
&= \left( 1 - \frac{1}{n}\right) \cdot \left( 1 - \frac{2}{n} \right) \cdot \cdots \cdot \left(1-\frac{n-1}{n}\right)
\end{align}
$$
Take logs on both sides, and since$\ln{(1-x)} \approx -x$ for small $x$, 
$$
\begin{align}
\ln{(Pr(A))} &= \ln\left( 1 - \frac{1}{n}\right) + \ln\left( 1 - \frac{2}{n} \right) + \cdots + \ln\left(1-\frac{n-1}{n}\right)\\
&\approx -\frac{1}{n} - \frac{2}{n} - \dots - \frac{m-1}{n} \\
&\approx - \frac{m^2}{2n} \\
Pr(A) &\approx e^{-\dfrac{m^2}{2n}}
\end{align}
$$
$$
\begin{align}
\text{Probability of collision} &=
1 - Pr(A)\\
\text{If we want }Pr(A) \leq a, \\
-\frac{m^2}{2n} &\leq \ln{(a)}
\end{align}
$$

### Birthday Paradox
How many people in the room so that prob of 2 ppl having same birthday is at least 0.5?
- $\# bins = 356$ , $a = 0.5$
$$\begin{align}
-\frac{m^2}{2 \cdot 2^n} &\leq \ln 0.5 \\ 
m &\geq \sqrt{(2\ln2)2^n} \\
&\approx 1.177 \sqrt{2^n}
\end{align}$$
Or, with $O(2^{n/2})$ random hash values, the chance of hash collision more than 50% 


## How to use this for an attack
Collisions can be directly used to attack
- [[Commitment scheme]]
- [[Digital signature scheme]]
- [[TLS certificate]] (more on them later, breaks TLS)

Attacks have been demonstrated for [[MD5]] (precursor of SHA-1) and [[SHA-1]].

Birthday paradox does not help finding [[Cryptographic properties for hash functions|second preimages]]

## Current state of hash functions
- Collisions and preimages can be found for MD4
- Collisions can be constructed for [[MD5]] and SHA-0
- Theoretic collisions discovered for [[SHA-1]]
- SHA-256 and SHA-512 has no known attacks

## [[Cryptanalysis]] of [[SHA-1]]
2005
- Collisions found in $2^{69}$ steps instead of $2_{80}$, factor of 2048

2009
- That result was claimed to be improved to $2^{52}$ steps (but found to be incorrect)

Assuming $2^{60}$ tries, and $2^{14}$ CPU cycles per SHA-1, breaking it will cost:
- $700K in 2015
- $173K in 2018
- $43K in 2021

2017
Google found collisions in $2^{63}$ tries

GPU can help
