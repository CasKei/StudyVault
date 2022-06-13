---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Algo Hash functions]]

## Applications for [[Cryptographic hashing]]
[[Hash functions]] provide an interesting **one-way** function on data.

Ideally, the hash value does not reveal any information about input.

Can be used for:
- [[Commitment scheme]]: salt or padding required
	- [[Cryptographic padding]]
- [[Message authentication code]] (Message integrity protection and authentication) : e.g. HMAC: careful with $k$
- [[Storage of secrets]] : salt required
- Other attacks on hashes
	- [[Yuval's square root attack]]
	- [[MD5 collisions]]

