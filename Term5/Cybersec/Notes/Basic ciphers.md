---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]

## Encryption schemes
- Symmetric encryption schemes
	- What
		- A *single shared key*
			- encrypt and decrypt with same key
			- if it gets out, you'll need another key
		- *Secret key* algorithm
			- a shared secret
		- Doesn't scale very well: can be challenging to distribute
		- Very fast to use
			- less overhead than asymmetric encryption
			- often combined with asymmetric encryption
	- Examples
		-  [[Substitution ciphers]]
			- [[Substitution ciphers|Caesar's cipher]]
			- [[Substitution ciphers|Vigenere cipher]]
		- [[Stream ciphers]]
		- [[Block ciphers]]
- Asymmetric encryption scheme
	- What
		- Also called public key cryptography
		- Private key: keep this private
		- Public key: anyone can see this. Give it away.
		- The private key is the only key that can decrypt data encrypted with the public key: you cannot derive the private key from the public key
		- Key generation
			- build both the public and private key at the same time
			- Lots of randomisation, prime numbers, math
			- Everyone can have the public key, but only authorised have private key
	- Examples
		- [[RSA]]
		- [[Elliptic curve cryptography]] (if have time)
			- instead of numbers, use curves
			- smaller keys than non-ECC asymmetric encryption
			- smaller storage and transmission requirements
			- perfect for mobile devices


[[Transposition ciphers]]
[[Binary representation]]
[[Modern ciphers]]