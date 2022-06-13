---
aliases: RainbowCrack
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Passwords]]
[[Attacking password storage]]
[[Hash chain]]

## What
![[Pasted image 20220602114249.png]]

> A rainbow table consists of $m$ [[Hash chain]]s of length $t$.

For each chain, only the first input (plaintext) $I_1$ and the last hash $O_t$ are stored

Overall space requirement:
$$(|I| + |O|) \cdot m$$
Even more efficient: each chain uses its index as starting input.

Product $m \cdot t$ must be $\geq$ the number of possible input values

Runtime of lookup:
$O(t)$ if comparisons are free and hashing is the only expensive operation.

## Operation
Example:
> Given $Y$, we want to find $X$ such that $Y = H(X)$

Check if $Y$ is in the list of last chain elements.
- If $Y=O_z$, regenerage chain $z$ using input value $I_z$, then $X=I_t$ that is hashed to $O_z$
- If not, compute $H(R(Y))$, then
	- Use $Y$ to find matches in the chain's last elements
		- If found, regenerate chain and found input $X$
		- If not found, repeat again with $Y=H(R(Y))$

### Analysis
Estimated effort:
- $\dfrac{t}{2}$ reductions to find matching last element
- $\dfrac{t}{2}$ to regenerate chain

## RainbowCrack
> Rainbow tables can be generated using RainbowCrack tool for [[MD5]], [[SHA-1]], etc.

Having too much time? Open a commercial rainbow table:
- https://www.cloudcracker.com/ (was still working in 2017)
- $17 per hash lookup

## Defending against rainbow tables
> To make it harder, add a salt (random number) to each input.

salt $s$:
$$x = H(m||s)$$
$(x,s)$ can be stored in the password file.

- $s$ should differ per user
- Attacker cannot just use the same rainbow table
- $n$ bit salt increases attack effort by $2^n$
	- each salt requires own rainbow table of same size as original

Some say rainbow tables are dead...

So [[Hashcat]]?