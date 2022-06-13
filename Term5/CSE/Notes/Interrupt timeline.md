---
aliases: interrupt handling process
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]
[[Hardware Interrupt]]

## Summary
**Interrupt-driven** procedure of [[Asynchronous Input Handling|asynchronous IO handling]] during [[Hardware Interrupt]]:
![](https://natalieagus.github.io/50005/assets/images/week1/9.png)

Notes:

1.  I/O Devices: External I/O Device, e.g: printer, mouse, keyboard. Runs asynchronously, capable of being “smart” and run its own instructions.
2.  [[Device Controller]]: Attached to motherboard. Runs asynchronously, may run simple instructions. Has its own buffers, registers, and simple instruction interpreter. Usually transfer data to and fro the I/O device via standard protocols such as USB A/C, HDMI, DP, etc.
3.  Disk Controller: Same as device controller, just that it’s specific to control Disks

![[Pasted image 20220520153458.png]]

## Receiving asynchronous input
From the figure above, you may assume that at first the CPU is busy executing user process instructions. At the same time, the device is _idling_.

### Step 1
Upon the presence of external events, e.g: mouse `CLICK()`, the device **records** the input.

-   This triggers **step 1**: The I/O device sends data to the [[Device Controller]], and **transfers** the data from the **device buffer** to the **local buffer of the device controller.**

### Step 2
When I/O transfer is complete, this triggers **step 2**: the [[Device Controller]] makes an **interrupt request** to signal that a _transfer is done (and data needs to be fetched)_.

- The simplest way for the [[Device Controller]] to raise an interrupt is by asserting a signal on the interrupt request line (this is why we define I/O interrupts as hardware generated)

### Step 3
The interrupt request line is sensed by the CPU at the beginning of each instruction execution, and when there’s an interrupt, the execution of the **current user program is interrupted.**

-   Its states are **saved**[2](https://natalieagus.github.io/50005/os_notes/week1_resource#fn:3) by the entry-point of the interrupt handler,
-   Then, this handler determines the **source** of the interrupt (be it via Vectored or Polling interrupt) and performs the necessary processing.
-   This triggers **step 3**: the CPU executes the proper I/O service routine to transfer the data **from** the local device controller buffer **to** the physical memory.

### Step 4
After the I/O request is serviced, the handler:

1.  **Clears** the interrupt request line,
2.  **Performs** a state restore, and executes a **_return from interrupt_** instruction (or `JMP(XP)` as you know it from 50.002).

## Consuming the input
Two things may happen from here after we have stored the new input to the RAM:
1.  If there’s no application that’s currently waiting for this input, then it might be temporarily stored somewhere in kernel space first.
2.  If there is **any application** that is waiting (blocked, like Python’s `input()`) for this input (e.g: mouse click), that process will be labelled as **ready**. For example, if the application is blocked upon waiting for this new input, then the_ system call returns. **We will learn more about this in Week 3.**

**One thing is clear**: in an interrupt-driven system, upon the presence of new input, a [[Hardware Interrupt]] occurs, which invokes the [[Asynchronous Interrupt Handler|interrupt handler]] and then the interrupt service routine to service it. **It does not matter whether any process is currently waiting for it or not**. If there’s a process that’s waiting for it, then it will be scheduled to resume execution since its system call will **return** (if the I/O request is blocking).