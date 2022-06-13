---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Passwords]]

## Terminology
**Access control**
- Allow/deny users access to resources
- Sometimes, delegation is possible

**Authentication verifies the correctness of data and source**
- In this context: verifying the identity of login request
- Identification itself does not include verification

## Identification schemes
[[Identification scheme]]

## Authentication schemes
[[Authentication scheme]]

## Password-based authentication
#### Advantages
- Can be changed
- User is free to choose

#### Disadvantages
- Can be forgotten
- User can create bad passwords
- Can be re-used

How to remember 30+ passwords?

## Password guessing
Why is guessing passwords so easy compared to cryptographic keys?
- Passwords use *printable characters*
- Passwords are somewhat *short*
- Some passwords are used more *frequently*

These enable semi-intelligent brute forcing:
- [[Dictionary attack]]
- [[Hybrid attack (password)]]

## Finding passwords in practice
Both [[Dictionary attack]]s and [[Hybrid attack (password)|hybrid attack]]s can be used to build long lists of likely passwords.

If there is an API to submit unlimited password attempts, this could be called to break into a system
- most systems limit the number of attempts

In most cases, dictionary and hybrid attacks are used to attempt to find [[Cryptographic properties for hash functions|preimages]] of hashes
- Password hashes were stolen in some attack
- attacker has unlimited attempts to find preimage

