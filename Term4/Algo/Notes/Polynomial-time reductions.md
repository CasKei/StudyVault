---
aliases: reduction
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Key idea
Given a Problem A that we want to solve, and suppose there is another Problem B that we already know to solve.

Suppose we can reformulate Problem A to “look like” Problem B, so that by starting with a solution to Problem B, we are able to solve Problem A.

This reformulation could be as simple as a change in notation, or it could be an algorithmic process to use computed solutions to Problem B, do further computations, so as to generate one or more solutions to Problem A.

Then we say that we have reduced Problem A to Problem B.

## How do reductions work
Assume we have 2 problems A and B.
- A: we want to design an algo to solve it
- B: we already know an algo to solve it

![[Pasted image 20220508145639.png]]

- $F$: an algo that transforms an input for A into an input for B
- $F^{-1}$: an algo that transforms a solution to B into a solution to A

Using $F$ and $F^{-1}$, we have reduced A to B.

## Example
[[Partition problem]] can be reduced to [[Knapsack problem]].
[[Partition problem#Reduction]]

## Polynomial-time reductions
> If both algorithms $F$ and $F^{-1}$ run in [[Polynomial time]], then we say that the reduction of A to B is a **polynomial-time reduction**.

If there is a polynomial-time reduction of A to a known [[Tractable vs Intractable|tractable]] problem B, then A is also [[Tractable vs Intractable|tractable]] ([[Polynomial time|in P]])

$$A \leq_p B$$
There is a polynomial-time reduction from A to B
If $A \leq_p B$ and $B \leq_p A$, then
$$A \cong_p B$$
## Consequences
If $A \leq_p B$,
- If B [[Polynomial time|in P]], then A also [[Polynomial time|in P]].
- If A not [[Polynomial time|in P]], then B also not [[Polynomial time|in P]].
- If we believe A is [[Tractable vs Intractable|intractable]], then we should also believe that B is also [[Tractable vs Intractable|intractable]].

Intuition:
$A \leq_p B$ means that B is "at least as [[NP-hard|hard]] as" A.
