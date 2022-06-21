---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]

## Challenge
Design a secret chat application.
- Need at least: confidentiality, integrity, what else?

Wireless devices and vommunication can be used.
Staff/Student ID as source/destination for message sending/receiving.

Design questions
- Which infrastructure?
- Which.how many messages?
- Students joining/leaving?

## An Insecure Solution
- Alice computes hash value of $m$ : $H(m)$
- Alice broadcasts message: $(Bob : m, H(m))$
- Bob receives, validates $H(m)$

What are the security problems here?

## Distributed Solution
- Everyone has shared key with everyone
- Messages can be sent directly
- To send $m$ to Bob, Alice
	- Looks up the shared key $k_{AB}$
	- Compute the $MAC(m, k_{AB})$ ([[Message authentication code]])
	- Encrypt $m$ to obtain ciphertext $c$ (e.g. [[AES]] with $k_{AB}$)
	- Send $(c , MAC(m, k_{AB}))$ to Bob
	- Bob decrypts $c$ using $k_{AB}$ and verifies $MAC(m,  k_{AB})$

## Centralised Solution
- One server (Charles), everyone gets shared key with server.
- $n$ keys are pre-shared (somehow)
- If Alice wants to send message to Bob
	- Alice securely asks Charles for a new key $k_{AB}$
	- Alice uses that key to encrypt, and compute [[Message authentication code|MAC]] for the message.
	- Bon gets $k_{AB}$ securely from Charles, decrypts message
- Delay + overhead for server communication
- Need to trust the server

## Summary
Given symmetric encryption and [[Message authentication code|MAC]], confidentiality nad integrity is easy.

The main practical challenge is [[Key Establishment]]!

This appears frequently in real systems:
- How to authenticate users for SUTD WiFi
- How to set up secure communication for ad hoc users
