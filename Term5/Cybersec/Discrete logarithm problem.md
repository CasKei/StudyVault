---
aliases: DLP
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]

## Discrete Logarithm Problem
Why is [[Diffie-Hellman key exchange]] secure?
- Attacker cannot find $a$ from $g^a \text{ mod }p$

This is called the DLP.
> Given a finite cyclic [[Group]] $G$ of order $p-1$ and an element $r$, and a (multiplicative) generator element $g$ :
> - Find $1 \leq x \leq p-1$, such that $$g^x \equiv r \text{ mod } p$$
> > Also written as
> > $$x = \log_gr \text{ mod } p$$

## Brute Force
Keep multiplying generator element until reaching $r$
$$r = \underbrace{g * g * \dots * g}_x \text{ mod } p$$
Expensive, $O(p)$

## Better Algorithms
- [[Shank's Baby-Step-Giant-Step]]
- [[Pollard's Rho]]
- [[Pohlig-Hellman]]
	- Runtime is only as big as the largest factor of $p-1$
- [[SAGE]] contains all these implementations

## Where is the DLP Used?
- DLP is (very) hard in some well-chosen [[Group]]s.
- Core of many cryptographic schemes
- Examples of well-chosen finite cyclic groups:
	- The original [[Diffie-Hellman key exchange]]: $\mathbb{Z}_p$
	- [[Elgamal encryption]] and the [[Digital signature scheme]] algorithm uses $\mathbb{Z}_p$
	- [[Elliptic curve cryptography]] uses a [[Group]] defined by elliptic curve equations
