---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]
[[System resource]]

## Deadlock Avoidance
> We need to spend some time to perform an algorithm to **check BEFORE granting** a resource request, ==even if the request is valid and the requested resources are now available.==

This algo is called the [[Banker's Algorithm]]. Its job is to **compute** whether or not the current request will lead to a deadlock.
- If yes, reject request for resource
- If no, grant request

This algorithm is run **each time** a process requests the shared resources.
