---
aliases: graph
tags: #data-structure, #graph
---
Back to [[Data Driven World|DDW]]
# Introduction to Graph
## What is a Graph?
Previous data structures like lists, arrays, [[Stacks and Queues data structure|stacks and queues]], only are related in a linear fashion.
A Graph allows more relationship to be represented between each item.
![[Pasted image 20211226195430.png]]
This example represents some kind of connection between places, like in a map.With this kind of data, we can find a path from one place to another, or find the shortest distance between the two places.
![[Pasted image 20211227112936.png]]
This example represents the control flow of ta computer program.
Compiler can use this information to optimise the code.

We can define 2 things when dealing with a graph:
- Vertex: a node that is connected by edges in a graph. Also called 'key'
- Edge: lines connecting two vertices. Can be uni-directional or bi-directional.
## How to Represent a Graph in Code?
Main info needed by the computer:
- vertices
- edges
- how they connect

![[Pasted image 20211227113850.png]]
Here is an example.
### Adjacency Matrix
In this matrix, if there is a connection between one vertex to another, the cell between that row and column is represented by soem number, like 1 instead of 0, as when there is no connection.

| |V1|V2|V3|V4|V5|
|---|---|---|---|---|---|
|V1| 0|1| 0| 0|1|
|V2|1| 0|1|1| 0|
|V3|0 |1|0 |0 |0 |
|V4|1| 0|1|0 |0 |
|V5|0 |0 | 0|1| 0|

Note: If edge is bidirectional, then there is a symettry in the entry.

Advantage: simple and intuitive
Disadvantage: may be a sparse matrix where most of the entry are zeros and only a few non-zero entries.
Hence good when number of edges are large as when every vertex is connected to every other vertex.

### Adjacency List
More suitable when the number of edges is not large. Can use a dictionary for this.
```py
graph1 = {'V1': ['V2', 'V5'],
          'V2': ['V1', 'V3', 'V4'],
          'V3': ['V2'],
          'V4': ['V1', 'V3'],
          'V5': ['V4']}
```
If edges are weighted, you can use another dictionary instead of list.
```py
graph1 = {'V1': {'V2': 1, 'V5': 1},
          'V2': {'V1': 1, 'V3': 1, 'V4': 1},
          'V3': {'V2': 1 },
          'V4': {'V1': 1, 'V3': 1},
          'V5': {'V4': 1}}
```
### [[Object Oriented Programming|OOP]]
We can create 2 classes: `Vertex` and `Graph` class.
The `Vertex` class is similar to each entry in the dictionary. It contains the information on that particular vertex and who are the neighbour vertices. Can also contain the weights of the connection between this vertex to its neighbours.
The `Graph` class contains the list of all the vertices in the graph.
![[Pasted image 20211227123226.png]]
`Graph` is **composed** of one or more `Vertex` objects. (composition).
![[Pasted image 20211227123306.png]]
More operations can be added. ^aaec7e