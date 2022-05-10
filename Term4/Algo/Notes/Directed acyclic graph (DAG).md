---
aliases: DAG
tags: #50.004
---
[[Algo]]
[[Algo week 6]]
[[Algo week 9]]

## Examples
| DAG                                  | Not DAG                              |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20220301144022.png]] | ![[Pasted image 20220301144053.png]] |
| ![[Pasted image 20220301144251.png]] |                                      |
| ![[Pasted image 20220301144336.png]]                                     |                                      |


## [[Single-source shortest path problem|Single-source shortest path]] in DAGs
[[Topological sort]]
[[Weight function]]
[[Representing graphs|adjacency list]]
```php
function DAG_Shortest_Paths(G,w,s)
	'''
	Require: A weight function w for G
	Require: A vertex s of G
	Require: A DAG G represented as an adjacency list, where G.Adj[u] is the LL of vertices adj to u
	'''
	topologically sort the vertices of G
	initialise_single_source(G,s)
	for each vertex u (in topsort order)
		for each vertex v in G.Adj[u]
			relax(u,v,w)
```

### Complexity
Topsort: $\Theta(|V| + |E|)$
initialise_single_source(G,s): $\Theta(|V|)$
Main loop: $\Theta(|V| + |E|)$

In main loop:\
Iterate over each vertex $u$ exactly once. Iterate over each directed edge $(u,v)$ exactly once.

Overall complexity: $\Theta(|V| + |E|)$