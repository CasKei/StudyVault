---
aliases: 
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Problem
> Is $P=NP$?

Technicality: To have a fair comparison, the input size of problems in P should be in terms of the number of bits used to store the input, just like in the case of NP.

## Fact
$$P\subseteq NP$$
For any problem [[Polynomial time|in P]], there is by definition a [[Polynomial time]] algorithm to solve the problem, so we can use the solution to [[Verification algorithms|verify]] any certificate for a "yes" answer to the "converted" [[Decision problem]].

## Cases
$$P \not = NP$$
Comsequence:
[[NP-complete]] problems are indeed [[Tractable vs Intractable|intractable]]

Solving hard problems is harder than verifying solutions to hard problems

$$P=NP$$
All seemingly hard problems actually have relatively easy solutions that hvae eluded humans for decades.

Implies efficient solutions for all [[NP-complete]] problems.
Cryptographic hashing will no longer be secure.

