---
tags: #50.002
---
[[Comp Struct]]

## Ripple carry adder
N-bit
Why: we are not going to use full adders for every single bit, so if there is a device available for adding n-bit numbers: noice.

Tis a Cascade of [[Anatomy of the Beta CPU#Adder Subtractor|full adders]]

4 bit RCA => 4 FA

Use one FA for each digit

## Carry select

## Carry lookahead
N-bit adder needs N FA and hence Ntpd which is a massive delay

Carry for each FA is going to generate simultaneously

$$S = A \oplus B \oplus C_{in}$$
$$C_{i+1} = (A_i \oplus B_i)C_{in} + A_iB_i$$
Carry propagate: $P_i = A_i \oplus B_i$
Carry generate: $G_i = A_i \cdot B_i$

$$
\begin{align}
C_{i+1} &= P_i \cdot C_i + G_i\\
C_2 &= P_1 \cdot C_1 + G_1
\end{align}
$$
$$\begin{align}
C_3 = P_2 (C_2) + G_2 &= (A_2 \oplus B_2)C_2 + A_2 \dot B_2\\
&= (A_2 \oplus B_2)(P_1 \cdot C_1 + G_1)  + A_2 \dot B_2\\
&= P_2(P_1 \cdot C_1 + G_1)+ G_2\\
etc
\end{align}$$

![[Pasted image 20220302090300.png]]


## Kogge Stone
Every black is a dot operator
This is 4 bit
![[Pasted image 20220302090706.png]]
8 bit
![[Pasted image 20220302090837.png]]
16 bit
![[Pasted image 20220302090949.png]]

every dot feeds at most 2  outputs
fanout is 2 other dot operators at most

The _radix_ of the adder refers to how many results from the previous level of computation are used to generate the next one.



## Brent Kung
8 bit
![[Pasted image 20220302091449.png]]
16 bit
![[Pasted image 20220302091502.png]]
2 comes from 1 and 3
4 comes from 3 and 5
5 from 4 and 6


bad: a dot feeds way more than 2: up to 4
Like the 7 bit
Fanout is high