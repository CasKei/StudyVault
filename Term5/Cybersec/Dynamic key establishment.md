---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]

## Dynamic peer-to-peer key establishment
What if we could find a protocol to automatically negotiate keys?
- Alice and Bob could run it to derive a shared key

Ideally both contribute "randomness".
- This prevents an attacker from reusing keys

## What if there are no pre-existing keys?
What happens if there are no pre-existing keys?
- Chicken and egg problem??

Wihtout pre-existing key:
- No integrity protection is possible
- No authenticity can be verified
- No confidentiality is possible

Public key protocols solve this problem!