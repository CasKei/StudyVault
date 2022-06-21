---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]

https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#Description
A type of [[Dynamic key establishment]].
## Setting
Alice and Bob want to establish shared key
- Can only communicate over public channel
- Both can do maths
- Attacker is *passive eavesdropper* (Can't do anything else)

How to agree on key without attacker learning it?

Some public parameters:
- Large prime $p$
- Some integer $g$

## Diffie-Hellman key exchange
![[Pasted image 20220620084140.png]]
- Each creates a random private number $a$ (resp. $b$)
- Publicly announces $g^a \text{ mod } p$ (resp. $g^b \text{ mod } p$)
- Alice computes $X = (g^b)^a \text{ mod } p$
- Bob computes $Y = (g^a)^b \text{ mod } p$
- Both end up with same value: $X = Y = g^{ab} \text{ mod }p$
	- This is now their shared key
	- Attacker cannot compute $g^{ab}$ from $g, p, g^a, g^b$.

Why is this secure? [[Discrete logarithm problem]].