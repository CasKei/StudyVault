---
aliases: Data Encryption Standard
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
![[5vil3tp9.bmp]]
[![Data Encription Standard Flow Diagram.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Data_Encription_Standard_Flow_Diagram.svg/300px-Data_Encription_Standard_Flow_Diagram.svg.png)](https://en.wikipedia.org/wiki/File:Data_Encription_Standard_Flow_Diagram.svg)

The predominant [[Block ciphers]] before replaced by [[AES]].
- Developed in the 70s

Block size of 64 bits, 64 bit key (8 bits for parity, 56 bit for key size)
- Small keyspace: brute force attacks are now feasible
- No relevant other attacks have been found except some weak keys

## Process (encryption). Decryption just reverse the order of the 16 round keys
### Key transformation/generation/schedule
![[0g1u5ijz.bmp]]
Key goes through parity check (8 bits) so left with 56 bits.
Key transformation function turns them to 48 bits each.

### Expansion permutation
Duplicates a number of bits of $R$ (the right half of data input) to produce 48 bit output from 32 bit input.

This 48 bit result is XORed with the 48 bit round key $K_i$, and used in the S-box tables. ==XORing the key ensures the key and data are mixed, which is the whole point of a cipher==.

### S-Box permutation
A lookup table that is publicly known. 8 lookup tables, each of which maps 6 bits to 4 bits, bringing the result back to 32 bits. ==Provide nonlinearity. Without them, the cipher could be written as a bunch of binary additions, which is easy to mathematically attack.==

### P-box permutation
These 32 bits are then swapped around by the bit shuffle function.

### XOR and swap
Then they are XORed into the left value $L$.

REPEAT 16 TIMES. ==Combination of S-box, expand and bitshuffle provide diffusion==.

## Feistal round
![[Pasted image 20220607152218.png]]

64 bit plaintext split into 2 32 bit halves L and R.\
Splitting is done by rearranging the bits in a semi-ordered fashion. (has no cryptographic effect but that's how the designers defined DES).\
A similar swapping of bits is implemented at the end of the encryption to create the 64 bit ciphertext from the two halves L and R.

Consists of  ==**16 rounds of [[Feistel network]]**==
- $P$ is a parity check function
- $T$ is a key transformation function

## 3DES
Encrypt with one 56 bit key, decrypt with second 56 bit key, then encrypt again either with first key or thried 56 bit key. 3 times slower than DES.\
3DES (Triple DES) is used as a drop-in replacement
$$c=E(E^{-1}(E(m,k_1), k_2), k_3)$$
- Effective key length increased to 112
- Backward compatible: when $k_1 = k_2 = k_3$, same as DES.

## Weakness
Each  round key consists purely of some bits selected from cipher key. If cipher key is 0, then all round keys are 0. Remember that the only difference between enc and dec is the order of round keys. But with all round keys 0, enc with 0 key is same as dec with 0 key. This is a very easy property of detect and leads to an easy and efficient distinguishing attack.

Complementation property. Ensures that
$$E(\overline{K}, \overline{P}) = \overline{E(K,P)}$$
for all keys $K$ and plaintexts $P$, where $\overline{X}$ is the value obtained by complementing all bits in $X$. In other words, if you encrypt the complement of the plaintext with the complement of the key, you get the complement of the ciphertext. This property may lead to attacks.

## Modes of operation
