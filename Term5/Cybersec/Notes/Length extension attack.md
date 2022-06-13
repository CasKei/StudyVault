---
aliases:
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]
[[MD-based hash functions]]

## What
Let
$m=m_1 ,\dots , m_k$
$m'=m_1 ,\dots ,m_k ,m_{k+1}$.
$$
H(m') = f(H(m), m_{k+1})
$$
$H(m)$ provides direct info about the intermediate state after the first $k$ blocks of $m_0$.

## Consequences
$H(m')$ can be computed *without* knowing $m$.
- $m=(secret | pad)$. Attacker can compute $H(secret|pad|data)$ for any data

If attacker finds a [[Intro to hashing|collision]] of $m$, he can generate infinite number of collisions.

## Fixes
Special processing is needed at the end of the process, e.g.

### $H_{fixed}(m) = H(H(m)||m)$
The iterative hash computations immediately depends on all the bits of the message

Disadvantages: slow, have to hash $m$ twice, cannot hash on the fly

### Truncate the output
Only use the first $n-s$ bits as the hash value

E.g. SHA-512 can drop 256 bits of output, return the other 256 bits hash value