---
aliases: hard
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Hardness
Suppose B is a problem you think is [[Tractable vs Intractable|intractable]].
To convince others that B is indeed intractable, you need more evidence
- find a [[Polynomial-time reductions]] of some well studied A to B such that no known solution A runs in [[Polynomial time]], then your reduction is strong evidence that B is indeed intractable.

Intuition
$A\leq_p B$ means that B is at least as hard as A, so if everyone found A intractable, then B is likely also intractable.

## NP hard
>B is NP-hard if every problem in A [[NP problems|in NP]] has a [[Polynomial-time reductions]] to B.

A [[Non-deterministic algos|deterministic]] algorithmic solution for B can be used as a subroutine to solve every problem in NP deterministically.
![[Pasted image 20220508154528.png]]
Intuition:
If we can find a deterministic algorithm solution for B that runs in [[Polynomial time]], then this solution can be used to design a polynomial time algorithmic solution for every problem in NP. Hence solving NP-hard problems should be hard.