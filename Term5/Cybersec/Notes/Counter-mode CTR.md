---
aliases: CTR
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
![[Pasted image 20220617092411.png]]

- Use [[AES]] to (pre)compute key stream of $80 * 128$  bits
	- $k$: key, [[Initialisation vector|IV]] + counter: "message"
	- For next round, same key, but incremented counter
	- So for first block, input to [[AES]] is $k$ and [[Initialisation vector|IV]]
	- Second block, $k$ and [[Initialisation vector|IV]] + 1, etc
- Use key stream to $\oplus$ with data
- Decryption is done the same way
- **Can be parallelized**
