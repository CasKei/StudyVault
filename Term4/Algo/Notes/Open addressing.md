---
aliases: probing
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

[[Intro to hashing#Collisions in hashing|Recall collisions]]

Chaining is not the only method for [[Intro to hashing#Collisions in hashing|collision]] resolution! Another method: open addressing.

## Idea
Instead of having a [[Arrays and Linked Lists|LL]] in every slot of the [[Hash Table]] `A`, possibly with many elements, we constrain every slot of `A` to have at most one element.

Whenever the insertion of a new element `x` into `A` would cause a [[Intro to hashing|collision]], find a different empty slot to insert `x`.

> Open addressing: a systematic method for finding the next available empty slot to insert any element that would otherwise cause a [[Intro to hashing|collision]]

Note: Since every slot has $\leq 1$ element, the [[Hash Operations|load factor]] of such a [[Hash Table]] cannot exceed 1.
i.e. $\alpha \not > 1$.

## What happens
**Goal: insert a new element `x` into [[Hash Table]] `A` with $m$ slots**

Let $q$ be the hash value of `x.key`, and suppose slot $q$ is already occupied by another element.
We cannot insert `x` into `A[q]`, otherwise there will be a [[Intro to hashing|collision]].

> Probing: the process of finding another available empty slot.
> We probe the [[Hash Table]] until we find an empty slot where we can insert `x`.

> Probe sequence:
> Generate a **permutation** $(i_1, \dots, i_m)$ of $(0, \dots, m-1)$.
> The sequence $(i_1, \dots, i_m)$ is called a probe sequence.
> It depends on the key value.
> Different key values generate different probe sequences.

To insert a new element `x`, try to insert `x` into slots $i_1, \dots, i_m$ one by one in this order, until insertion is successful.

## Comparison with normal [[Hash functions|hash function]]

| Open addressing                                                                                                                                     | Normal hash                                                                                                                                                        |  
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | 
| Insert a new element `x` into `A` based on probe sequence associated to its key value $k$                                                           | Insert `x` into slot $h(k)$, where $h$ is the [[Hash functions\|hash function]] of `A`. Usually gives us only one slot number and tells us which slot to insert to |     
| Require the [[Hash functions]] to give us a sequence of slot numbers: $h(k,0), h(k,1),\dots,h(k,m-1)$. This is the probe sequence associated to $k$ | [[Hash functions\|hash function]] only gives a single hash value                                                                                                   |     

## Linear probing
> Let `A` be a [[Hash Table]] with $m$ slots.
> Let $K=\set{\text{all possible key values}}$.

> Start with an auxiliary [[Hash functions|hash function]] $h': K \to \set{0,1,\dots, m'-1}$.
> Then define $h(k,i) = (h'(k) + i) \text{ mod } m$.

Example: $𝑚 = 𝑚' = 10$, $ℎ'(𝑘) = (𝑘 \text{ mod }10)$.

## Quadratic probing
> Let `A` be a [[Hash Table]] with $m$ slots.
> Let $K=\set{\text{all possible key values}}$.

> Start with an auxiliary [[Hash functions|hash function]] $h': K \to \set{0,1,\dots, m'-1}$.
> Then define $h(k,i) = (h'(k) + c_1i + c_2i^2) \text{ mod } m$.

## Double hashing
> Let `A` be a [[Hash Table]] with $m$ slots.
> Let $K=\set{\text{all possible key values}}$.

> Use 2 auxiliary [[Hash functions|hash function]] 
> $h_1: K \to \set{0,1,\dots, m_1-1}$ and 
> $h_2: K \to \set{0,1,\dots, m_2-1}$
> Then define $h(k,i) = (h_1(k) + ih_2(k)) \text{ mod } m$.