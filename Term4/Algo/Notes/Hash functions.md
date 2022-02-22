---
aliases: hash function
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

Recall: [[Intro to hashing]]


## Division Method
Goal: To create a hash function $h: K \to \set{0, 1, \dots, m-1}$

Assumptions: $K$ is a set of integers, [[Hash Table]] has $m$ slots
> Define $h$ by the map $$h(k) = k \% m$$
> where % denotes remainder of k/m

Example 1: K: 0 to 99999, m=10
h(k) = last digit of k
e.g. h(43564) = 4

Example 2: K: -1000 to 1000, m = 137
h(k) = remainder of k when divided by 137
e.g. h(743) = 58

Initialize 𝐴 as a hash table with 5 slots, and suppose its hash function is created using the division method. Suppose we insert the following integers 2, 7, 5, −1, −8,4,11 into 𝐴.
Draw the final hash table `A` after these insertions:
![[Pasted image 20220221142603.png]]

### Comments on [[Designing hash functions#Comments on Hash functions Division Method division and Hash functions Multiplication Method multiplication method|design]]
Recall `m` is the number of slots in the [[Hash Table]]
- Avoid letting `m` be a power of 2 unless you know what you are doing (e.g you know the distribution of the key values)
	- Data is usually stored in chunks where the number of bits in each chunk is a power of 2
	- If $m=2^p$, then the hash values depend only on the last `p` bits of the key values, which is typically not uniformly distributed.
- Values close to powers of 2 may yield surprising effects
	- e.g. If 𝐾 = {8-character password ASCII strings as base-128 integers}, and if $𝑚 = 2^7 − 1 = 127$, then all permutations of the password string would be hashed to the same slot. (Why?)

## Multiplication Method
Goal: To create a hash function $h: K \to \set{0, 1, \dots, m-1}$

Assumptions: $K$ is a set of ==real numbers==, [[Hash Table]] has $m$ slots

> Define $h$ by the map 
> $$h(k) = \lfloor m(k\beta \%1) \rfloor$$
> where $\beta > 0$ is a positive constant,
> - $k\beta \%1$ denotes the 'fractional' part of $k\beta$, i.e. the part of the number that comes after the decimal point
> - ![[Pasted image 20220221142914.png]]

Multiply the fractional part of $k\beta$ by $m$, then take its floor.

![[Pasted image 20220221142948.png]]

Initialize `𝐴` as a hash table with 5 slots, and suppose its hash function is created using the multiplication method with constant $5.3$. Suppose we insert the following real numbers $1.1$, $2.2$, $3.3$, $4.4$, $6.6$ into `𝐴`, in this order. Exercise: Draw the final hash table `𝐴` after these insertions.
![[Pasted image 20220221143041.png]]

Initialize `𝐴` as a hash table with $1000$ slots, and suppose its hash function is created using the multiplication method with constant $0.01$. Which slots of `𝐴` should the following numbers $1234567$, $4194091$, $9205832$, $1.2377$ be hashed to?
![[Pasted image 20220221143141.png]]

### Comments on [[Designing hash functions#Comments on Hash functions Division Method division and Hash functions Multiplication Method multiplication method|design]]
Recall `m` is the number of slots in the [[Hash Table]]
- The value of `m` is not critical. Powers of 2 can be used for `m`
	- Instead the choice of $\beta$ is more important
- In course textbook, the value $\beta$ is restricted to $0<\beta<1$
- However this still makes sense even if $\beta > 1$ or $\beta < 0$.
- For this course we shall allow $\beta$ to be any strictly positive value.
- A suggested 'good default' value for $\beta$ is $\dfrac{\sqrt{5} - 1}{2} \approx 0.618034$
- This method is slower than  [[Hash functions#Division Method|division]] method.

## Mid-Square Method
Let `k` be the 4-digit integer corresponding to the last 4 digits of your student id,
square it,
then take the 4th and 5th digit from the right to form a 2 digit integer.
This is now your hash value.


