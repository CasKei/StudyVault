---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]

Like [[Multiprocessor System]]s, but multiple systems working together

Clustered systems (e.g: AWS) are multiple systems that are working together. They are usually:

1.  Share **storage** via a *storage-area-network (SAN)*
2.  Provides **high availability** service which survives failures
3.  Useful for **high performance computing**, require special applications that are written to utilize **parallelization**

There are two types of clustering:

1.  **Asymmetric**: has one machine in hot-standby mode. There’s a master machine that runs the system, while the others are configured as slaves that receive tasks from the master. The master system does the basic input and output requests.
2.  **Symmetric**: multiple machines (nodes) running applications, they are monitoring one another, requires complex algorithms to maintain data integrity.