---
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

## Set up for universal hashing
You are creating a [[Hash Table]] `A` with the help of Bob.
Bob knows your [[Hash functions|hash function]], and he sends you pointers to objects that you would be interested to insert.
Bob is secretly malicious, and he chooses numerous objects with key values that hash to the same few slots.
For the final `A` obtained, any [[Hash Operations]] you run seems to be running at worst-case complexity.
You are not aware of Bob's malicious action.

Note: Bob can be malicious because he knows your [[Hash functions|hash function]].
Question: **What can you do to avoid this worst-case complexity**?

## Universal Hashing
Idea:
Use a class of [[Designing hash functions|carefully designed]] [[Hash functions]].
Each time you need to generate a hash value, **randomly choose** a [[Hash functions|hash function]] from this class to generate your hash value.

Note: a [[Hash functions|hash function]] is by definition deterministic. For a given input, the same hash value is always generated.

> Let $\mathcal{H}$ be a collection of [[Hash functions]], each of whihc maps to $\set{0,1,...,m-1}$.
> We say that $\mathcal{H}$ is **universal** if for every fixed pair of key values $k$ and $k'$, with $k\not=k'$, the number of functions that cause [[Intro to hashing|collisions]] on this pair is bounded by
> $$|\set{h\in \mathcal{H}: h(k) = h(k')}|\leq \dfrac{|\mathcal{H}|}{m}$$

> Theorem: If a [[Hash functions|hash function]] $h$ is chosen uniformly at random from a universal collection of [[Hash functions|hash functions]], then insertion has average case complexity $O(1+\alpha)$, where $\alpha$ is the [[Hash Operations|load factor]].

This average case complexity is the same as in the case that the [[Designing hash functions|simple uniform hashing]] assumption is satisfied.

It is in general easier to design a universal collection of [[Hash functions|hash functions]], than to [[Designing hash functions|design a hash function]] that satisfies the [[Designing hash functions|simple uniform hashing]] assumption.