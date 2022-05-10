---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Scheduling multiple interrupts]]

The machine has a fixed ordering of device handling, but will not pre-empt current service. It will only reorder requests in the interrupt queue based on the types of device.

Order depends on [[Handler Priority Level]]