---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Scheduling multiple interrupts]]

## Priority Level
> **Priority level for each interrupt handler can be illustrated using**:
> Higher `p` bits of [[Anatomy of the Beta CPU|PC]] - meaning location of handler in memory matters; it defines the handler's priority level

Some hardware tweaks on [[Anatomy of the Beta CPU|CPU]] is needed to support this feature, but we don't have to dwell too deep into this at this point.

![](https://dropbox.com/s/7w7oy1jyaa5trnq/pc.png?raw=1)

Value `p` depends on how many priority levels you want the mahcine to have, e.g. 3 bits for 8 levels.

This is analogous to what we have learned before. A system two mode: Kernel and user mode, is differentiated only with the MSB of the PC – `1` for Kernel mode (hence enabling the highest privilege) and `0` for user mode.


