---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5, 6 - Deadlock]]

## Resource allocation graph
[[Deadlock]]s can be described more precisely in terms of a directed [[Graphs|graph]] called a **system resource-allocation graph**.

A set of vertices $V$ that is partitioned into 2 different types of ==nodes==:

| Circle           | Square                                      |
| ---------------- | ------------------------------------------- |
| Active processes | All [[System resource]] types in the system | 

Directed ==edges==:

| Request edge                                             | Assignment edge                                                                  |
| -------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Process to resource nodes: process requesting a resource | Resource to Process nodes: assignment/allocation of that resource to the process | 

==Dots==: resource *instances* within each resource type node

## E.g. 1
Suppose a system has the following *state*:

| Active Processes | Types of resources                                                       | Requests                                             | Allocation (per instance) |
| ---------------- | ------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------- |
| 1, 2, 3          | 1: 1 instance <br> 2: 2 instances <br> 3: 3 instances <br> 4: 1 instance | P1 requests R1<br> P2 requests R4<br> P3 requests R2 | R1 allocated to P2<br> R4 allocated to P3 <br> R2 allocated to P1 and P2 (1 instance each)                          |

Graph:
![[enrpjpqs.bmp]]

If the graph **has no cycle**: deadlock will **never** happen.

If there’s _at least_ 1 cycle:

-   If **all** resources has exactly **one** instance, then **deadlock** (deadlock necessary and sufficient condition)
-   If cycle involves only **a set** of resource types with **single** instance, then **deadlock** (deadlock necessary and sufficient condition)
-   Else if cycle involves a set of resource types with **multiple** instances, then _maybe_ deadlock (we can’t say for sure, this is just a necessary but not sufficient condition)

In Example 1 diagram above, the **three** processes are deadlocked (process and resource is shortened as `P` and `R` respectively):

-   `P1` needs `R1`, which is currently held by `P2`
-   `P2` needs `R4`, which is currently held by `P3`
-   `P3` needs `R2`, which is currently held by either `P1` or `P2`
    
    > Neither process can give up their currently held resources to allow the continuation of the others resulting in a deadlock.


## E.g. 2
Now consider the another system state below. Although _there are cycles_, this is **not** a deadlocked state because `P1` might eventually release `R2` after its done, and `P3` may acquire it and complete. Finally, `P2` may resume to completion after `P3` is done.

![](https://natalieagus.github.io/50005/assets/images/week5/3.png)
