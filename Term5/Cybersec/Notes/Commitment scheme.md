---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hashing applications]]

## Rock Paper Scissors
Alice and Bob are playing rock, paper, scissors via email.
- Each player sends action to the other
- Once both players receive all actions, select winner

Challenge: collect actions and determine winner *securely without shared keys*

## Commitment schemes
Design a solution using a [[Cryptographic hashing|cryptographic hash function]]:
$$H()$$
Alice and Bob follow a **two-phase protocol**.

Phase 1:
- Alice and Bob choose action 
	- $m_a = rock$
	- $m_b = rock$
- Compute commitment 
	-  $c_a = H(m_a)$
	- $c_b = H(m_b)$
- Exchange commitments
	- $c_a \leftrightarrow c_b$

Phase 2:
- Both exchange their actual messages
- Only the correct message will fit the commitment, so no one can cheat

## Problem: inversion of commitment
Alice and Bob can invert the commitment above. Input space is too small. One can preempt inputs and compare the hash value to react.

How to fix? Pad. Because of [[Cryptographic properties for hash functions|second preimage resistance]].

[[Cryptographic padding]]