---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Hardware Support for OS Multiplexing]]

In this section, we illustrate an example of how a basic Kernel Scheduler works with the support of hardware.

Consider a [[Building Beta CPU|beta computer]] having a 16 bit counter (hardware)with a frequency of 50Hz that runs asynchronously with the [[Anatomy of the Beta CPU|CPU]]. This counter will be used as a timer for process scheduling.

Upon start-up, the kernel can set `IRQ` signal to point to an arbitrary bit of the counter (assume that hte pointer's output is passed through a rising edge detector so `IRQ` is 1 for 1 clock cycle during a rising edge only).

For example, if it points to the `4`th^{th}th bit:
-   The value of the `4`th^{th}th bit of the counter changes every $0.02 \times 2^{3} = 0.16$ seconds because it takes $0.02$ seconds for the counter to increase by 1.
-   There’s $0.32$ seconds between rising edges.

This means that the `IRQ` value will be `1` **once** every $0.32$ seconds.

If at first the CPU is executing instructions of Program `P1`:

1.  After 0.32 seconds, `IRQ` turns to `1`. This triggers an interrupt, and the control signals will cause the PC will execute the interrupt handler instruction at `XAddr` in the next cycle (and saving the _supposed_ _next_ instruction at `Reg[XP]`).
    
2.  The handler at `XAddr` must _save register states_, branch to the _scheduler_, and resume the program after the scheduler returns. Note that `Reg[XP]` may or may not be the same as when _before_ `BR(scheduler_handler, LP)` is executed.

```cpp
X_addr : ST(R0, save_location) || save register states at an allocated address
ST(R1, save_location+4)
ST(R2, save_location+8)
ST(R3, save_location+12)
....
ST(R30, save_location+30*4) 

CMOVE(kstack, SP) || use kernel stack
BR(scheduler_handler, LP) || branch to the scheduler

|| return instruction from scheduler
LD(save_location,R0) ||  restore register states
LD(save_location+4,R1)   
...
LD(save_location+30*4, R30)

SUBC(XP, 4, XP) || Reduce XP by 4 to re-execute the instruction that was interrupted by the timer
JMP(XP)  || Resume execution
```

> Although not written, `save_location` is a label, representing an address to store P1’s states.

Observation: in this simple example, the handler is written such that it _always branches to the scheduler_. In practice, there are many kinds of hardware interrupts (not just from a timer) that needs to be handled differently depending on its _type_. We will have a hands-on experience about this in Lab 8, and also in the next term.
