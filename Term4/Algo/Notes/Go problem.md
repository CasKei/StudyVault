---
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Problem
Given a configuration of pieces on the Go board, can the white player force a win? Yes or No?

### Closely related problem
Given a configuration of pieces on the Go board, find all possible endgames that can be obtained from the given configuration.

(An endgame configuration is one where there are no more valid moves.)

## To solve
We could first solve the closely related problem:
list all possible endgames, then check which player wins in each endgame.

## To verify
[[Verification algorithms]]
To verify no, just find one endgame where black wins

To verify yes, check that in all possible endgames, white wins.
If $n$ is the number of remaining vacant positions in the given configuration, then the number of suc possible endgames is at least $\Omega(e^n)$.
There are [[Exponential time|exponentially]] many endgames to check.

Even if we already have the list of all endgames, we still need to go through every endgame and check that the white player wins.

It has been proven that any [[Verification algorithms|certificate]] to verify a "yes" answer, no matter how it is encoded, would have a size of at least $\Omega(e^n)$.

Even with any theoretically fastest [[Verification algorithms|verification algorithm]] to verify a yes answer, we still need to process the entire cetificate, so the time complexity for verification must at least be $\Omega(e^n)$.