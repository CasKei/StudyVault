---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Algo Hash functions]]

## Data Integrity
[[Data integrity]]

## Cryptographic Hash Functions
[[Cryptographic properties for hash functions]]

[[Cryptographic padding]]
Algo:
[[Cryptographic hashing]]
[[Designing hash functions]]

## Iterative Cryptographic Hash Functions
- [[Merkle-Damgard construction]]
- [[MD-based hash functions]]
- [[Length extension attack]]

## Cryptanalysis of hash functions
[[Cryptanalysis]]

## Hash Examples
[[SHA-1]], [[SHA-2]], [[SHA-3]]

## Conclusion
Message integrity is not preserved by [[Stream ciphers]].
Many other ciphers also do not guarantee integrity

Secure Hash functions are designed to allow integrity validation
- [[Cryptographic properties for hash functions|second preimage resistance]] is useful

MD5 is practically broken [[MD5 collisions]]

[[SHA-1]]'s collision resistance is questionable

Long term, [[SHA-3]] is best choice.