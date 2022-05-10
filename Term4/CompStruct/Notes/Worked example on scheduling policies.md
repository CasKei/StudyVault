---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]
[[Scheduling multiple interrupts]]
[[Weak, non-preemptive measure]]
[[Strong, preemptive measure]]

Each scheduling policy has its own pros and cons. Non-preemptive Kernel is simpler to develop, but without it the device with the slowest service time constraints response to the fastest devices. 

With preemption, [[Real-Time IO Handling|latency]] for higher priority devices is not affected by service times of the lower priority devices. However, this additional feature will complicate the Kernel code. 

We will use some examples to understand how each policy works, and justify whether there's any one that is better than the other.

## Setup
Consider a computer that has three devices: disk, keyboard and printer. 
Each has the following specs for service time, average period, and deadline: 

| Device   | Service Time (ms) | Deadline (ms) | Period (ms) |
| -------- | ----------------- | ------------- | ----------- |
| Keyboard | 0.8               | 3             | 10          |
| Disk     | 0.5               | 3             | 2           |
| Printer  | 0.4               | 3             | 1           |

## Case 1: Without Scheduling
> Without any scheduling measure, the worst case latency seen **by each device** is the total service time of the other devices, as the interrupt requests *can arrive in any order.*

| Device   | Service Time (ms) | Deadline (ms) | Period (ms) | Worst-case Latency (ms) |
| -------- | ----------------- | ------------- | ----------- | ----------------------- |
| Keyboard | 0.8               | 3             | 10          | 0.9                     |
| Disk     | 0.5               | 3             | 2           | 1.2                     |
| Printer  | 0.4               | 3             | 1           | 1.3                     |

## Case 2: Weak, Non-Preemptive Policy
[[Weak, non-preemptive measure]]
Assume now we have the following hardware priority ordering: **Disk $>$ Printer $>$ Keyboard.**

Recall that in this weak policy, we
* **Cannot interrupt** whatever service that is currently going on, but 
* Can **re-order** other interrupt requests in the queue

The **worst case** latency for each device is:

| Device   | Service Time (ms) | Deadline (ms) | Period (ms) | Worst-case Latency (ms) |
| -------- | ----------------- | ------------- | ----------- | ----------------------- |
| Keyboard | 0.8               | 3             | 10          | 0.9                     |
| Disk     | 0.5               | 3             | 2           | 0.8                     |
| Printer  | 0.4               | 3             | 1           | 1.3                     |

*   The worst case latency for *disk* is 0.8ms despite having the highest priority, because it has to account for service time for the *keyboard*, if the keyboard service has just started when interrupt by disk arrives. 
*  The worst case latency for *printer* is 1.3ms because it has to take into account the scenario that the *keyboard* has just started when the interrupt by *printer* and *disk* arrive. 
	> The printer, which has lower priority than disk will have to wait for both disk and keyboard to finish execution before it can be serviced. 
*  The worst case latency for keyboard, with the lowest priority is the service time for *disk* + *printer*.

## Case 3: Stricter Deadline with Weak Policy
[[Weak, non-preemptive measure]]
Suppose the system requires a stricter **deadline** as shown in the table below. 
The hardware priority ordering: **Disk $>$ Printer $>$ Keyboard** with *weak policy* results in the following worst-case latency:

| Device   | Service Time (ms) | Deadline (ms) | Period (ms) | Worst-case Latency (ms) |
| -------- | ----------------- | ------------- | ----------- | ----------------------- |
| Keyboard | 0.8               | 1.1           | 10          | 0.9                     |
| Disk     | 0.5               | 0.8           | 2           | 0.8                     |
| Printer  | 0.4               | 0.7           | 1           | 1.3                     |

We can see that the deadline for Disk will not be met, despite having the highest priority:
* Its max latency is 0.8ms, and its service time is 0.5ms 
* Adding the two, we have 1.3ms of (worst case) total time to service the disk. This violates the deadline that's set at 0.8ms. 

Therefore the weak, non-pre-emptive policy will not work for this specification anymore. 
> There's a need to somehow pre-empt the keyboard when the interrupt request for disk arrives so that the disk will not miss its deadline (see next section).

## Case 4: Strong, Pre-emptive Policy
Suppose we have the following interrupt handler priority ordering: **Disk handler $>$ Printer  handler $>$ Keyboard handler**. 

The worst-case latency for each device is now:

| Device   | Service Time (ms) | Deadline (ms) | Period (ms) | Worst-case Latency (ms) |
| -------- | ----------------- | ------------- | ----------- | ----------------------- |
| Keyboard | 0.8               | 1.1           | 10          | 0.9                     |
| Disk     | 0.5               | 0.8           | 2           | 0                       |
| Printer  | 0.4               | 0.7           | 1           | 0.5                     |

The disk has *zero* [[Real-Time IO Handling|latency]] because pre-emption is enabled. 

The *keyboard* with the lowest priority still has to wait for the disk and printer to *complete* regardless.

The interrupt requests from these devices are recurring with certain frequency. For example, the keyboard interrupt occurs once every 10ms, and so on. 

We can draw the timeline of these interrupts as follows:
![](https://dropbox.com/s/vn644mg6ifqnqd1/irqstimeline.png?raw=1)

Since the _disk_ has the highest priority, it will be serviced first. Once finished, the _printer_ will be serviced.

After both _disk_ and _printer_ are serviced, the _keyboard_ is serviced at `t=0.9`. However, it will be interrupted by the printer at `t=1`. Therefore, the keyboard service time is spread out due to interrupts from printer and disks:
![](https://dropbox.com/s/5wodlj3hwpx9ltm/interruptsvc.png?raw=1)

The keyboard service time is spread out (red region) due to interrupts from printer and disks

## Missing Deadline
The strong priority ordering Disk > Printer > Keyboard as explained above **does not** fulfil the deadline for Printer or Keyboard, since the worst-case latency + service time for each Printer and Keyboard exceeds their deadline. What will be the **minimum deadline** for printer and keyboard in this case, so that the strong priority ordering of Disk > Printer > Keyboard can fulfil all deadlines?

