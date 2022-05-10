---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Scheduling multiple interrupts]]

## Recurring Interrupts
Some interrupts may happen periodically or at a bounded rate.

e.g. a system autosave feature that requires periodic disk writes, periodic timer, maximum mouse interrupt per second, etc.

Consequence: If higher priority interrupts happen at high rate, requests with lower priorities might be interrupted repeatedly - potentially resulting in **starvation**.
