---
aliases: MACs, HMAC, MAC
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hashing applications]]

## Motivation
![[Data integrity#Data Manipulation attacks]]

- Alice and Bob share key $k$
- Using [[Stream ciphers|One-Time Pad]] or [[Stream ciphers]], they cannot guarantee [[Data integrity]].
- Using [[SHA-1]] directly does not help
	- attacker can flip bits and compute new hash
- MAC prevents this attack

## Message authentication codes (MACs)
### Requirements
- Alice and Bob share $k$
- Alice sends $m$ to Bob, also sends $x$
- Using $x$, Bob can verify integrity of $m$
- Both have access to [[Cryptographic properties for hash functions|cryptographic hash function]] $H()$

> $x$ is the message authentication code

### MAC construction
#### Which construction is better? (assuming [[MD-based hash functions]])
Secret as prefix:
$$x = H(k||m)$$
##### Attack
[[Length extension attack]]
Allows attacker to create valid MAC for a version of $m$ with additional blocks at the end

Secret as suffix:
$$x = H(m||k)$$
##### Attack
Allows attacker to re-use MAC if second preimage can be found


## Hash-based MACs (HMACs)
HMAC combines both prefix and suffix secrets to solve previous problems

$$
HMAC(k,m) = H\left(
(k \oplus opad)||
H(k \oplus ipad) ||
m
\right)
$$
- opad: outer padding $(0x5c5c5c \dots 5c5c)$
- ipad: inner padding $(0x363636 \dots 3636)$

Alice sends $(m, HMAC(k,m))$ to Bob
- Bob compute $HMAC$ for $m$ and $k$
- Bob acceps message if $HMAC$ same as sent
- Attacker cannot construct valid $HMAC$ wihtout $k$
- Attacker cannot change $m$ without changing $HMAC$

### Exercise
Recall your hash function $HS()$ that computes the hash of
$$m = (m_0 , \dots , m_n)$$
as
$$
HS(m) = m_0 \oplus m_1 \oplus \dots \oplus m_n
$$

Alice and Bob use the following MAC:
$$HMAC(m,k) = HS(m||k)$$
Alice sends $(m , HMAC(m,k))$ where $m = (222,222,222)$ (block length 3) to Bob.

#### Attack: Charlie intercepts this message
Charlie knows $HS()$. Can Charlie generate a valid HMAC for $m' \not= m$?

$$
\begin{align}
m &= (222,222,222) \\
x \leftarrow HS(m||k) &= 222 \oplus 222 \oplus 222 \oplus k \\
&= 222 \oplus k \\
\\
m' &= (345,345,222)\\
x \leftarrow HS(m||k) &= 345 \oplus 345 \oplus 222 \oplus k \\
&= 222 \oplus k
\end{align}
$$
Hence there exists a second input $m'$ that generates the same HMAC as $m$, without Charlie knowing the key $k$.

This breaks the [[Cryptographic properties for hash functions|second preimage resistance]] and hence is unsafe.