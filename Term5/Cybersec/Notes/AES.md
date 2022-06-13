---
aliases: AES-128, AES-192, AES-256, Rijndael
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Block ciphers]]

## What
- Result of NIST design competition in 2000
- Not a [[Feistel network|Feistel cipher]].
- Designed to operate on **128-bit block size**
- 3 modes with different key length:
	- AES-128 (10 rounds)
	- AES-192 (12 rounds)
	- AES-256 (14 rounds)

No efficient attacks are known aside from side-channel attacks on implementation.

## Basic structure
10/12/14 rounds.

Round keys are derived from key
- 11 round key for 10 rounds
- Each round key is $4 \times 32$ bits long
- Rijndael key schedule is used to derive keys (not in syllabus)

In each round
- Substitution layer (SubBytes)
- Diffusion layer
	- Shiftrows
	- MixColumns
- Key addition (AddRoundKey)

All operations operate on bytes.

## AES-128
### Overview
![[Pasted image 20220607155134.png]]

Last round does not use the MixColumns function.

### Single round
![[Pasted image 20220607155212.png]]

### Substitution layer (S-Boxes)
**128-bit state (16 bytes)** input.\
Each input byte translated by S-Box to output byte. S-boxes are all identical.

Mapping is **bijective** (256 individual mappings)

Similar to constant key substitution cipher
- non-linear if constructed correctly (not just [[Substitution ciphers|Caesar's cipher]])
- $S(A) + A(B) \not= S(A+B)$

Implementation

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | a   | b   | c   | d   | e   | f   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 63  | 7c  | 77  | 7b  | f2  | 6b  | 6f  | c5  | 30  | 01  | 67  | 2b  | fe  | d7  | ab  | 76  |
| 1   | ca  | 82  | c9  | 7d  | fa  | 59  | 47  | f0  | ad  | d4  | a2  | af  | 9c  | a4  | 72  | c0  |
| 2   | b7  | fd  | 93  | 26  | 36  | 3f  | f7  | cc  | 34  | a5  | e5  | f1  | 71  | d8  | 31  | 15  |
| 3   | 04  | c7  | 23  | c3  | 18  | 96  | 05  | 9a  | 07  | 12  | 80  | e2  | eb  | 27  | b2  | 75  |
| 4   | 09  | 83  | 2c  | 1a  | 1b  | 6e  | 5a  | a0  | 52  | 3b  | d6  | b3  | 29  | e3  | 2f  | 84  |
| 5   | 53  | d1  | 00  | ed  | 20  | fc  | b1  | 5b  | 6a  | cb  | be  | 39  | 4a  | 4c  | 58  | cf  |
| 6   | d0  | ef  | aa  | fb  | 43  | 4d  | 33  | 85  | 45  | f9  | 02  | 7f  | 50  | 3c  | 9f  | a8  |
| 7   | 51  | a3  | 40  | 8f  | 92  | 9d  | 38  | f5  | bc  | b6  | da  | 21  | 10  | ff  | f3  | d2  |
| 8   | cd  | 0c  | 13  | ec  | 5f  | 97  | 44  | 17  | c4  | a7  | 7e  | 3d  | 64  | 5d  | 19  | 73  |
| 9   | 60  | 81  | 4f  | dc  | 22  | 2a  | 90  | 88  | 46  | ee  | b8  | 14  | de  | 5e  | 0b  | db  |
| a   | e0  | 32  | 3a  | 0a  | 49  | 06  | 24  | 5c  | c2  | d3  | ac  | 62  | 91  | 95  | e4  | 79  |
| b   | e7  | c8  | 37  | 6d  | 8d  | d5  | 4e  | a9  | 6c  | 56  | f4  | ea  | 65  | 7a  | ae  | 08  |
| c   | ba  | 78  | 25  | 2e  | 1c  | a6  | b4  | c6  | e8  | dd  | 74  | 1f  | 4b  | bd  | 8b  | 8a  |
| d   | 70  | 3e  | b5  | 66  | 48  | 03  | f6  | 0e  | 61  | 35  | 57  | b9  | 86  | c1  | 1d  | 9e  |
| e   | e1  | f8  | 98  | 11  | 69  | d9  | 8e  | 94  | 9b  | 1e  | 87  | e9  | ce  | 55  | 28  | df  |
| f   | 8c  | a1  | 89  | 0d  | bf  | e6  | 42  | 68  | 41  | 99  | 2d  | 0f  | b0  | 54  | bb  | 16    |

Example: $S(b7)=a9$

- S-Boxes are implemented as complete lookup tables
- or hardwired as logic circuits
- *256 bytes per table*

### Diffusion layer
**Shiftrows** simply changes the order of Bytes
![[Pasted image 20220607163714.png]]

**MixColumns** computes a linear combination of the input bytes (more in [[Modular Arithmetic]])
$\theta : M_{4\times 4} \begin{bmatrix} \mathbb{F}_{2^8}\end{bmatrix} \to M_{4\times 4} \begin{bmatrix} \mathbb{F}_{2^8}\end{bmatrix}$ by
$$
\theta(a) = b \Leftrightarrow 
\begin{bmatrix}
b_{0j}\\
b_{1j}\\
b_{2j}\\
b_{3j}\\
\end{bmatrix}
= T\cdot
\begin{bmatrix}
a_{0j}\\
a_{1j}\\
a_{2j}\\
a_{3j}\\
\end{bmatrix}
$$
where $T\in M_{4\times 4} \begin{bmatrix} \mathbb{F}_{2^8}\end{bmatrix}$ is fixed as
$$
T=
\begin{bmatrix}
02 &03 &01 &01 \\
01 &02 &03 &01 \\
01 &01 &02 &03 \\
03 &01 &01 &02 \\
\end{bmatrix}
$$

## Decryption
- Each operation is inverted and applied in reverse order.
- Round keys are derived in the same way but applied in reverse order
- XOR of addRoundKey is easy to invert
- Diffusion layer inverted using the multiplicative inverse of the coefficients in $GF(2^8)$
- S-Boxes can also be inverted easily
- Overall, same effort for decryption and encryption

## Properties
Parallelism: Each step  consists of a number of operations that can be performed in parallel. This makes high-speed implementations easy.

Decryption operation is significantly different from encryption operation. You need the inverse lookup table of the S-box, and the inverse mixing operation is different from the original mixing operation.

XORs add key material to data. S-boxes add nonlinearity, byte shuffle and mixing functions provide diffusion.

## Other NIST finalists
[[Serpent]]
[[Twofish]]
[[RC6]]
[[MARS]]
