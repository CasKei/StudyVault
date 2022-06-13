---
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]

## What
> Security: derived from latin "securus", meaning "free from care"

Interpretations:
- I am secure because I dun care
- I am secure because I know there cannot (negligible possibility) be any successful attack

## Terminology
Properties
- ==Confidentiality==
	- attacker cannot obtain data of victim
	- **prevent disclosure of information to unauthorised** individuals or systems
	- certain information should only be known to certain people
	- *Encryption*: encode messages so only certain people can read it
	- *Access controls*: selectively restrict access to a resource
	- *Steganography*: conceal info within another piece of info
- ==Integrity==
	- attacker cannot **change data** of victim **undetected**
	- data is stored and transferred as intended, any modification to the data is identified
	- *Hashing*: map data of an arbitrary length to data of a fixed length
	- *Digital signatures*: a mathemtical scheme to verify the integrity of data
	- *Certifiates*: combine with a digital signature to verify an individual
	- *Non-repudiation*: provides proof of integrity, can be asserted to be genuine
- ==Availability==
	- attacker cannot stop services proviced by victim
	- Systems and networks must be **up and running**
	- Info is accessible to authorised users
	- *Redundancy*: build services that will always be available: multiple duplicate servers?
	- *Fault tolerance*: system will continue to run even when failure occurs
	- *Patching*: stability, close security holes
- Safety
	- Escape plans and routes: best way out
	- Drills: test and adjust
	- Testing controls: run periodic tests against physical and digital security

- Privacy
- Authenticity
	- ensure you are communicating with the right person
- Non-repudiation
	- You cannot deny an action that you have taken
- etc

Difference between privacy and confidentiality

| Privacy                                                                                 | Confidentiality                                                         |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Control of data, specify visibility, state when person is free from public interference | Important information is kept secret until owner permits to disclose it |

## Measuring security
How to specify security?
- Attribute of system
	- depends on attacker
- Boolean value (secure/insecure) or real number
	- how about probabilistic attacks
- Metrics?
	- "level 7", "78% secure" ???

In practice
- Number of bugs found in software
- Attack surface: how many entry points
- Practical time-to-compromise for experts
- In general: estimates based on complexity and cost

Effort/time estimates based on brute force key exploration
![[Pasted image 20220517171337.png]]

## Alice, Bob and Eve
Commonly used in security research to explain protocol interactions.
Names sometimes change (Mallory, Charles, etc)
Convenient way to identify parties (servers, users, etc)
Alice usually initiates communication

Part of fundamental attacker and system model.

## Cryptography
[[Cryptography]]

## System and threat model, requirements
[[Requirements of system and threat model]]
- [[Kerckhoff design]]

## Conclusion
Security is important and will be ubiquitous.
Often hard to define and measure.
Depends on System model, Sequrity Requirements and Attacker model.
Good venues to follow: DefCon, Blackhat, etc.
