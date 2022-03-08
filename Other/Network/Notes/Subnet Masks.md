---
aliases: subnet
tags: network
---
[[Network Fundamentals]]

But machines can only directly send IP [[ARP - Address Resolution Protocol|packets]] to machines on the same network, so what is a network/subnetwork?

## Subnets
As well as [[Mac and IP]], each machine has a subnet mask.
They look like this:
- `255.255.255.0`

The **subnet mask** is used in combination with a source and destination IP to decide if they are on the same subnet or not.

It's actually much easier to understand in binary.
Two machines are on the *same subnet if the bits in their IPs match where the corresponding bit in the subnet mask is a 1*
![[Pasted image 20220307135619.png]]

If computers are in the same subnet, it can send information via [[ARP - Address Resolution Protocol|ARP]], else, it has to send via [[Routers]]