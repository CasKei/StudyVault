---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]

> **Effective Interrupt Load**
> Imposed by devices to the [[Anatomy of the Beta CPU|CPU]] is computed by
> $$\text{Maximum frequency of each device interrupt }\times \text{ its own service time}$$

We can easily compute the max frequency of each device:
-   Keyboard: 100/s
-   Disk: 500/s
-   Printer: 1000/s

The load % from each device is therefore:
-   Keyboard: $100 \times 0.0008 = 0.08 = 8\%$
-   Disk: $500 \times 0.0005 = 0.25 = 25.0\%$
-   Printer: $1000 \times 0.0004 = 0.4 = 40.0\%$

The total Interrupt load of these devices on the CPU is 73%. The remaining fraction, 27% is what is left for processes to use to do _work_ (computation).

The computer will not be able to run any other processes if the Interrupt load reaches 100 %.