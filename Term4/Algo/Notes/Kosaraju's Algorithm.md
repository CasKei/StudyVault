---
tags: 50.004
---
[[Algo]]
[[2SAT solver]]
[[Strongly connected components]]

Kosaraju's algorithm is programmed to find [[Strongly connected components]] of the [[Graphs|graph]].

Run [[Depth-First-Search (DFS)|DFS]] in 2 cycles, where the first DFS identifies the stack order, and the second DFS utilises this stack.\
At the end, every child node will be assigned a parent, and nodes with the same leader nodes are one [[Strongly connected components]] group.

Complexity $O(m + n)$, where $m$ and $n$ are number of edges and vertices.

1. [[Depth-First-Search (DFS)|DFS]] on the whole graph starting at first node.
2. Visit all child nodes.
3. If node leads to visited node, push visited node into stack.
4. Traverse through the [[Implication Graph]] to find direct neighbours next to the node if path exists.
5. [[Depth-First-Search (DFS)|DFS]] starts from top node of stack and traverses though all children. When child is revisited, nodes in path are a [[Strongly connected components]] group.

One strong property of this algo is that it uses the fact that the transpose graph has the sme [[Strongly connected components]] as the original [[Graphs|graph]].