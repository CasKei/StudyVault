---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 5 - Process Synchronisation]]
[[Java synchronisation]]

## Java Static Locks
It is also possible to declare `static` methods as **synchronized**. This is because, along with the locks that are associated with object **instances**, there is a single class lock associated with **each** class.

The class lock has its own queue sets. Thus, for a given class, there can be several object locks, one per object instance. However, there is only one (static) class lock.