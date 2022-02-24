---
tags: #50.004
---
# 50.004 HW Set 3
## Cassie Chong 1005301 CL01
## 1) Hash Functions
### i)
Let $h : S → \set{0, 1, . . . , 126}$ be a hash function given by $h(k) = (k \text{ mod } 127)$, where the domain S consists of all non-empty ASCII strings, treated as base-128 integers. Will the ASCII string ‘DEADLINE’ and its permutation ‘DDEEALIN’ be mapped to the same hash value? Justify your answer. [3]
***
ASCII-encoding treats strings as base 128 integers, that is base $2^7$. The mod in the hash function is using 127, that is $2^7 - 1$.
Performing the hash by dividing $127$, the mod is found with the remainder. 
Hashed term at $i$th bit is $a\cdot (128)^i$ where $a$ is ASCII encoding.
Hashed terms are added.
For the $i$th term where $a$ is the ASCII encoding of the character,
$$
\begin{align}
a(128^i)\text{ mod }127 &= a(128^{i-1})(128 \text{ mod }127)\text{ mod }127 = a(128^{i-1}) \text{ mod }127\\
&= a(128^{i-2})(128 \text{ mod }127)\text{ mod }127 = a(128^{i-2}) \text{ mod }127\\
&\vdots\\
&= a(128 \text{ mod }127) = a
\end{align}
$$
For a string like ABC, its hashed value will be its own encoding values added together.
This would be the same as any permutation of ABC.

Hence for DEADLINE and DDEEALIN, by a similar argument, hashed values are the same.
<br>
### ii)
Initialize $A$ has a hash table with 100 slots, and assume we know that all possible key values that we could insert into A are 3-digit integers. We want to design a hash function for A, using either the mid-square method (take the middle two digits of the 6-digit expression after squaring), or the multiplication method with constant 0.2. Now, suppose $K = \set{162, 195, 240, 277, 352, 375}$ is the actual set of key values that we would like to insert into A. For this specified set of key values $K$, compute their associated hash values for both methods. Which of these method (mid-square method versus multiplication method with constant $0.2$) is better for inserting $K$ into $A$? Justify your answer.[2]
***
A[0:99]
All possible key values are 3 digit int 

Midsquare: middle 2 digits of 6 digit after squaring
Multiplication method: $m = 6$, $\beta = 0.2$

| Key val | Square | Mid (==hash val==) | $k\beta \% 1$ (fractional part) | prev part $\times m$, floor ==(hash val==) |
| ------- | ------ | -------------- | ------------------------------- | -------------------------------------- |
| 162     | 026244 | 62             | 0.4                             | $\lfloor0.4 \times 6\rfloor = 2$       |
| 195     | 038025 | 80             | 0                                |  0                                      |
| 240     | 057600 | 76             |  0                               |   0                                     |
| 277     | 076729 | 67             | 0.4                                | $\lfloor0.4 \times 6\rfloor = 2$                                       |
| 352     | 123904 | 39             | 0.4                                |  $\lfloor0.4 \times 6\rfloor = 2$                                      |
| 375     | 140625 | 06             | 0                                |    0                                    |

As the multiplication method in this case leads to many key values being hashed to the same hash values of 0 and 2, it is not a good choice to do this method as there are multiple collisions.
The mid-square method hashes each key value to a unique hash value and is the better option without collisions in this situation.
<br>
## 2)
Design an algorithm that takes as its two inputs a singly linked list $L$ with $n$ elements, and a positive integer value $k$, and returns as its output the total number of pairs of elements whose sum of their key values is divisible by $k$. Assume that every element $x$ in $L$ has an integer key value $x.key$. Here, a pair shall mean a set with two elements, which means that the order of the elements in a pair does not matter. (If $\set{x, y}$ is a pair, then $\set{y, x}$ is the exact same pair; so $\set{x, y}$ and $\set{y, x}$ should be counted only once if $x.key$ + $y.key$ is divisible by $k$.) Please present your algorithm in pseudocode, and explain why your algorithm works as intended. Your algorithm should have time complexity $O(n)$ to have full credit, but a correct algorithm with time complexity $O(n^2)$ will still get most of the credit.

