---
aliases:
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[OS Kernel]]

## How
> The operating system kernel provides **protection** for the computer system by providing a mechanism for **controlling access** of processes or users to resources defined by the OS.

This is done by identifying the **user** associated with that process:

1.  Using user identities (user IDs, security IDs): name and associated number among all numbers
2.  User ID then associated with all files, processes of that user to determine **access control**
3.  For shared computer: group identifier (group ID) allows set of users to be defined and controls managed, then also associated with each process, file

You will learn more about this in Week 6 and during Lab 2. During Lab 2, you will learn about **Privilege Escalation**: an event when a user can change its ID to another effective ID with more rights. You may read on how this can happen in Linux systems [here](https://linux-audit.com/understanding-linux-privilege-escalation-and-defending-against-it/).

Finally, the Kernel also provides **defensive security measures** for the computer system: protecting itself against internal and external attacks via firewalls, encryption, etc. There’s a huge range of security issues when a computer is connected in a network, some of them include denial-of-service, worms, viruses, identity theft, theft of service. You will learn more about this in Week 10.