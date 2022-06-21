---
aliases: MAC, IP
tags: network
---
[[Network Fundamentals]]

## One To One
- 2 machines can talk to each other
- Each machine has a [[Network Interface]] (connected with a network cable)
- [[Network Interface]]s can be connected directly to each other via network cable
- Each [[Network Interface]] has a Media Access Control (MAC) address (hardware address)
- Looks like this: `50:46:5d:54:94:23`
- **MAC addresses** are globally unique (in theory)
- Data is sent in chunks called 'frames'
- Each frame has a source and destination MAC address

## How do they know the destination MAC Address?
- They don't
- They do know the **IP address** (because you tell them it)
- An IPv4 address looks like :`192.168.0.1`
	- There's also IPv6, not covered
- A machine can ask the whole network who has that particular IP
- Machines ignore frames that don't have their MAC as the destination
- But there's a special 'anyone' or 'broadcast' MAC: `ff:ff:ff:ff:ff:ff

## Why a MAC *and* a IP?
Machine can have more than 1 IP address... and other reasons too.

These are representative ways of expressing addresses in a network.

## IP Address (version4)
- 4 octets(32 bit)
- used at internet connection.

![[Pasted image 20220619150307.png]]

## MAC Address
- 6 octets (48 bits)
- first 3: OUI
- last 3: NIC unique number
- used at network communication

![[Pasted image 20220619150353.png]]