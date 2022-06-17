---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
![[Pasted image 20220617092430.png]]

- Use [[AES]] to (pre)compute key stream of $80 * 128$  bits
	- $k$: key, [[Initialisation vector|IV]]: "message"
	- For next round, [[Initialisation vector|IV]] is the **ciphertext block** of pevious round
- Use key stream to $\oplus$ with data
- Decryption is done the same way