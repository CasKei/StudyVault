---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hashing applications]]

## Attack
- Attacker wants Alice to sign a $m$ text of his choice
- Attacker wants Alice to believe she signed a harmless text $t$
- Attacker generates $n$ different variations $m_i$ , $t_j$ of $m$ and $t$
- If there is one collision between $m_i$ and $t_j$, attack is successful
	- Alice checks $t_j$ and signs the harmless text
	- The signature is also valid for $m_i$, as it has the same hash!