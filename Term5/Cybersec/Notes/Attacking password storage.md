---
aliases: brute force password, brute force hashes
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Passwords]]

## Brute force attack
Common [[Cryptographic properties for hash functions|cryptographic hashes]] have length 128 ([[MD5]]), 160 ([[SHA-1]]), 224-512 ([[SHA-3]]).

Brute forcing [[SHA-1]] takes about $O(2^{160})$ computations.

To speed this up:
- Precompute all/some values
- Look up directly
- Unfortunately takes $160\cdot 2^{120} TB$ of storage

## Improving brute force
> Computing hashes on demand, or full precomputation is infeasible.

Mix?
- Do precomputation, but store only a subset of the found hashes
- Ensure that you can recover preimage of the pre-computed values

This is the idea behind [[Rainbow Tables]], based on [[Hash chain]]s.

> - Ignore hash [[Intro to hashing|collisions]] to simplify things.
> - Assume input space < output space (10 char inputs only)

Note: [[Rainbow Tables]] are not computed "on the fly" to look up one hash
- direct brute force more efficient in that case
- [[Rainbow Tables]] allow you to reuse brute force effort for many hashes


[[Hash chain]]

[[Rainbow Tables]]

[[Hashcat]]