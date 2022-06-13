---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Passwords]]
[[Attacking password storage]]
[[Hash chain]]

## Hm
If salts used, [[Attacking password storage|brute force]] might be the only solution to find preimages. 

Not infeasible if:
- input from small space
- hashing is cheap

Attacker effort directly depends on cost of hash
- if hashing can be done in 1% of time, attack is 100 times faster
- Bitcoin gave birth to a lot of specialised hashing hardware

> Hashcat is optimised for password recovery, can run on GPUs