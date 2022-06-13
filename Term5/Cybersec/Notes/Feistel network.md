---
aliases: Feistel cipher
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]
[[DES]]

## What
A symmetric structure used in the construction of [[Block ciphers]]. Encryption and decryption are very similar operations, both consist of running a function called a 'round' function a fixed number of times.

## Feistel Networks
![[Pasted image 20220607152426.png]]
**Symmetric structure** for en/decryption.
- Only the *key scheduling* differs between both

Plaintext split to 2 halves $L_i$ and $R_i$. Splitting is done by rearranging the bits in a semi-ordered fashion. (has no cryptographic effect but that's how the designers defined DES).\
A similar swapping of bits is implemented at the end of the encryption to create the 64 bit ciphertext from the two halves $L$ and $R$.

- Each round in [[DES]] is **1 Feistel iteration**
- Function $f$ does [[Block ciphers|diffusion]] and [[Block ciphers|confusion]].

## Round function $f$
The round function $f$ takes in 2 inputs:
$R_i$ (data block) and $K_i$ (round key)

Returns an output of the same size as the data block.

In each round, the round function is run on half the data, and this output is XORed with the other half of the data. This is repeated.

- Each round $i$ uses a separate 48 bit round key $K_i$.
	- Each round key is formed by selecting 48 bits from the 56 bit key, selection is different for each round key. Algo that derives the round key is called the key schedule.
	- Round $i$ transforms $(L,R)$ pair into new $(L,R)$ pair under control of a round key $K_i$. Most work is done by round function $f$. 

An important advantage of Feistel networks compared to other cipher designs such as [substitution–permutation networks](https://en.wikipedia.org/wiki/Substitution%E2%80%93permutation_network "Substitution–permutation network") is that the entire operation is guaranteed to be invertible (that is, encrypted data can be decrypted), even if the round function is not itself invertible. The round function can be made arbitrarily complicated, since it does not need to be designed to be invertible.

## Encryption
For each round $i = 0, 1, \dots , n$, conpute
$$
\begin{align}
L_{i+1} &= R_i \\
R_{i+1} &= L_i \oplus f(R_i , K_i)
\end{align}
$$
Then ciphertext is $(R_{n+1}, L_{n+1})$

## Decryption
For each round $i = n, n-1, \dots , 0$, conpute
$$
\begin{align}
R_i &= L_{i+1} \\
L_i &= R_{i+1} \oplus f(L_{i+1} , K_i)
\end{align}
$$
Then plaintext is $(L_0, R_0)$

Note the reversal of the subkey order for decryption; this is the only difference between encryption and decryption.

## List of Feistel ciphers
Feistel or modified Feistel:
-   [Blowfish](https://en.wikipedia.org/wiki/Blowfish_(cipher) "Blowfish (cipher)")
-   [Camellia](https://en.wikipedia.org/wiki/Camellia_(cipher) "Camellia (cipher)")
-   [CAST-128](https://en.wikipedia.org/wiki/CAST-128 "CAST-128")
-   [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard "Data Encryption Standard")
-   [FEAL](https://en.wikipedia.org/wiki/FEAL "FEAL")
-   [GOST 28147-89](https://en.wikipedia.org/wiki/GOST_28147-89 "GOST 28147-89")
-   [ICE](https://en.wikipedia.org/wiki/Information_Concealment_Engine "Information Concealment Engine")

-   [KASUMI](https://en.wikipedia.org/wiki/KASUMI_(block_cipher) "KASUMI (block cipher)")
-   [LOKI97](https://en.wikipedia.org/wiki/LOKI97 "LOKI97")
-   [Lucifer](https://en.wikipedia.org/wiki/Lucifer_(cipher) "Lucifer (cipher)")
-   [MARS](https://en.wikipedia.org/wiki/MARS_(cryptography) "MARS (cryptography)")
-   [MAGENTA](https://en.wikipedia.org/wiki/MAGENTA_(cipher) "MAGENTA (cipher)")
-   [MISTY1](https://en.wikipedia.org/wiki/MISTY1 "MISTY1")

-   [RC5](https://en.wikipedia.org/wiki/RC5 "RC5")
-   [Simon](https://en.wikipedia.org/wiki/Simon_(cipher) "Simon (cipher)")
-   [TEA](https://en.wikipedia.org/wiki/Tiny_Encryption_Algorithm "Tiny Encryption Algorithm")
-   [Triple DES](https://en.wikipedia.org/wiki/Triple_DES "Triple DES")
-   [Twofish](https://en.wikipedia.org/wiki/Twofish "Twofish")
-   [XTEA](https://en.wikipedia.org/wiki/XTEA "XTEA")

Generalised Feistel:
-   [CAST-256](https://en.wikipedia.org/wiki/CAST-256 "CAST-256")
-   [CLEFIA](https://en.wikipedia.org/wiki/CLEFIA "CLEFIA")
-   [MacGuffin](https://en.wikipedia.org/wiki/MacGuffin_(cipher) "MacGuffin (cipher)")
-   [RC2](https://en.wikipedia.org/wiki/RC2 "RC2")
-   [RC6](https://en.wikipedia.org/wiki/RC6 "RC6")
-   [Skipjack](https://en.wikipedia.org/wiki/Skipjack_(cipher) "Skipjack (cipher)")
-   [SMS4](https://en.wikipedia.org/wiki/SMS4 "SMS4")