---
aliases: 
tags: #50.004
---
[[Algo]]
[[Algo week 5

## Why [[Hash Operations]] are usually fast
> Observation:
> If the number of elements is at most some ratio of the number of slots in the [[Hash Table]], i.e. $n=O(m)$, then $\alpha$ is $\frac{O(m)}{m} = O(1)$, so the average case complexity is $\Theta(1+\alpha)=O(1)$. 

-> How do we keep the number of slots to be at least the number of elements in the [[Hash Table]] `A`?
i.e. how to ensure that $n=O(m)$ as $n$ grows?
[[Re-hashing]]!

## What is re-hashing
> Let $\gamma > 0$ be a fixed constant.
> For every new element to be inserted into a [[Hash Table]] `A`, check  its [[Hash Operations|load factor]] $\alpha=\frac{n}{m}$
> where $n=(\text{number of elements already in A})+1$ and $m=(\text{current number of slots in A})$.
> - $\alpha \leq \gamma$: [[Hash Operations#Operations on a Hash Table A|insert]] new element as per normal.
> - $\alpha > \gamma$: re-hash `A` intoa new [[Hash Table]] `A'` with $>m$ slots (usually $2m$), followed by the usual insertion of new element into this new [[Hash Table]] `A'`

Intuition: resize the [[Hash Table]] when it gets too full!

## How to build re-hashed table
We need a new [[Hash functions|hash function]]. modified from the original $h$.
==Cohort class cont.

## Rehash to what size?
Let $\gamma > 0$ be a fixed constant.
Let `A` be a [[Hash Table]].

**Question**:
If the [[Hash Operations|load factor]] $\alpha=\frac{n}{m}$ of `A` would exceed $\gamma$ after the insertion of a new element,
i.e. $\dfrac{n+1}{m} > \gamma$,
then what should be the new number $m'$ of slots in the new [[Hash Table]] `A'` be?

**Intuition**:
Re-hashing a [[Hash Table]] with $n$ elements takes at least $n$ steps, since we need to process all $n$ elements in `A`.

***Key observation 1***
Re-hashing a [[Hash Table]] with $n$ elements takes at most $O(m + n + m')$ steps.
- $O(m)$: visit each slot of oiginal [[Hash Table]] `A`
- $O(n)$: processing all $n$ elements of `A`
- $O(m')$: steps for visiting each slot of new [[Hash Table]] `A`.

***Key observation 2***
Re-hashing a [[Hash Table]] with $n$ elements takes at least $n$ steps, since we need to process all $n$ elements in `A`.

## Re-hashing by constant increments
Let `𝐴` be the current [[Hash Table]] with 𝑚 slots and 𝑛 elements.
Let $0<\gamma<1$ be a fixed constant, and assume that $\dfrac{n}{m} \leq \gamma < \dfrac{n+1}{m}$.
Let `A'` be the new [[Hash Table]] with `m'` slots and `n+1` elements.
***
What happens if $m' = m + 1$?
- Insert $n$ elements into a [[Hash Table]] one by one
- For every insertion, we have to re-hash, starting with $m=1$
- Re-hashing a [[Hash Table]] with `n'` elements takes at least `n'` steps.

Consequence: inserting $n$ elements into a [[Hash Table]] takes at least 
$$\sum_{n'=1}^{n} n' =\frac{n(n+1)}{2} = \Omega(n^2)$$
steps. (Quadratic is very high for hashing)
***
What happens if $m' = m + c$ for some cosntant $c$?
- Insert $n$ elements into a [[Hash Table]] one by one
$$
\begin{align}
\dfrac{n}{m} \leq \gamma < \dfrac{n+1}{m} \implies \dfrac{n'}{m+c} &\leq \gamma < \dfrac{n'+1}{m+c'}\\
n'+1 &> \gamma(m+c') \geq n+\gamma c \\
n' &> n+\gamma c - 1;\\
n' &\leq \gamma(m+c) < n+1 + \gamma c
\end{align}
$$
Since $\gamma c - 1 \leq n' - n < \gamma c + 1$,
we have to re-hash after every $\approx \gamma c$ insertions.
Rehashing a [[Hash Table]] with `n'` elements takes at least `n'` steps.

Consequence: inserting $n$ elements into a [[Hash Table]] (starting from an empty table) takes at least 
$$
\begin{align}
&\Omega\left(\gamma c + 2\gamma c + \cdots + \left\lfloor\frac{n}{\gamma c}\right\rfloor \gamma c \right)\\
&= \Omega\left(\frac{\left\lfloor\frac{n}{\gamma c}\right\rfloor \left(\left\lfloor\frac{n}{\gamma c}\right\rfloor + 1\right) \gamma c}{2}\right)\\
&= \Omega(n^2)
\end{align}
$$
steps,
inclusive of re-hashing steps (complexity still quadratic!)

## Re-hashing by doubling
What happens if $m' = 2m$?
- Insert $n$ elements into a [[Hash Table]] one by one
$$
\begin{align}
\dfrac{n}{m} \leq \gamma < \dfrac{n+1}{m} \implies \dfrac{n'}{2m} &\leq \gamma < \dfrac{n'+1}{2m}\\
n'+1 &> 2\gamma m \geq 2n \\
n' &> 2n-1 \implies n' \geq 2n\\
n' &\leq 2\gamma m < 2(n+1)\\
\implies n' &\leq 2n+1
\end{align}
$$
Since $2n \leq n' \leq 2n+1$,
we have to re-hash every time the number of insertions doubles, starting from the very first re-hashing when inserting a new element to a [[Hash Table]] with $n_0$ elements.
=> re-hashing occurs when size of hash table reaches $n_0, 2n_0, 4n_0, ...$

Re-hashing a [[Hash Table]] with $n' \leq \gamma m' \leq m'$ elements and `m'` slots takes at most $O(m'+n'+2m')$ steps.

Consequence: inserting $n$ elements into a [[Hash Table]] (with the necessary re-hashing) takes at **most**
$$
\begin{align}
&O\left( n_0 + 2n_0 + \cdots + 2^{\left\lfloor\log_2{(n/n_0)}\right\rfloor}n_0  \right)\\
& \leq O\left(n_0 2^{\log_2{(n/n_0) +1}}\right)\\
&= O(2n) = O(n)
\end{align}
$$
steps.
Complexity is now linear.

## Amortized analysis
>Suppose we are interested in some operation that is executed $n$ times.
Each execution could possibly have a different number of steps taken.
Suppose we find that no matter what, it takes a total of $N$ steps to execute this operation $n$ times.
Then the **amortised cost** of this operation is $\dfrac{N}{n}$.

***
Amortised cost for `chain_hash_insert(A,x)` under [[#Re-hashing by doubling]]:
- Inserting $n$ elements into a [[Hash Table]] takes at most $O(n)$ steps.
- So amortised cost: $\dfrac{O(n)}{n} = O(1)$.

Cost for re-hashing is incorporated here and averaged over all insertions.
i.e. if we insert a total of 𝑛 elements into `𝐴`, then the insertion of each element takes on average $𝑂(1)$ steps.
***
`chain_hash_delete(A,x)`: $O(1)$
***
Average case `chain_hash_search(𝐴, 𝑘)`: $O(1)$,
provided [[Designing hash functions|simple uniform hashing]] assumption is satisfied.
Because of re-hashing, the [[Hash Operations|load factor]] of `A` does not exceed some given constant.
***
Average case `chain_hash_delete_key(𝐴, 𝑘)`: $O(1)$,
similar to above
provided we assume [[Designing hash functions|simple uniform hashing]].