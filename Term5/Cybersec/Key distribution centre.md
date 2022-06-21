---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Key Establishment]]

## Centralised key distribution centre
- Each new user has [[Pre-shared key]] with KDC
- KDC can create $k_{AB}$ on demand and send to Alice and Bob
- The [[Kerboros protocol]] uses such a KDC

Problems?
- If KDC gets compromised, past keys could be disclosed
- KDC is a single point of failure