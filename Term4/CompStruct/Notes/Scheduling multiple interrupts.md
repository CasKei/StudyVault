---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Asynchronous Handling of IO Devices]]
[[Asynchronous Input Handling]]
[[Real-Time IO Handling]]

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

