---
aliases: ECB
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
- Break big message into blocks
- Apply block cipher individually to each block

![[Pasted image 20220608111159.png]]
![[Pasted image 20220608111210.png]]

$$
\begin{align}
C_i &= E(K, P_i) &\text{for } i=1, \dots, k\\
P_i &= E^{-1}(K,C_i) = E^{-1}(K, E(K,P_i)) &\text{for } i=1, \dots, k
\end{align}
$$

## Problem
**If 2 plaintext blocks are the same, then with fixed key, the corresponding ciphertext blocks are identical**, and that is visible to the attacker.
^ **Lack of [[Block ciphers|diffusion]]**: does not hide data patterns well.

If 2 occurrences of the same string happen to line up on a block boundary, then a plaintext block value will be repeated.

In most Unicode strings,every other byte is a 0, which greatly increases the chance of a repeated block value. Many file formats will have large blocks of only 0s, which result in repeated block values.
***
Assume $P$ is encrypted with AES-ECB, and ciphertext is $C$:
$$P = \text{SUTD-ISTD-50.042*Foundations-CS*}$$
Swap the 2 blocks of $C$ to form a new ciphertext $C_1$, what is the new plaintext $P_1$ that corresponds to $C_1$?

Change the last bit of $C$ to form another ciphertext $C_2$, what is the plaintext $P_2$ that corresponds to $C_2$?
***


## Solution
Introduce some form of randomness, typically in the form of an [[Initialisation vector]].
You are allowed to exchange 128 bit $n$ [[nonce]] value over a public channel.
- Use $n \oplus k$ to randomise things
- $n$ should change often but can be public
