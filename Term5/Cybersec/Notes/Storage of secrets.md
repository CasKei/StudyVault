---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Hashing applications]]

## Problem
You want to store a set of usernames and their passwords.

But other users might be able to read or copy the storage.

How to protect the [[Passwords]]?

## Linux hashing passwords
In Linux, passwords are stored as [[SHA-2|SHA-512]] hashes in `/etc/shadow`

When user inputs the password, it is hashed and compared with the stored value. This is intended to keep passwords secret. 

### Can you think of ways to attack this scheme?
Password, then hash, then store the hash.
Input is small so we can just brute force. Hash function is ok, but because passwords are short, its still possible to brute force.

## Finding Preimages
Attacker:
- has hash values of passwords
- needs to find original passwords

### Attack
- Create list of likely passwords
- Compare hash of each one with stolen hashes
- For short passwords, complete lists can be precomputed ([[Rainbow Tables]])
- Using [[Rainbow Tables]], large sets of user/hash tuples can be processed quickly

Example: [[Hashcat]]

## Hashing other secrets
- Hashing is also used to anonymise other data (e.g. IDs, URL blacklists)
- Without salt (random number), randomness of the input might be too low again
- (Bad example): anonymisation of license plates in data reported by police