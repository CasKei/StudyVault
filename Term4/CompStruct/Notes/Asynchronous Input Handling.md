---
aliases:
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]

## How to pass new inputs
Since I/O devices are asynchronous, an efficient way has to be devised to pass new inputs to the [[Anatomy of the Beta CPU|CPU]] to be stored in the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

> **Asynchronous input**
> We cannot guarantee that there's any process that asks for an input at the exact moment that new input is detected by the I/O devices.
> Therefore, the [[OS Kernel]] has to temporarily store these new inputs in the Kernel Space until there's some process that asks for it (and then it can be cleared from the Kernel Space).

## When device requests for interrupts
Most modern system is **interrupt-driven**. That is, devices may request for **interrupts**:
- Any I/O device may request for an I/O interrupt; in the presence of new input or update, etc.
- This will interrupt the execution of the current process in the [[Anatomy of the Beta CPU|CPU]], causing the [[Anatomy of the Beta CPU|PC]] to switch to `XAddr` (interrupt handler). Recall [[Asynchronous Interrupt Handler]].

The interrupt handler does the following:
- Saves states of interrupted process
- Examines the cause of the interrupt
- Branch to appropriate I/O interrupt handler (if interrupt caused by I/O device)

The **device-specific** I/O interrupt handler will fulfil the request, e.g. fetching new input from the device and putting it to a dedicated buffer in the kernel space. This value stays in the kernel buffer until a related [[Supervisor Call|SVC]] is made.

When an [[Supervisor Call|SVC]] is made, the Kernel fetches the requested item from the buffer (if any) and put it in `Reg[R0]` before returning to the originating process.