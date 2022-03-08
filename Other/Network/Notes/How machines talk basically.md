---
tags: 
---
[[Network Fundamentals]]

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

Both machines store the correspponding [[Mac and IP]] in their [[ARP cache]] (Address Resolution Protocol) cache for future use.