For example, if $k = 10$, and if the singly linked list $L$ has 4 elements $a, b, c, d$, whose key values are $2, 12, 8, 18$ respectively, then your algorithm should return the output $4$, which corresponds to the 4 pairs of elements $\set{a, c}, \set{a, d}, \set{b, c}, \set{b, d}$. 

As another example, if $k = 10$, and if the singly linked list $L$ has 3 elements $a, b, c$, whose key values are $5, 5, 5$ respectively, then your algorithm should return the output $3$, which corresponds to the $3$ pairs of elements $\set{a, b}, \set{a, c}, \set{b, c}$. Note that elements of a set must be distinct. [5]
***



## 3)
Design an algorithm that takes as its two inputs a singly linked list $L$ with $n$ elements, and a non-negative integer $k$, and returns as its output the key value of the $k$-th last element in $L$. If the $k$-th last element does not exist, your algorithm should return $NIL$. Here, the $0$-th last element refers to the last element $x$ in $L$, which must satisfy $x.next = NIL$, while the $k$-th last element for $k = 1$ refers to the “second last” element. Please present your algorithm in pseudocode. Your algorithm must have time complexity $O(n)$ and space complexity $O(1)$. Also, your algorithm must use at most one for/while loop. (To be clear, this means that if part of your pseudocode already uses a for-loop, then to get full credit, you cannot use another for-loop or while-loop. Similarly, if part of your pseudocode already uses a while-loop, then to get full credit, you cannot use another for-loop or while-loop. A solution receiving full credit will not use any iterated for-loops or iterated while-loops.) [5]

Hint 1: By space complexity, we refer to the additional space required for anything you initialize beyond the inputs. Having a space complexity of $O(1)$ is not the same as having a space complexity of $O(k)$. If you initialize a new linked list with $k$ elements, then you would have a space complexity of $O(k)$. What could take up a space complexity of $O(1)$?

Hint 2: It is possible to design an algorithm that uses exactly one while-loop and no for-loops.
***

## 4)
Initialize a hash table $A$ with 5 slots, whose hash function is created using the division method. Assume that collisions are resolved by chaining. Also, assume that the load factor cannot exceed $\gamma = 0.8$, and that re-hashing is done by doubling. Suppose we insert the following twelve integer key values into $A: 2, 3, 6, 7, 10, 21, 24, 28, 30, 32, 35, 39$ (in this given order).
(Hint: When drawing a hash table, you should draw all slots, even if some slots contain the NIL object. Remember also to indicate the indices for your hash table.)
### i)
Draw A immediately before A is re-hashed for the second time. [2]
### ii)
Draw the final hash table after the insertion of all eleven key values. [3]
***
i) 
![[Pasted image 20220224180426.png]]
ii)
![[Pasted image 20220224153259.png]]
## 5)
Let $A$ be an empty open address hash table with $30$ slots. Suppose we insert the key values $2, 32, 62, 92, 122$ into $A$ in this given order. For each of the three following probing strategies, please give all non-empty slots of the hash table with their corresponding key values. 
### i)
Suppose the hash function $h(k, i)$ is defined using linear probing, with auxiliary hash function $h'(k) = (k\text{ mod }30)$. [1]
### ii)
Suppose the hash function $h(k, i)$ is defined using quadratic probing, with auxiliary hash function $h'(k) = (k\text{ mod }30)$ and auxiliary constants $c_1 = 1, c_2 = 2$. [2]
### iii)
Suppose the hash function $h(k, i)$ is defined using double hashing, with two auxiliary hash functions $h_1(k) = (k\text{ mod }30)$ and $h_2(k) = 1 + (k\text{ mod }11)$. [2]
***
![[Pasted image 20220224151357.png]]