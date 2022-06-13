---
aliases: 
tags: 50.0042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Passwords]]
[[Attacking password storage]]

## Property
Tradeoff:
**storage space** VS **computational effort**

## Main operation
Hashing function, mapping input domain to hash domain:
$$H()$$
Reduction function, mapping hash back to input domain:
$$R()$$

Lets initiate a hash chain with $I_1$ as its first input:
$$
I_1 \xrightarrow{H()}
O_1 \xrightarrow{R()}
I_2 \xrightarrow{H()}
O_2 \xrightarrow{R()}
\cdots \xrightarrow{H()}
O_t
$$
After $t$ operations, we get hash output $O_t$.

> If we store only $I_t$ and $O_t$, how can we find $I_t$ for $1 < i \leq t$ ?

Recompute the chain with $I_1$ until we hit $I_i$.