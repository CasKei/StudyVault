---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Machine]]
[[Multiplexing]]
[[Hardware Support for OS Multiplexing]]

## Beta Asynchronous Interrupt Hardware
[[Beta Asynchronous Interrupt Hardware]]
Recall **asynchronous interrupt** [[Beta Datapaths|datapath]]:
![](https://natalieagus.github.io/50002/assets/contentimage/beta/irq.png)

One of the inputs that is received by the [[Anatomy of the Beta CPU|CU]] is `IRQ` (1 bit).
In the event of **interrupt**, `IRQ` = 1.
At each CLK cycle, the [[Anatomy of the Beta CPU|CLU]] always checks the value of `IRQ`.

A kernel scheduler will typically configure some system timer to *fire* at some interval. This timer runs asynchronously with the [[Anatomy of the Beta CPU|CPU]] and sets the `IRQ` signal to `1` each time it fires.

The register transfer language that describes what happens in the datapath when `IRQ == 1` is:
```C
if (IRQ == 1 && PC31 == 0):
	Reg[XP] <- PC + 4
	PC <- Xaddr
```

### Note
`IRQ` may turn to be 1 asynchronously.
However, [[Anatomy of the Beta CPU|CLU]] is synchroised with the [[Anatomy of the Beta CPU|CPU]] clock.
Therefore this will only *trigger the interrupt* in the next [[Anatomy of the Beta CPU|CPU]] clock tick.

`IRQ == 0`
- [[Anatomy of the Beta CPU|CLU]] produces all control signals as dictated by `OPCODE` received.

`IRQ == 1`
- [[Anatomy of the Beta CPU|CLU]] *traps* the [[Anatomy of the Beta CPU|PC]] onto interrupt handler located at `XAddr`, by setting `PCSEL` to `100`; so [[Anatomy of the Beta CPU|PC]] points to `XAddr` in the next clock cycle.
- At the same time, it stores the address of the next instruction (`PC + 4`) at `Reg[XP]` (`R30`).
- `R30` is always used to hold the return address in the event of interrupt or illegal operation so that the system knows how to resume the interrupted program later on.
