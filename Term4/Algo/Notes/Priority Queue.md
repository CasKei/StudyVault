---
aliases: 
tags: #50.004
---
[[Algo]]
[[Binary Heap and Heapsort]]
[[Heap data structure]]
[[Data Types and Data Structures]]
[[W3 Heap]]

> A Priority Queue is an [[Data Types and Data Structures#Data types versus abstract data types ADT|abstract data type (ADT)]] that consists of a set $S$ of elements, together with operations on S

- Every element of $S$ has an associated key
	- a key is a numerical value, usually interpreted as "priority score"
	- If $x \in S$, then the key if $x$ is sometimes denoted by $k(x)$

## Operations on S
`max(S)`: return element from S with largest key
`insert(S, x)`: insert element `x` into set $S$
`extract_max(S)`: return element from $S$ wtih largest key and remove it from $S$
`increase_key(S, x, k)`: increase the value of the key of element $x$ tothe new value $k$

## Implementation with arrays
- `A1` : store elements of S the order they arrive
- `A2`: store the elements of S one by one, where each new element is inserted into the array, so the elements are always in decreasing order

## Implementation with heap
Most real-world implementations use heaps and their variations.
More advanced implementations could support additional operations, e.g. `batch_insert`, `merge`, etc.

## Complexity

| Operation               | Array `A1`        | Array`A2`        | Heap              |
| ----------------------- | ----------- | ----------- | ----------------- |
| `max(S)`                | $\Theta(n)$ | $\Theta(1)$ | $\Theta(1)$       |
| `insert(S, x)`          | $\Theta(1)$ | $\Theta(n)$ | $\Theta(\log{n})$ |
| `extract_max(S)`        | $\Theta(n)$ | $\Theta(n)$ | $\Theta(\log{n})$ |
| `increase_key(S, x, k)` | $\Theta(n)$ | $\Theta(n)$ | $\Theta(\log{n})$ |

## Some Applications of Priority Queues
### Path-Finding
[[Algo week 9]]
Dijkstra's algorithm (for finding the shortest path from one node to another)
### Targeted advertising (on socal networks)
Prim's algorithm (for finding a minimum spanning tree)
### Broadband routing management
Bandwidth acceess depends on the "priority score" of each user; a higher score implies a lower likelihood for transmission delay