---
aliases: message-digest algorithm 5
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]
[[MD-based hash functions]]

## MD5 Function
Specifies the compression function to use.

- Processes 512-bit message blocks
- Produces a 128-bit digest
***
* Derived from MD4 to address security concerns
* Created by Ronald Rivest and described in RFC in 1321

## MD5 Compression Function
Each iteration:
- 4 rounds of 16 steps each

Each step:
- process 32-bits of the message

Each round:
- Process all 512 of the input bits

4 round functions, 1 per round : $F(X,Y,Z)$

4 internal 32-bit registers store the current state of the algorithm

The internal registers are initialised to fixed constants.

## An MD5 Step
![[Pasted image 20220527143159.png]]
$A \to D$ are the 32 bit internal registers

$F$ is 1 of 4 functions
$$
\begin{align}
F_1 &= (X \land Y)\lor(\lnot X \land Z)\\
F_2 &= (X \land Z)\lor(Y \land \lnot Z)\\
F_3 &= X \oplus Y \oplus Z\\
F_4 &= Y \oplus (X \lor \lnot Z)
\end{align}
$$
- $M_i$ is the $i^{th}$ message block
- $K_i$ os tje $i^{th}$ round constant
- $<<<_s$ is an $s$ bit rotation to the left

## Attack
- brute force
- dictionary
- [[Rainbow Tables]]