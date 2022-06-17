---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## System Resources
A system consists of ==finite resources== to be distributed among a number of ==competing processes==. Each type of resource can have several finite instances. E.g.
- CPU cores/cycles
- IO devices
- Access to  [[Week 6 - Files|files]] or memory locations (guarded by [[Critical section solutions|locks]] or [[Sephamores|sephamore]]s, etc)

> A process must **request** a resource before using it and must **release** the resource after using it.
> A process can **request as many resources** as it requires for its task.
> Number of resources requested should not exceed total resources available.

Under normal mode of operation, a process may utilise a resource in only the following sequence:
1. **Request**: Process requests resource. If request cannot be granted immediately, then requesting process must wait.
2. **Use**: Process can operate on the resource
3. **Release**: Process releases the resource

> **Request** and **release** may require [[System calls]], depending on who manages the resources.

## Kernel managed resources KMR
For each use of a KMR, OS checks to make sure processes who requested these resources has been granted allocation.
E.g.
- `request()` and `release()` device
- `open()` and `close()` [[Week 6 - Files|file]]
- `allocate()` and `free()` memory [[System calls]]

```ad-note

Some implementation detail: A typical OS manages some kind of system table (data structure) that records whether each resource is **free** or **allocated**. For each resource that is allocated, the table also records the process to which it is allocated. If a process requests a resource that is currently allocated to another process, it can be added to a **queue** of processes waiting for this resource.
```

> Developers who simply write programs utilising these resources simply make [[System calls]] and need not care about how [[OS Kernel]] manages these resources (abstracted)

## User managed resources UMR
For each use of a UMR, we can guard them using [[Sephamores]] or [[Mutex]]es.
- [[Sephamores]] request and release:
	- `wait()` and `signal()`
- [[Mutex lock]] request and release:
	- `acquire()` and `release()`

```ad-note
Writing these series of `wait()` and `signal()` are defined by developers, and they have to be very careful in writing them else it might result in a [[Deadlock]] situation.
```
