---
aliases: collisions
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

> Hashing is a method for storing data that has all the advantages of [[Direct addressing|direct address tables]], without its limitations.

- `insert`, `delete`, and `search` are fast with $O(1)$ on average
- No waste of memory with many NIL entries
- Prior knowledge of max possible key value not required
- Key values need not be integers

## Key ideas
[[Hash functions]]: function that maps arbitrary key values to a fixed set of integers
[[Hash Table]]: Similar to a [[Direct addressing|direct address table]], but instead each object is stored based on its hash value, i.e. the value obtained after passing the key value to the hash function.

## Idea of Hash function
![[Pasted image 20220221135530.png]]

## Collisions in hashing
If two key values are hashed to the same slot
We cannot avoid collisions if there are more key values than hash values.
![[Pasted image 20220221135632.png]]

> Collision resolution: a systematic prrocess for inserting objects with duplicate hash values into the hash table

e.g. chaining
**key idea**: every slot in the hash table `A` is a [[Arrays and Linked Lists|LL]]
- All elements that hash to the same slot are placed in the same [[Arrays and Linked Lists|LL]]. This allows the insertion of multiple elements with the same hash value.
- Inserting new elements into `A` is fast because insertion of new elements into [[Arrays and Linked Lists|LL]] is fast
- Given a hash function `h` and a new element `x` with a key value `k`, we insert `x` into `A` by running `list_insert(A[h(k)], x)`.
	- We are inserting `x` as the head of the [[Arrays and Linked Lists|LL]] `A[h(x)]`.
- If the [[Designing hash functions|simple uniform hashing]] assumption is satisfied, then collisions are 'equally distributed'.

## [[Direct addressing]] VS [[Intro to hashing|Hashing]]
| Direct addressing                                                                                                                                                                           | Hashing                                                                           |                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Objects we want to store must have distinct integer key values. Store the pointers to the objects in a [[Direct addressing\\                                                                | direct address table]] based on the key values.                                   | Objects we want to store can have arbitrary key values. Given some [[Hash functions\|hash function]], these key values are mapped to hash values. We store the pointers to these objects in a [[Hash Table]] based on their hash values. |
| If `x` is a pointer to an object with key value `k`, then store `x` in slot `k`                                                                                                             | If `x` is a pointer to an object with hash value `k`, then store `x` in slot `k`. |                                                                                                                                                                                                                                          |
| We assume objects have distinct key values, no two pointers of different objects will be stored in the same slot. Hence there are no [[Intro to hashing#Collisions in hashing\|collisions]] | Distinct objects could have the same hash value, so [[Hash Table]]s could have [[Intro to hashing#Collisions in hashing|collisions]]                                                                                  |                                                                                                                                                                                                                                          |