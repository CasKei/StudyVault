---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## History
In Oct 2012, Keccak was selected as [[SHA-3]] algorithm.
- Focus on security and implementation speed

## What
SHA-3 (Keccak) is fundamentally different to [[SHA-1]]/[[SHA-2]]

"Sponge" construction instead of [[Merkle-Damgard construction|MD]]:
- Absorbing, squeezing

Block of $b=r+c$ bits

- $r$ bits of message are "fed" into the state per round
- $r$ bits of output per round can be taken out afterwards

![[Pasted image 20220522193139.png]]