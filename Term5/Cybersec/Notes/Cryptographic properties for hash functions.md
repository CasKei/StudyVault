---
aliases: preimage resistance, second preimage resistance, collision resistance, random oracle, cryptographic hash function
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## Preimage Resistance
AKA: One-way property
> Given $y=f(x)$,
> It is hard to find the input $x$ that produces $y$.

Hard to invert. Given an element in the range of a hash function, it should be computationally infeasible to find an input that maps to that element.

## Second preimage resistance
AKA: Weak collision resistance
> Given $x$ and $f$,
> It is hard to find $x' \not= x$ such that $f(x) = f(x')$

It is computationally infeasible to find any second input which has the same output as any specified input.

## Collision resistance
[[Intro to hashing|collisions]]
AKA: Strong collision resistance
> Given $f$,
> It is hard to find any two inputs $x' \not = x$ such that $f(x) = f(x')$

It is computationally infeasible to find any two distinct inputs which hash to the same output.

## Random Oracle Property
> Each unique input is mapped to random output with uniform distribution.

Informally, for 2 correlated inputs $m_1$ and $m_2$, the output of $f$ is completely uncorrelated.

## Thinking
Does Cyclic Redundancy Code (CRC) have these?
Given a CRC, can compute an input that generates it.

## Design
Cryptographic hash functions are designed to have all 4 properties.

Using cryptographic hash functions, **message authentication codes** can be constructed.

We now discuss special algorithms, similar goals can be achieved with [[Block ciphers]].

[[Merkle-Damgard construction]]