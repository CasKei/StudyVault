---
aliases: halting problem
tags: 50.004
---
[[Algo]]
[[Algo week 12]]

## Unsolvable problems
Famous example: halting problem.
There are way more unsolvable problems than solvable problems.

## The Halting Problem
[[Turing Machine and Programmability#Uncomputable Function Halting Problem|Uncomputable function, halting problem]]

Given a computer program $P$ and some input $I$, determine whether $P$ will terminate when executed with input $I$.

This is a yes/no problem : [[Decision problem]]
Yes if $P$ terminates
No if $P$ runs forever.

If $I$ is not a valid input for $P$, then $P$ executed with input $I$ will terminate with an error message.

Suppose the halting problem can be solved, i.e. there exists an algorithm `halt(P,I)` that takes in any program `P` and any input `I`, and gives an output either true or false.
- True: yes program terminates on `I`
- False: no program does not terminate on `I`.

### Why unsolvable
Consider
```python
def funny(P):
	if halt(P,P):
		loop_forever()
```

What is the output of `funny(funny)`?
```php
if halt(funny,funny):
	loop_forever()
```
If `halt(funny,funny)` True:
- when running `funny(funny)`, we enter the loop and loop forever
- by definition of `halt`, we conclude `halt(funny,funny)` False.

If `halt(funny,funny)` False:
- when running `funny(funny)`, we don't enter the loop and halt
- by definition of `halt`, we conclude `halt(funny,funny)` True.

![[Pasted image 20220508104034.png]]