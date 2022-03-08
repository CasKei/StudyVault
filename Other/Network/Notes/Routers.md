---
aliases: routing, router, hop
tags: network
---
[[Network Fundamentals]]

## Routing
To send a [[ARP - Address Resolution Protocol|packet]] to a machine on another [[Subnet Masks|subnet]], the frame is sent to a **router**.

A router *usually* has more than one [[Network Interface]] (and [[Mac and IP|MAC address]]).

A router *always* has more than one [[Mac and IP|IP]] address (at least one per subnet)

Machine A (subnet 1):
- MAC: `aa:aa:aa:aa:aa:aa`
- IP: `192.168.0.1 / 255.255.255.0`

Machine B (subnet 2):
- MAC: `bb:bb:bb:bb:bb:bb`  
- IP: `192.168.1.1 / 255.255.255.0`

Router (both subnets):
- MAC1: `cc:cc:cc:cc:cc:cc`  
- IP1: `192.168.0.254 / 255.255.255.0` 
- MAC2: `dd:dd:dd:dd:dd:dd`  
- IP2: `192.168.1.254 / 255.255.255.0`

## Hop
Example: Machine A wants to talk to Machine B, but B is on a different subnet.
- So it sends a frame using the [[Mac and IP|MAC]]

https://www.youtube.com/watch?v=9uebakqWlB0

25.13 cont.