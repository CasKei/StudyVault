---
aliases: graph
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Introduction to Graph|DDW Intro to Graph]]

## What is a Graph?
> A graph is a non-linear [[Data Types and Data Structures|data structure]] that can allow representation of relationships between data elements.

We must define 2 things for a graph:
- **Vertex**: a node connected by edges. Also called **key**.
- **Edge**: lines connecting 2 vertices. Can be uni-directional or bi--directional. Or directed or undirected.

> $$G = (V, E)$$
> $V :  \set{\text{a set of n vertices}}$
> $E \subseteq V \times V : \set{\text{a set of n edges (pairs of vertices)}}$

> - **Directed graphs**: order of the vertices on the edges matters
> - **Undirected graphs**: ignore order

| Undirected                                                  | Directed                             |
| ----------------------------------------------------------- | ------------------------------------ |
| ![[Pasted image 20220228212317.png]]                        | ![[Pasted image 20220228212335.png]] |
| $V = \set{a, b, c, d}$                                      | $V = \set{a, b, c}$                  |
| $E=\set{\set{a,b},\set{a,c},\set{b,c},\set{b,d},\set{c,d}}$ | $E=\set{(a,c), (a,b), (b,c), (c,b)}$ |

## Examples
- Social networks - friend finder
- EEG brain dynamics
- Computer networks
	- Internet routing
	- Connectivity
- Transporation and energy networks
- Game States
	- Rubik's cube, chess
- Music
	- Auto accompaniment, chord progression

### 2x2x2 Rubik's Cube
Start with a given configuration.
Modes are quater turns of any face.
Solve by making each side one colour.

**Configuration Graph**
A graph that has:
- One **vertex** for each state of the cube
- One **edge** for each move from a vertex
	- 6 faces to twist
	- 3 nontrivial ways to twist $(1/4, 2/4, 3/4)$
	- So, each state has $18$ edges outwards

Solve cube by finding a path from initial state to solved state.

**State Exploration**
- One start vertex
- 6 new configurations reacheable by one $90\degree$ turn
- From those, 27 novel others by another $90 \degree$ turn
- And so on...

![[Pasted image 20220228214352.png]]
![[Pasted image 20220228214424.png]]

## Representing Graphs
In order to work with graphs, we have to be able to input a graph into a computer.
Main info needed by the computer:
- V
- E
- How they connect

**3 representations** with individual pros/cons
1. [[#Adjacency list]] (of neighbours of each vertex)
2. [[#Incidence list]] (of edges from each vertex)
3. [[#Adjacency matrix]] (of which pairs are adjacent)

### Adjacency list
[[Introduction to Graph#Adjacency List|DDW adjacency list]]
> For every vertex `v`, list its neighbours.
> Neighbours: vertices to which it is connected by an edge.

- [[Arrays and Linked Lists|Array]] `A` of `|V|` [[Arrays and Linked Lists|LL]]
- For `v` $\in$ `V`, list `A[v]` stores neighbours $\set{u | (v,u) \in E}$

**Directed graph** only stores *outgoing* neighbours
**Undirected graph** stores edge in 2 places

![[Pasted image 20220228220627.png]]

### Incidence list
> For each vertex `v`, list its edges

- Array `A` of `|V|` [[Arrays and Linked Lists|LL]]
- For `v` $\in$ `V`, list `A[v]` stores edges $\set{e| e=(v,u) \in E}$

**Directed graph** only stores *outgoing* edges.
**Undirected graph** stores edge in 2 places.

In Python, `A[v]` can be [[Hash Table]].
![[Pasted image 20220228221236.png]]

### Adjacency matrix
[[Introduction to Graph#Adjacency Matrix|DDW adjacency matrix]]
> Assume $V = \set{1, \dots , n}$
> Represent by $n \times n$ matrix $A = (a_{ij})$
> - $a_{ij} = 1$ if $(i, j) \in E$
> - $a_{ij} = 0$ otherwise

![[Pasted image 20220228221638.png]]

Note: if edge is **bi-directional**, then there is symmetry in the entry.

### Evaluation and comparison
Assume vertices: $V: \set{1, \dots, n}$
To add an edge: both $O(1)$.

| Type                  | Tradeoff: Space                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| [[#Adjacency list]]   | One list node per edge <br>                      $\Theta(n+m)$ bits                               |
| [[#Adjacency matrix]] | $n^2$ entries, but each entry can just be one bit so <br>                      $\Theta(n^2)$ bits |
| Conclusion            | Matrix better only for very dense graphs: when $m$ near $n^2$                                     |

**Tradeoff: Time**

| Operation                                 | [[#Adjacency list]]                      | [[#Adjacency matrix]] |
| ----------------------------------------- | ---------------------------------------- | --------------------- |
| Add an edge                               | Both $O(1)$                              | Both $O(1)$           |
| Check if there is an edge from `u` to `v` | Scan list of `u`: $O(\text{neighbours})$ | $O(1)$                |
| Visit all neighbours of `u`               | $O(\text{neghbours})$                    | $\Theta(n)$           |
| Remove an edge                            | like find + add                          | like find + add       |

