---
aliases: ARP, ARP cache, packets, packet
tags: packet, ARP
---
[[Network Fundamentals]]

## Message 1
Machine A wants to talk to Machine B
Machine A:
- IP `192.168.0.1`
- MAC `aa:aa:aa:aa:aa:aa`

Machine B:
- IP `192.168.0.2`
- MAC `bb:bb:bb:bb:bb:bb`

Machine A sends a frame like this:
- Source MAC: `aa:aa:aa:aa:aa:aa`
- Destination MAC: `ff:ff:ff:ff:ff:ff`
- Data: "Who has `192.168.0.2`? Tell `192.168.0.1`! "

Machine B responds with a frame like this:
- Source MAC `bb:bb:bb:bb:bb:bb`
- Destination MAC `aa:aa:aa:aa:aa:aa`
- Data: "`192.168.0.2` is at `bb:bb:bb:bb:bb:bb`!"

Both machines store the correspponding [[Mac and IP]] in their [[#ARP Cache]] (Address Resolution Protocol) cache for future use.

## Message 2
Machine A wants to talk to Machine B again.
This time Machine A can find the [[Mac and IP|MAC]] address in its [[#ARP Cache]].
Machine A sends a frame like this:
- Source MAC: `aa:aa:aa:aa:aa:aa`
- Destination MAC: `bb:bb:bb:bb:bb:bb`
- Data: ...

Inside the data is an [[Mac and IP|IP]] 'Packet', which looks like this:
- Source IP: `192.168.0.1`
- Destination IP: `192.168.0.2`
- Data: ...

Data in the previous message is an *ARP Packet*.

## ARP Cache
A ->
Frame:
- From: `aa:aa:aa:aa:aa:aa`
- To: `bb:bb:bb:bb:bb:bb`
- Packet:
	- From: `192.168.0.1`
	- To: `192.168.0.2`
	- Data: ...
B <-

### Seeing your ARP Cache
![[Pasted image 20220307133524.png]]
#### Linux
```
ip n
```
See other machines on your network.

#### Windows
##### Display current ARP table
```
arp -a
```
##### Show ARP table in verbose mode
```
arp -av
```
##### Record an IP and MAC address of a device on a LAN to the ARP table: `ping` it
```
ping 192.168.1.95
arp -a
```
##### Discover all the devices on a LAN: `ping` them all (Adjust the IP of your network)
```
FOR /L %i IN (1,1,254) DO ping -n 1 -w 100 _192.168.1_.%i | FIND /i "Reply"
```
##### Clear ARP Cache
Required: open an elevated cmd, otherwise will have error.
To start elevated cmd, press Windows, search `cmd`, press Crtl + Shift + Enter to start cmd as administrator
```
arp -d
```
