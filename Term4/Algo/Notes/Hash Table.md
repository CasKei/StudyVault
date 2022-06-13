---
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

> Hash table: a [[Data Types and Data Structures|data structure]] that extends the idea of an [[Arrays and Linked Lists|array]].

Formally, a hash table is an array where each element is a (doubly)-[[Arrays and Linked Lists|LL]].

Every hash table with $N$ slots has an associated [[Algo Hash functions|hash function]]
$$h: K \to \set{0, 1, \dots, N-1}$$
where $K= \set{\text{all possible key values}}$

![[Pasted image 20220221140348.png]]
Example: Hash tables are useed to implement dictionaries in Python

A good [[Algo Hash functions|hash function]] maps a very large set of key values to a small set of hash values, such that [[Intro to hashing#Collisions in hashing|collisions]] are uncommon.

## Operations on a Hash Table A
[[Hash Operations]]
Assume that `h` is a fixed hash function associated to `A`

| Operation                     | Code                          | Description                                                                              | Complexity        |
| ----------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------- | ----------------- |
| `chain_hash_insert(A,x)`      | `list_insert(A[h(x.key)], x)` | Insert `x` at the head of the [[Arrays and Linked Lists\|LL]] in slot `h(x.key)` of `A`. | $O(1)$            |
| `chain_hash_delete(A,x)`      | `list_delete(A[h(x.key)], x)` | Delete `𝑥` from the [[Arrays and Linked Lists\|LL]] in slot `ℎ(𝑥. key)` of `𝐴`.          | $O(1)$            |
| `chain_hash_search(𝐴, 𝑘)`     | `list_search(𝐴[ℎ(k)], 𝑘)`     | Return element (pointer) of `𝐴` whose key value is `𝑘`.                                  | Worst case $O(n)$ |
| `chain_hash_delete_key(𝐴, 𝑘)` | `list_delete_key(𝐴[ℎ(𝑘)], 𝑘)` | Delete element (pointer) of `𝐴` whose key value is `𝑘`.                                  | Worst case $O(n)$ |

