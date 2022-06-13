---
aliases: SHA-256, SHA-512
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hash functions]]

## What
Uses 64 rounds as default. Attacks have been found for 52 round versions

Designed by NSA (like [[SHA-1]]) and published in 2001

Shares a lot of the structure.
Successor of SHA-2 was chosen in a semi-public process

In Oct 2012, Keccak was selected as [[SHA-3]] algorithm.
- Focus on security and implementation speed

[SHA-2](https://cheapsslsecurity.com/blog/what-is-sha2-and-what-are-sha-2-ssl-certificates/), on the other hand, is a ==family of six different hash functions== that generate hash values of ==varying lengths== — 224, 256, 384, or 512 bits. However, it’s important to note that these other hash functions are not as frequently seen as the 256-bit. For example, the 224-bit variety isn’t strong enough for publicly trusted SSL certificates, and its big brother, the 512-bit variation isn’t widely supported by software. The most popular SHA2 algorithm is SHA256.