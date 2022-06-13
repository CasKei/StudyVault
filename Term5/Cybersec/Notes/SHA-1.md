---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## What
- Processes 512-bit input message blocks
- Produces a 160 bit digest (output is a 160 bit block)
- Pre-defined (e.g. constant and public) initial state of 160 bits
- Uses [[Merkle-Damgard construction]]
- 80 internal rounds per $f$

[[MD-based hash functions]]

- Also derived from MD4
- A slight modification of SHA-0 to fix a 'technical error'
- Created by NIST with the help of NSA
- Defined in FIPS PUB 180-2

## How
For each block of 512 bits,
- Expand block to $80 \times 32 = 2560$ bits
- Feed the block and previous state into $f$
- Each $f$ has 4 stages
- Each stage $t$ has 20 rounds, using a constant $K_t$, and a non-linear function $f_t$

## Compression Function
![[Pasted image 20220522185335.png]]
- Message expansion round expanding 16 32-bit message words to 80 32-bit message words
- Consists of 4 rounds of 20 steps each, each step processing 32 bits of the expanded message
- Each round processes 20 of the 80 expanded words
- 3 round functinos, 1 used twice
- 5 internal 32 bit registers store the current state of the algorithm
- The internal registers are initialised to fixed constants

## Expansion Round
Expansion Round
- Expands 512 bit (16 32-bit words) to 2560 bits (80 32-bit words)

Defined by the recurrence:
$$
\begin{align}
W_t = \begin{cases}
M_t &t = 0\dots15\\
(W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) <<< 1 &t=16\dots79
\end{cases}
\end{align}
$$
Differs from SHA-0 by the 1-bit rotation to the left

## Round Function (A SHA-1 Step)
![[Pasted image 20220522185409.png]]
$A \to E$ are the 32 bit internal registers

$F$ is one of the following:
$$
\begin{align}
F_1 &= (X \land Y) \lor (\lnot X \land Z)\\
F_2 &= X \oplus Y \oplus Z\\
F_3 &= (X \land Y) \lor(X \land Z) \lor(Y \land Z)\\
F_4 &= X \oplus Y \oplus Z
\end{align}
$$
- $W_t$ is the $t^{th}$ expanded message word.
- $K_t$ is the $i^{th}$ round constant
- $<<<$ is a rotation to the left

## Why 80 rounds
Increasing the number of rounds
- Makes brute force attacks more expensive (each hashing takes longer)
- Makes attacks relying on differential [[Cryptanalysis]] harder

The exact value for SHA-1 was most likely chosen as compromise between performance and security.

[[SHA-2]] uses 64 rounds as default. Attacks have been found for 52 round versions.

## [[Cryptanalysis]] of [[SHA-1]]
2005
- Collisions found in $2^{69}$ steps instead of $2_{80}$, factor of 2048

2009
- That result was claimed to be improved to $2^{52}$ steps (but found to be incorrect)

Assuming $2^{60}$ tries, and $2^{14}$ CPU cycles per SHA-1, breaking it will cost:
- $700K in 2015
- $173K in 2018
- $43K in 2021

2017
Google found collisions in $2^{63}$ tries

GPU can help
