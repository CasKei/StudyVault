---
aliases: 
tags: 50.002, 50.005
---
[[Comp Struct|50.002]]
[[50.005 Computer System Engineering|50.005]]
[[Asynchronous Handling of IO Devices]]
[[Asynchronous Input Handling]]
[[Real-Time IO Handling]]
[[Hardware Interrupt]]

1.  If there’s more than one I/O interrupt requests from multiple devices, the Kernel may decide which interrupt requests to service first.
2.  When the service is done, the Kernel scheduler may choose to resume the user program that was interrupted.

The computer is connected to multiple IO devices.
Each device is capable of making asynchronous interrupt requests. Whenever multiple interrupt requests are invoked, [[OS Kernel]] has to decide how to schedule these interrupt requests.

## Policies
2 policies to handle IO interrupts.
- [[Weak, non-preemptive measure]]
- [[Strong, preemptive measure]]

## Setting Handler Priority Level
[[Handler Priority Level]]

## Recurring Interrupts
[[Recurring interrupts]]

## Worked Example
[[Worked example on scheduling policies]]

