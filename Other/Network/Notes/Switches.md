---
aliases: 
tags: 
---
[[Network Fundamentals]]

## Switching
[[Hubs]]
Network switches are smarter and more efficient
- Switches remember the source [[Mac and IP|MAC]]s they have seen on each port
- Frames are only sent to the port that a MAC is connected to
- If the switch doesn't know where a MAC is, it sends to all ports
	- It never knows where `ff:ff:ff:ff:ff:ff` is so it always goes to all ports
- Fewer collisions!
- Much faster!
	- 10Gbit is fairly common in switched networks

But machines can only directly send IP [[ARP - Address Resolution Protocol|packets]] to machines on the same network, so what is a network/subnetwork? [[Subnet Masks]]