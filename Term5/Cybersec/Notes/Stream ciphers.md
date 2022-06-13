---
aliases: OTP, One-Time Pad
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Basic ciphers]]
[[Modern ciphers]]

## Data Processing
One character at a time.

Encryption is done one bit or byte at a time
- high speed, low hardware complexity

Starting state should never be the same twice
- key is often combined with an initialisation vector (IV) (Make sure IV is always changing whenever you're using it to encrypt info)

## Basic operations
- Mostly XOR shifts (performance reasons)
- Some ciphers use algebraic operations such as $(+ * \textasciicircum)$, $x \text{ mod } n$
- All operations are operating on finite sets of numbers

## Cipher is symmetric only
Not used in asymmetric encryption.

## Stream ciphers
- Operate on single elements of the input (single characters, bits)
- Well suited for (audio) signal transmission

| Pro                                          | Con                                               |
| -------------------------------------------- | ------------------------------------------------- |
| low processing delay for low data rate input | not as efficient (throughput) for high data rates |

## Ideal Stream ciphers
![[Pasted image 20220520215216.png]]

- enc and dec require same key
- operations are completely symmetric
- requires random symmetric key stream of same length as input

Will frequency analysis of the ciphertext work?
### Frequency analysis of ideal stream cipher
Ideal key stream $s$:
$$P(s_0) = P(s_1) = 0.5$$
independently of $p$.

$s_0, s_1, p_0, p_1$ are random events (key bit, plaintext bit)

| $s$ | $p$ | $c=s\oplus p$ | $P(\cdot)$                               |
| --- | --- | ------------- | ---------------------------------------- |
| 0   | 0   | 0             | $P(s_0) \cdot P(p_0) = 0.5 \cdot P(p_0)$ |
| 1   | 0   | 1             | $P(s_1) \cdot P(p_1) = 0.5 \cdot P(p_0)$ |
| 1   | 1   | 0             | $P(s_1) \cdot P(p_0) = 0.5 \cdot P(p_1)$ |
| 0   | 1   | 1             | $P(s_0) \cdot P(p_1) = 0.5 \cdot P(p_1)$                                         |

## One-Time Pad
Stream ciphers are very secure if **long random key** is available.
- It is **impossible to recover** plaintext from ciphertext (even if attacker has infinite resources)
- Key can only be used once

This ideal cipher is called One-Time Pad
- Has been used in practice e.g. to encrypt "red" telephone line between Russia and US

***Problem***
Key as long as message, must be exchanged securely
- Assume secure channel to exchange key

Why not exchange message over that channel?

### Why can't be brute force OTP ciphertext?
OTP is one of the few ciphers where brute force attacks are impossible.

With OTP encrypting a 5 letter word for example, every possible 5 letter word is a possible outcome after the encryption. The 'hacker' cannot know which set of words is the initially encrypted one. Hence you cannot break it even if you have infinite computational resources

### Why not reuse the key?
Encrypt twice with the same key?
e.g.
$m_1$ and $m_2$,
key stream $s$.
$c_1 = E(m_1 , s)$, $c_2 = E(m_2 , s)$

***Problem?***
$$
(m_1 \oplus s) \oplus (m_2 \oplus s) = m_1 \oplus m_2
$$


### Generating the key stream from short key
![[Pasted image 20220521100217.png]]
- Need way to generate a **long pseudo-random sequence**
- Both parties exchange **short key over secure channel**
- Both parties then **separately generate long key stream to de/encrypt**
- Key stream must be **unpredictable** (generating function is public)

### Attack OTP
```python
x = b'buy100\n'
from Crypto.Util.number import *
import pwn

key = long_to_bytes(0xa29c7b1e0e3aee)
key # output b'\xa2\x9c{\x1e\x0e:\xee'
```

```python
len(key) # output 7
len(x)   # output 7
```

```python
c = pwn.xor(x, key) #output : b'\xc0\xe9\x02/>\n\xe4
pwn.xor(c, key) # output : b'buy100\n'
pwn.xor(b'buy100\n', b'buy999\n') # output : b'\x08\t\t\x00'
```

```python
mask = b'\x00\x00\x00' + pwn.xor(b'buy100\n', b'buy999\n')
# b'\x00\x00\x00\x08\t\t\x00'
len(mask) # output 7
```

```python
c1 = b"\xc0\xe9\x02'7\x03\xe4"
pwn.xor(c1, key)
# output : b'buy999\n'
```
