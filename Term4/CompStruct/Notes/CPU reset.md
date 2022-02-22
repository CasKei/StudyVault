---
tags: #50.002
---
[[Comp Struct]]
[[Building Beta CPU]]

Finally, the beta processor accept external `RESET` signal that can reset the value of the `PC`. 
The signal `RESET` must be `1` for ==several clock cycles== in order to ensure that the values affected by `RESET` propagates throughout the entire circuit. 
During the period where `RESET = 1`, we need to make sure that `WR` is `0` so that we ==do not accidentally overwrite the content of the physical memory.==

![[Pasted image 20220221092836.png]]
