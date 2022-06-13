---
aliases: CBC
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
![[Pasted image 20220613083921.png]]
Each block of plaintext is XORed with the previous ciphertext block before being encrypted. This way, each ciphertext block depends on all plaintext blocks processed up to that point.

Ideas:
1. Encryption of all blocks are "chained together" such that the ciphertext $y_i$ does not depend only on block $x_i$ but on all previous plaintext blocks as well
2. Encryption is randomised by using an [[Initialisation vector]]. 

![[Pasted image 20220608181151.png]]

![[A7F9CD13-8578-419F-9E0A-69EE34FB0FC7.jpeg]]

If first block has index 1,
$$
\begin{align}
C_i &= E_K(P_i \oplus C_{i-1}) &\text{for } i=1, \dots, k\\
C_0 &= IV\\
\\
P_i &= D_K(C_i) \oplus C_{i-1} &\text{for } i=1, \dots, k\\
C_0 &= IV\\
\end{align}
$$
The ciphertext $y_i$ is fed back to the cipher input and XORed with the succeeding plaintext block $x_{i+1}$. This XOR sum is then encrypted, yielding the next ciphertext $y_{i+1}$, which then can be used to encrypt $x_{i+2}$, and so on. 

An [[Initialisation vector]] is added to the first plaintext, which allows us to make each CBC encryption [[Non-deterministic algos|non-deterministic]].  For the first plaintext block $x_1$, there is no previous ciphertext. For this, an [[Initialisation vector|IV]] is added to the first plaintext, which also allows us to make each CBC encryption [[Non-deterministic algos|non-deterministic]].

The first ciphertext $y_1$ depends on plaintext $x_1$ (and the [[Initialisation vector|IV]]), second ciphertext depends on [[Initialisation vector|IV]], $x_2$ and $x_1$, and so on. The last ciphertext is a function of all plaintext blocks and the [[Initialisation vector|IV]].

When decrypting a block $y_i$, we reverse the 2 operations on the encryption side. First reverse the block cipher encryption by applying the decryption function $e^{-1}()$. Then undo the XOR by XORing the correct ciphertext block. This can be expressed for general bocks $y_i$ as
$$e_k^{-1}(y_i) = x_i \oplus y_{i-1}$$
If first ciphertext $y_1$ is decrypted, the result must be XORed with the [[Initialisation vector|IV]] to determine the plaintext block $x_1$, i.e.
$$x_1 = IV \oplus e_k^{-1}(y_1)$$
Hence:
> Let $e()$ be a [[Block ciphers]] of block size $b$; let $x_i$ and $y_i$ be bit strings of length $b$; and [[Initialisation vector|IV]] be a [[nonce]] of length $b$.
> > Encryption
> > $$\begin{align}y_1&=e_k(x_1 \oplus IV)\\y_i&=e_k(x_i\oplus y_{i-1}), &i\geq2\end{align}$$
> 
> > Decryption
> > $$\begin{align}x_1&=e_k^{-1}(y_1) \oplus IV\\x_i&=e_k^{-1}(y_i)\oplus y_{i-1}, &i\geq2\end{align}$$

## Properties
- [[AES]] itself will encrypt the messages
- Use ciphertext to mask next encryption to make encryption unpredictable
- Input block $m_i$ is XORed with $c_{i-1}$ before encryption
- [[Initialisation vector]] is random and non-secret [[nonce]]
- Parallel encryption not possible

## 
