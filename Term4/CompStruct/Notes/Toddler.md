---
tags: #50.002
---
[[Comp Struct|50.002]]
[[FPGA]]
## Seq Logic Module
DFF `R1`: triggered at each positive clock edge
- CL: applies some function f to its input `QR1`
- At first cycle, value loaded to `R1` is `INIT`, and hence at the signal at `CL out` = f(`INIT`).
- then it becomes f(f(`INIT`))
- and so on.

Need to ensure DD obeyed, meaning t1 and t2 timing constriants are satisfied.
- Not an issue typically unless intensive computations in CLU such that tpd too large and viotates t2
- Alchitry lab will warn you if timing contraints are violated, means you need to break down the CLU into smaller parts and adding more DFFs in between

To make things simple, let's use the 8 bit RCA made in part 1 to increment `INIT` by `2` at each clk
- `cout` grounded
- `CL out` output. No external input.
- Add `2` to `INIT` value at each clk
- if we connect each bit of `CLout` to an LED, output sequence should observe `2,4,6,8,...`

## Declaring and Using DFF
Lucid has a built in DFF + the small reset mux built into it that you can use by declaring each unit with the keyword `dff` *before the always block*.

`dff` has 2 impt terminals `.d` for input and `.q` for output.
Simply connect them with the adder.