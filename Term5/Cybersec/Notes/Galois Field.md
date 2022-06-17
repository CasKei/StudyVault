---
aliases: GF, finite field
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Modular Arithmetic]]
[[Field]]

## Definition
> A [[Field]] with a finite order (number of elements).

Order of any finite field: always a prime or a power of prime.
- $p$ where $p$ is a prime
- or $p^n$ where $p$ is a prime and $n>1$

For each prime power $q = p^r$, there exists exactly one finite field with $q$ elements. 
-   This field is denoted $GF(q)$, and the prime field of GF(q) is GF(p).
Written as $GF(p)$ or $GF(p^n)$
> A field is called a prime field if it has no proper (i.e., strictly smaller) subfields. Every non-prime field contains a prime field.

> $p$ is called the **characteristic** of the field.

## Example
$$GF(p)$$
- $p$ is prime
- Operation: $+, *$
- In $GF(2)$, + is XOR, * is AND

## See
[[Extension field]]

