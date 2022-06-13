---
aliases: load factor
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

## Operations on a [[Hash Table]] A
[[Hash Operations]]
Assume that `h` is a fixed hash function associated to `A`

| Operation                     | Code                          | Description                                                                              | Complexity        |
| ----------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------- | ----------------- |
| `chain_hash_insert(A,x)`      | `list_insert(A[h(x.key)], x)` | Insert `x` at the head of the [[Arrays and Linked Lists\|LL]] in slot `h(x.key)` of `A`. | $O(1)$            |
| `chain_hash_delete(A,x)`      | `list_delete(A[h(x.key)], x)` | Delete `𝑥` from the [[Arrays and Linked Lists\|LL]] in slot `ℎ(𝑥. key)` of `𝐴`.          | $O(1)$            |
| `chain_hash_search(𝐴, 𝑘)`     | `list_search(𝐴[ℎ(k)], 𝑘)`     | Return element (pointer) of `𝐴` whose key value is `𝑘`.                                  | Worst case $O(n)$ |
| `chain_hash_delete_key(𝐴, 𝑘)` | `list_delete_key(𝐴[ℎ(𝑘)], 𝑘)` | Delete element (pointer) of `𝐴` whose key value is `𝑘`.                                  | Worst case $O(n)$ |

## Hash insert
(does not include deleted value)
```php
function hash_insert(T, k)
	i = 0
	repeat
		j = h(k,i)
		if T[j] == NIL
			T[j] = k
			return j
		else i++
	until i == m
	error "hash table overflow"

```
(see clrs 11.4-2 ans)
## Hash search
```php
function hash_search(T, k)
	i = 0
	repeat
		j = h(k,i)
		if T[j] == k
			return j
		i++
	until T[j] == NIL or i == m
	return NIL
```
## Hash delete
(clrs 11.4-2)

## Load Factor
> A [[Hash Table]] with `n` elements and `m` slots has a ==load factor== of $\frac{n}{m}$.
> This ==load factor== is the average number of elements in each slot, under the [[Designing hash functions|simple uniform hashing]] assumption.

![[Pasted image 20220221210537.png]]
![[Pasted image 20220221210548.png]]

## Average case performance
Let `A` be a [[Hash Table]] with `m` slots, `n` elements and a [[#Load Factor]] $\alpha = \frac{n}{m}$.
Recall `chain_hash_search(A, k)` and `chain_hash_delete_key(A, k)`, with worst case complexity $O(n)$

Under the [[Designing hash functions|simple uniform hashing]] assumption,
==Average case complexity is $\Theta(1+\alpha)$  for either operation==
=> Depends on how n and m are related
- If `m` is a fixed constant, then $\Theta(1 + \alpha) = \Theta(1+n) = \Theta(n)$
- If $\alpha = O(1)$ then $\Theta(1 + \alpha) = O(1)$

Justification:
Let $h: K \to \set{0, 1, \dots, m-1}$ be the [[Algo Hash functions|hash function]] of `A`.
- Case 1: `k` is not the key value of any element in `A`
	- It takes $\Theta(1)$ steps to compute $h(k)$
	- Within the [[Arrays and Linked Lists|LL]] `A[h(k)]`, all elements must be visited before the operation returns NIL. On avg there are $\alpha$ elements in `A[h(k)]`, so the overall complexity is $\Theta(1+\alpha)$
- Case 2: `k` is the key value of some element in `A`
	- Also same
	- Proof in textbook [go read pls]

## Why hashing is usually fast
> Observation:
> If the number of elements is at most some ratio of the number of slots in the [[Hash Table]], i.e. $n=O(m)$, then $\alpha$ is $\frac{O(m)}{m} = O(1)$, so the average case complexity is $\Theta(1+\alpha)=O(1)$. 

-> How do we keep the number of slots to be at least the number of elements in the [[Hash Table]] `A`?
i.e. how to ensure that $n=O(m)$ as $n$ grows?
[[Re-hashing]]!

More Complexity analysis in [[Re-hashing]]