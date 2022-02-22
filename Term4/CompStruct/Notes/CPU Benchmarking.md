---
tags: #50.002
---
[[Comp Struct]]
[[Building Beta CPU]]

We always want a CPU that has a high performance (most instruction per second) at a low cost. Unfortunately there will always be a tradeoff between the two. We can benchmark the quality of a CPU by computing its MIPS (million instruction per second),
$$MIPS = \frac{\text{Clock Rate}}{CPI}$$
Where $CPI$ means "Clocks per Instruction".

Although it is common to judge a CPU’s performance from its _clock rate_ (cycles per second, typically ranging between 2-4 GHz per core for modern computers), we also need to consider another metric called the $CPI$, that is the ==_average clock cycles_ used to execute a single instruction.==

In beta ISA, each instruction requires only 1 clock cycle to complete (atomic execution). It is possible for other ISA to take more than 1 clock cycle _on average_ to complete an instruction.

Typically, one will choose a particular program (with fixed number of instructions) for benchmarking purposes, and **the same benchmark program** is run on different CPUs with potentially different Clock Rate and CPI.

The ==higher== the MIPS, the ==faster== it takes to run the benchmark program. Therefore we can say that a CPU with the highest MIPS has the ==best== performance.