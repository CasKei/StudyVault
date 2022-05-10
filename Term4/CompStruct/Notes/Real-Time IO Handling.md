---
aliases: latency
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]

## Timeline at interrupt request
![](https://www.dropbox.com/s/h0e8epak5kz505o/rth.png?raw=1)

When IO interrupt requests are made by devices, they may not be immediately serviced by the [[OS Kernel]].

Timeline starts from when a particular interrupt request is first made to the moment it is serviced.

Each interrupt request usually have a **deadline**, and the Kernel has to service the request before the deadline.

For example, the Kernel has to service each keyboard input interrupt request quick enough so as to give the experience of a responsive system.

## Latency
> **Latency**
> The amount of elapsed time from when interrupt is first requested up until the Kernel BEGINs servicing it.

The Kernel scheduler in the kernel has to ensure that the interrupt request is sreviced before its deadline.

The amount of latency affects how "real-time" the machine reacts. The shorter the latency, the more responsive it will seem.
