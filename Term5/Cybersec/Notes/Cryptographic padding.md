---
aliases: pad, padding
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hashing applications]]

## Block size different how
So far we assumed $m$ was of correct length of [[Block ciphers|block-based]] cryptographic [[Hash functions]] (512 for [[SHA-1]])

If $I=|m|$ is too short, we have to apply padding.

#### Example
Block size: 10 char
$m = Hello!$

Pad with random data?
$\to Hello!X4Qa$

## Padding structure
Padding has structure.

[[SHA-1]]
- Padding is a 1 followed by 0s and the length of the message

Other crypto functions require other schemes

Random bytes as padding also can be used.

## Rule
Padding must be reversible. It must be possible to uniquely determine the original message from a padded message.

## Scheme 1
Let $P$ be plaintext and $\ell (P)$ be the length of $P$ in bytes. Let $b$ be block size of the [[Block ciphers]] in bytes.

Append a single byte with value 128, then as many 0 bytes as required to make overall length a multiple of $b$. Number of 0 bytes added is in the range $0, \dots , b-1$.

## Scheme 2
Let $P$ be plaintext and $\ell (P)$ be the length of $P$ in bytes. Let $b$ be block size of the [[Block ciphers]] in bytes.

Determine the number of padding bytes required. This is a number $n$ which satisfies $1 \leq n \leq b$ and $n + \ell (P)$ is a multiple of $b$. Pad the plaintext by appending $n$ bytes, each with value $n$.

## After pad
Then we can cut the data into blocks. Number of blocks $k$ can be computed as $\left\lceil \dfrac{\ell(P) + 1}{b} \right\rceil$.

After decrypting ciphertext, padding has to be removed. Code that removes padding should also check that padding was correctly applied. Each padding byte has to be verified to ensure it has the correct value. Erroneous padding should be treated in the same manner as an authentication failure.

