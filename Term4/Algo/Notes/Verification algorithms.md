---
aliases: certificate
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

[[Decision problem]]: Decide if input $I$ satisfies a set of conditions.

How do we verify an answer to the [[Decision problem]]?

> An algorithm to verify an answer is called a verification algorithm.

We can have 2 verification algorithms
- Verify that a yes answer is correct
- Verify that a no answer is correct

A verification takes in **2 inputs** $I$ and $E$.
$I$: the given input to the [[Decision problem]]
$E$: evidence that we provide to the algorithm
- If $E$ is sufficient evidence, then algo outputs 1 ("accept") and we say $E$ is a ==**certificate** for the verification algo==
- If $E$ is insufficient evidence, then algo outputs 0 ("reject")

