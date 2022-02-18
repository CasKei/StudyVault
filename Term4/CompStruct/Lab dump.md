---
tags: #50.002
---
## Comparator
32 bit compare
**Output**: `0` or `1`

Required:
`A`-`B`=`S` (done in adder/subtractor)

**Inputs** from adder/subtractor
-   `Z` which is `1` when the `S` outputs are all `0`
-   `V` which is `1` when the addition operation overflows (i.e., the result is too large to be represented in 32 bits), and
-   `N` which is `1` when the `S` is negative (i.e., S31 = 1).

**Control signal**
- `ALUFN1`
- `ALUFN2`

| ALUFN1 | ALUFN2 | Comparison |
| ------ | ------ | ---------- |
| 1      | 0      | =          |
| 0      | 1      | <          |
| 1      | 1      | <=           |

The combination of control signals tells what operation (comparison) to do

`=` : Output is 0: pass `z=1` 
`<`: `V` overflowed ==XOR== `S` is negative
`<=`: Output all `0` ==OR== (`V` overflowed ==XOR== `S` is negative)

**Performance**
-   The `Z`, `V` and `N` inputs to this circuit can only be calculated by the adder/subtractor unit **after** the 32-bit add is **complete**.
- Takes tpd of adder and compare

**Do**: A-B and get S as output.


E.g. A=0, B=0
A-B: Z=0, V=0, N=0
If do `=`: If output is 0, pass z=1 -> `z=1` -> `=` is `1`
If do `<`: overflow XOR negative -> `0`
If do `<=`: Output all 0 OR ( overflow XOR negative) -> `0`

E.g. A=01, B=10
A-B: S=11, Z=0, V=1, N=1
`=`: Output is not 0: -> `0`
`<`: V XOR N -> `1`
`<=`: Z OR (V XOR N) -> `1`

E.g. A=(3)011, B=(2)010
A-B: S=1, Z=0, V=0, N=0
`=`: S!=0 -> `0`
`<`: overflow XOR neg -> 0 XOR 0 -> `0`
`<=`: Output all 0 OR ( overflow XOR negative) -> `0`
