---
aliases: NP, in NP
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## What
> A [[Decision problem]] is said to be in class NP if there is at lest 1 [[Non-deterministic algos|non-deterministic]] algorithm that is able to verify a "yes" answer to the [[Decision problem]], such that in the best case scenario, this [[Non-deterministic algos|non-deterministic]] algorithm runs in [[Polynomial time]].

$$
NP \approx \text{solvable in non-deterministic polynomial time}
$$
$$
\text{"problem in NP"}=\text{"problem in class NP"}=\text{"NP problem"}
$$

> A [[Decision problem]] is in NP if for every input whose corresponding correct answer should be "yes", there is a [[Verification algorithms|certificate]] for a "yes" answer that can be verified in [[Polynomial time]].

### Note
NP does not say anything about the verifcation of a "no" answer, is onl concerned for the verification of a "yes" answer.

Problem can be in NP and still potentially take a "very long time" to verify a "no" answer.
So it is possible that even in the best scenario (first guess is a certificate), with a theoretically "best" verification algorithm, the verification of a "no" anser still does not complete in [[Polynomial time]].

## Intuition for NP
We say the [[Decision problem]] is in NP if we can guess a [[Verification algorithms|certificate]] for a "yes", such that it takes [[Polynomial time]] to verify that the guess indeed certifies the correct answer should be "yes".

Guessing is a [[Non-deterministic algos|non-deterministic]] process.
We can verify a "yes" answer [[Non-deterministic algos|non-deterministically]] in [[Polynomial time]].

By considering “polynomial time” in terms of the number of bits required to store the input, the class NP becomes much more general and includes many interesting decision problems.

## Example
[[Partition problem]]
![[Pasted image 20220508141701.png]]

## NP for non decision problems
Any computational problem can be "converted" to a [[Decision problem]].

General definition: we say that a problem is in NP if its "converted" decision problem is in NP.
