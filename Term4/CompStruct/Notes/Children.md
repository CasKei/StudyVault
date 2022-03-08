---
tags: #50.002
---
[[Comp Struct|50.002]]
[[FPGA]]

Mainly shows how to handle I/O units, namely *reset*, *input button presses*, and *rounting output to external LEDs*.
We will utilise all the parts we have learned before in [[First FPGA Project]], [[Toddler]], [[Synchronous logic for FPGA]] (CL, Seq, DFF and FSM, usage of counter to slow the clk, and ROM.)

Finally we try to write our own constraints `.acf` file to connect our board to the external LED outputs (or button/switch inputs).