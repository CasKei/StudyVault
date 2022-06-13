---
aliases: iterative hash function, MD construction
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## Design
![[Pasted image 20220522140241.png]]
Construction, where $M = m_1 || m_2 || \dots || m_n$
$$
\begin{align}
H(M) := \begin{cases}
H_0 &= g(IV, m_1)\\
H_i &= g(H_{i-1}, m_i) &i \in \mathbb{Z}_2^n \\
H(M) &= H_n
\end{cases}
\end{align}
$$
![[Pasted image 20220527142135.png]]
## Iterative hash functions
- Split input into fixed-sized blocks $m_1, \dots, m_k$ (usually block size is 512 - 1024 bits)
- Pad the last block
- Process blocks in order using a compression function $f()$ and a fixed-size intermediate state
	- $H_i = f(H_{i-1}, m_i)$, where $H_0$ is a fixed value (IV) and $H_k$ is the hash
	- Advantage: **message can be hashed on the fly**

## Merkle-Damgard construction
Defines a method for padding a message.

Creates a hash function from a fixed input size compression function
> A compression function $g$ takes a fixed size binary string as input and creates a smaller fixed size binary string

If the compression function is preimage resistant and collision resistant, then so is the hash function.

- Iterative hash function
- IV is an initial state (known)
- If one-way compression function is [[Cryptographic properties for hash functions|collision resistant]], then so is the hash function.

Other constructions:
- HAIFA, EMD, RMX, Dynamic construction

## Merkle-Damgard Padding
![[Pasted image 20220527141744.png]]
- Append a single 1 bit to the end of the message
- Append as many 0 bits to the end of the message as is required to make the message a multiple of the input size of the compression function, minus 64 bits
- Append the bit length of the message as a 64 bit integer to the end of the message

## Insecure example
[[AES]]
Message $m$ is split into 128 bit blocks $m_1, m_2, \dots , m_k$
$$
H_i = AES_K(H_{i-1} \oplus m_i) \hspace{2em} \text{where } H_0 = 0
$$
Why is this not a cryptographic hash function?
- Hint: break collision using only 2 blocks

### Attack
Let:
$$
\begin{align}
m &= (m_1 , m_2) \\
H_1 &= AES_k(0 \oplus m_1) \\
H_2 &= AES_k (H_1 \oplus m_2)
\end{align}
$$
Let:
$$\begin{align}
m' &= (m'_1 , m'_2) \hspace{2em} \text{ where}\\
m'_1 &= m_2 \oplus H_1 \\
m'_2 &= H_2 \oplus m_2 \oplus H_1
\end{align}$$
Then
$$\begin{align}
H'_1 &= AES_k(0 \oplus m_2 \oplus H_1) = H_2 \\
H'_2 &= AES_k (H'_1 \oplus H_2 \oplus m_2 \oplus H_1)\\
&= AES_k (m_2 \oplus H_1) \\
&= H_2
\end{align}$$
## Exercise
You designed a custom hash function $HS()$.\
Given the message $m=(m_0, m_1, \dots , m_n)$, the hash function returns $HS(m)=m_0 \oplus m_1 \oplus \cdots \oplus m_n$.
Which properties of a cryptographic hash function does $HS$ have?

### Is $HS()$ a [[Cryptographic properties for hash functions|cryptographic hash function]]?
- Preimage resistance
	- NO. Given $y$, then $m=y$
- Second preimage resistance
	- NO: Given $x = (m_1, m_2)$, then $x' = (m_2,m_1)$
- Collision resistance
	- NO: All pairs $(m_1, m_2)$ and $(m_2, m_1)$ collide
- Random oracle
	- NO: $m_1 = (m_1, 0)$

