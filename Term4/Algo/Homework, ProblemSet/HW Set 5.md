---
tags: #50.004
---

# 50.004 HW5 Cassie Chong 1005301 CC01
## 1)
Let $G_1$ be a directed weighted graph with 5 vertices $A, B, C, D, E$. This graph $G_1$ and its associated weight function $w_1$ are depicted in Figure 1, where the values on the edges represent the corresponding weights.
![[Pasted image 20220325122211.png]]
### i)
Run the Bellman–Ford algorithm on graph $G_1$, with weight function $w_1$ and source vertex $A$, using the relaxation order $(A, B), (A, E), (B, D), (B, E), (C, B), (D, C), (E, D)$. Please give the table of $d$ and $\pi$ values for all vertices, obtained at the end of each pass of all edges of $G_1$ in the given relaxation order. The rows of your table should correspond to the iterations of the algorithm. You should include all iterations, including the initialization and the final check. Please write each entry of your table as a $(d, \pi)$ pair. For example, if the entry corresponds to vertex $x$, and we have the values $x.d = 10$, $x.\pi = y$, then the corresponding entry is $(10, y)$.
***
| Iteration  | $A(d,\pi)$ | $B(d,\pi)$ | $C(d,\pi)$ | $D(d,\pi)$ | $E(d,\pi)$ |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Init       | $(0, NIL)$          | $(\infty, NIL)$    | $(\infty, NIL)$  | $(\infty, NIL)$   |$(\infty, NIL)$   |
| 1          | $(0, NIL)$          | $(6, A)$       | $(8, D)$       | $(4, E)$       | $(2, A)$       |
| 2          | $(0, NIL)$          | $(6, A)$       | $(3, D)$       | $(4, E)$       | $(2, A)$       |
| 3          | $(0, NIL)$          | $(5, C)$       | $(3, D)$       | $(4, E)$       | $(2, A)$       |
| 4          | $(0, NIL)$          | $(5, C)$       | $(3, D)$       | $(4, E)$       | $(2, A)$       |
| Last Check | $(0, NIL)$          | $(5, C)$       | $(3, D)$       | $(4, E)$       | $(2, A)$           |

Return `TRUE`.

### ii) [3]
Next, consider a new weight function $w'_1$ on the same graph $G_1$, where $w'_1(C, B) = -1$, and where $w'_1(e) = w_1(e)$ for all other edges $e \not = (C,B)$ in $G_1$. Run the Bellman–Ford algorithm on graph $G_1$, with weight function $w'_1$ and source vertex $A$, using the same relaxation order as before. Please give the new table of $d$ and $\pi$ values for all vertices, obtained at the end of each pass of all edges of $G_1$ in the given relaxation order. Again, you should include all iterations in your table, including the initialization and the final check.
***
| Iteration  | $A(d,\pi)$ | $B(d,\pi)$ | $C(d,\pi)$ | $D(d,\pi)$ | $E(d,\pi)$ |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Init       | $(0, NIL)$ | $(\infty, NIL)$   | $(\infty, NIL)$   | $(\infty, NIL)$   | $(\infty, NIL)$   |
| 1          | $(0, NIL)$ | $(6, A)$       | $(8, D)$       | $(4, E)$       | $(2, A)$       |
| 2          | $(0, NIL)$ | $(6, A)$       | $(3, D)$       | $(4, E)$       | $(2, A)$       |
| 3          | $(0, NIL)$ | $(2, C)$       | $(3, D)$       | $(4, E )$      | $(2, A)$       |
| 4          | $(0, NIL)$ | $(2, C)$       | $(3, D)$       | $(2, E)$       | $(0, B)$       |
| Last Check | $(0, NIL)$ | $(2, C)$       | ***(1, D)***   | $(2, E )$      | $(0, B)$       |

Last check failed. Return `FALSE`. Negative cycle in graph.

## 2)
Design an algorithm that takes as its three inputs a directed weighted graph $G$, its associated weight function $w$, and a vertex $s$ of $G$, and runs the necessary computation so that every vertex $v$ of $G$ (including $v = s$) has an attribute $v.d$, such that the value of $v.d$ is the shortest-path distance from $s$ to $v$ in $G$. Your algorithm should not return any output. Your algorithm should compute the correct shortest-path distances from s to every other vertex, even if $G$ contains a negative-weight cycle. In other words, if $v$ is a vertex of $G$ such that there is a path from $s$ to $v$ that contains a negative-weight cycle as a subpath, then your algorithm should assign the attribute value $v.d = −\infty$. Otherwise, $v.d$ should be the sum of the weights of the edges in a shortest path from $s$ to $v$. Justify why your algorithm works and analyse the running time complexity of your algorithm. For full credit, your algorithm should run in $O(|V ||E|)$ time, where $|V |$ is the number of vertices in $G$, and $|E|$ is the number of edges in $G$. (Hint: Modify the Bellman–Ford algorithm.)
***
Inputs: G (directed, weighted), w, s
No output.
```php
function initialise_single_source(G, s)
	'''
	Require: G = (V, E) is a weighted directed graph
	Require: s in V is a vertex
	'''
	for every vertex v in V:
		v.d <- \infty
		v.pi <- NIL
	s.d <- 0

function relax(u, v, w)
	'''
	Require: (u, v) is a directed edge of G
	'''
	if u.d + w(u, v) < v.d then:
		v.d <- u.d + w(u, v)
		v.pi <- u

function neg_check(u, v, w)
	'''
	Require: (u, v) is a directed edge of G
	'''
	if u.d + w(u, v) < v.d then:
		v.d <- - \infty 
		v.pi <- NIL
		
function Mod_Bellman_Ford(G, w, s)
	'''
	Require: A directed graph G with vertex set G.V and edge set G.E
	Require: A weight function w for G. A vertex s of G.
	'''
	// Main loop: update d and pi for all V
	for i = 1 to |G.V| - 1:
		for every directed edge (u, v) in G.E:
			relax(u, v, w)

	// Check and assign negative infty if reacheable by negative
	// weight cycle
	for i = 1 to |G.V| - 1:
		for every directed edge (u, v) in G.E:
			neg_check(u, v, w)
```
**Algo**
In comparison to the Bellman-Ford Algorithm taught in class, this algorithm has another utility function similar to `relax`, but sets `v.d` and `v.pi` to $- \infty$ and `NIL` respectively when the attribute `d` is updated further. In the main function, the main loop remains the same, but the check has simply turned into a repeat of the main loop but using the `neg_check` function instead of the `relax` function like in the main loop.

**Correctness**
It is already known from Lemma 24.2 that after $|V| - 1$ iterations in the main loop, we have $v.d = \delta(s,v)$ for all vertices $v$ of $G$, no matter the order. Thus, after the main loop is done, we already have the answer if there are no negative weight cycles. If there are any changes to the answer during the check, we can conclude that $v$ in the edge involved in the change are due to a negative cycle in its path from the source.

To check if all the vertices are connected with the negative weight cycle, by a similar logic to Lemma 24.2, we repeat the same $|V| - 1$ iterations, but if there are any changes, mark them with $-\infty$ `v.d`. Doing so will catch all the vertices with a negative weight cycle in its subpath from the source to that vertex. We will then end up with the result required.

**Complexity**
`initialise_single_source(G,s)`: $\Theta(|V|)$
`relax(u, v, w)`: $\Theta(1)$
`neg_check(u, v, w)`: $\Theta(1)$
Main loop: $\Theta(|V||E|)$
Final check: $\Theta(|V||E|)$

Overall: $\Theta(|V||E| + |V||E|) = \Theta(|V||E|)$

***
For the next two questions, consider a directed weighted graph $G_2$ with 5 vertices $s, t, x, y, z$. This graph $G_2$ and its associated weight function $w_2$ are depicted in Figure 2, where the values on the edges represent the corresponding weights.
![[Pasted image 20220325122443.png]]

## 3)
Run Dijkstra’s algorithm on graph $G_2$, with weight function $w_2$ and source vertex $x$. In a table format, please give the $d$ and $\pi$ values of all vertices, as well as the set $S$ and the priority queue $Q$, obtained at the end of each iteration of the while loop in Dijkstra’s algorithm. You may assume that $Q$ is implemented using a min-heap, and you may write $Q$ in its array representation. The first row of your table should correspond to the initialization. Each subsequent row of your table should correspond to an iteration of the while loop. Also, please draw the final shortest-paths tree for $G_2$ as computed by Dijkstra’s algorithm.
***
| `u` | $s(d, \pi)$     | $t(d, \pi)$     | $x(d, \pi)$ | $y(d, \pi)$     | $z(d, \pi)$     | $S(V,d)$                                     | $Q(V, d)$                                                 |
| --- | --------------- | --------------- | ----------- | --------------- | --------------- | --------------------------------------- | --------------------------------------------------------- |
| NIL | $(\infty, NIL)$ | $(\infty, NIL)$ | $(0, NIL)$  | $(\infty, NIL)$ | $(\infty, NIL)$ | $\set{}$                                | $\set{(x,0),(s,\infty),(t,\infty),(y,\infty),(z,\infty)}$ |
| $x$ | $(\infty, NIL)$ | $(\infty, NIL)$ | $(0, NIL)$  | $(9, x)$        | $(8, x)$        | $\set{(x,0)}$                           | $\set{(z,8), (y,9),(s,\infty), (t,\infty)}$               |
| $z$ | $(12, z)$       | $(\infty, NIL)$ | $(0, NIL)$  | $(9, x)$        | $(8, x)$        | $\set{(x,0),(z,8)}$                     | $\set{(y,9),(s,12),(t,\infty)}$                           |
| $y$ | $(12, z)$       | $(\infty, NIL)$ | $(0, NIL)$  | $(9, x)$        | $(8, x)$        | $\set{(x,0),(z,8),(y,9)}$               | $\set{(s,12),(t,\infty)}$                                 |
| $s$ | $(12, z)$       | $(19, s)$       | $(0, NIL)$  | $(9, x)$        | $(8, x)$        | $\set{(x,0),(z,8),(y,9),(s,12)}$        | $\set{(t, 19)}$                                           |
| $t$ | $(12, z)$       | $(19, s)$       | $(0, NIL)$  | $(9, x)$        | $(8, x)$        | $\set{(x,0),(z,8),(y,9),(s,12),(t,19)}$ | $\set{}$                                                          |

![[Pasted image 20220327133116.png]]

## 4) [5]
Run Dijkstra’s algorithm on graph $G_2$, with weight function $w_2$ and source vertex $s$. Similar to the previous question, please give in table format the $d$ and $\pi$ values of all vertices, as well as the set $S$ and the priority queue $Q$, obtained at the end of each iteration of the while loop in Dijkstra’s algorithm. You may assume that $Q$ is implemented using a min-heap, and you may write $Q$ in its array representation. The first row of your table should correspond to the initialization. Each subsequent row of your table should correspond to an iteration of the while loop. Also, please draw the final shortest-paths tree for $G_2$ as computed by Dijkstra’s algorithm.
***
| `u` | $s(d, \pi)$ | $t(d, \pi)$     | $x(d, \pi)$     | $y(d, \pi)$     | $z(d, \pi)$     | $S(V, d)$                              | $Q(V,d)$                                                  |
| --- | ----------- | --------------- | --------------- | --------------- | --------------- | -------------------------------------- | --------------------------------------------------------- |
| NIL | $(0, NIL)$  | $(\infty, NIL)$ | $(\infty, NIL)$ | $(\infty, NIL)$ | $(\infty, NIL)$ | $\set{}$                               | $\set{(s,0),(t,\infty),(x,\infty),(y,\infty),(z,\infty)}$ |
| $s$ | $(0, NIL)$  | $(7, s)$        | $(9, s)$        | $( 5, s)$       | $(\infty, NIL)$ | $\set{(s,0)}$                          | $\set{(y,5),(t,7),(x,9),(z,\infty)}$                      |
| $y$ | $(0, NIL)$  | $(7, s)$        | $(9, s)$        | $(5, s)$        | $(12, y)$       | $\set{(s,0),(y,5)}$                    | $\set{(t,7),(x,9),(z,12)}$                                |
| $t$ | $(0, NIL)$  | $(7, s)$        | $(8, t)$        | $(5, s)$        | $(12, y)$       | $\set{(s,0),(y,5),(t,7)}$              | $\set{(x,8),(z,12)}$                                      |
| $x$ | $(0, NIL)$  | $(7, s)$        | $(8, t)$        | $(5, s)$        | $(12, y)$       | $\set{(s,0),(y,5),(t,7),(x,8)}$        | $\set{(z,12)}$                                            |
| $z$ | $(0, NIL)$  | $(7, s)$        | $(8, t)$        | $(5, s)$        | $(12, y)$       | $\set{(s,0),(y,5),(t,7),(x,8),(z,12)}$ | $\set{}$                                                          |

![[Pasted image 20220327133129.png]]

## 5) [5]
Suppose that you are (once again) trying to find the “best” path between two locations $s$ and $t$, but unlike the usual scenario, you do not seek to minimise the time or distance of your journey. Instead, you want to find the most comfortable path from $s$ to $t$. For example, you may prefer to take a longer, sheltered path over a shorter unsheltered path.

We can model this pathfinding problem with a directed weighted graph $G$, and an associated weight function $w$, where each edge $(u, v)$ represents a possible route from $u$ to $v$, and where the weight of an edge $e$ is a strictly positive integer $w(e)$ representing the discomfort experienced when taking the route. We define the discomfort level of a path $(e1, e2, . . . , en)$ to be the maximum discomfort of the edges traversed, i.e. $\max\set{{w(e1), . . . , w(en)}}$. You may consider a path with no edges to have a discomfort level of 0.

Design an efficient algorithm that takes as its four inputs a directed weighted graph $G$, its associated weight function $w$, a start vertex $s$, and an end vertex $t$, and returns as its output the minimum possible discomfort level of any path in $G$ from $s$ to $t$. You may use any operations discussed in the lectures or cohort classes. To get full credit for this question, your algorithm should run in $O((|V | + |E|) \log{|V |})$ time, where $|V |$ is the number of vertices in $G$, and $|E|$ is the number of edges in $G$. Justify why your algorithm has running time complexity $O((|V | + |E|) \log{|V |})$. (Hint: Modify Dijkstra’s algorithm.)
***
Input: G (directed, weighted), w ($\mathbb{Z}^+$), $s$, $t$
Output: Minimum discomfort
Finding minimum discomfort when edges are not distances but discomfort is doing the same as minimising the paths. There is no change, except the d attribute now represents discomfort, and we can stop after we find the distance for the target vertex. Then when the target is found, its d value is the minimum discomfort, if it is reachable. We modify and add to the Dijkstra's algorithm. Mainly, the way relaxation is done has changed.
```php
function initialise_single_source(G,s):
	'''
	Require: G = (V, E) is a weighted directed graph
	Require: s in V is a vertex
	'''
	for every vertex v in V:
		v.d <- \infty
		v.pi <- NIL
	s.d <- 0

function mod_relax(u, v, w)
	'''
	Require: (u, v) is a directed edge of G
	Require: priority queue Q has decrease_key operation that can be accessed here
	'''
	if u.d < w(u, v) then // current edge has higher discomfort
		v.d <- w(u, v) // retain largest discomfort
	else // infty or previous edges has larger discomfort
		v.d <- u.d // keep previous largest discomfort recorded
	v.pi <- u // track parent regardless, don't use parent to check reachability
	// for identifying path if required (not required in this qn)

function Mod_Dijkstra(G, w, s, t)
	'''
	Require: A weight function w for G
	Require: A vertex s and t of G
	Require: A DAG G represented as an adj list, where G.Adj[u] isthe LL of vertices adj to u
	'''
	initialise_single_source(G,s)
	S <- ∅ // initialise S as empty set
	Q <- G.V // Q is a min-priority queue. Elements of Q are vertices, and keys of these elements are the d values
	while Q != ∅
		u <- extract_min(Q) // u has smallest d among vertices in Q, and it is removed from Q

		// if least discomfort vertex (u) found
		if (u == t) then
			// if reachable
			if (u.d != \infty) then
				return u.d
			else
				return "target is unreachable"
		else // target not extracted from Q yet
			S <- S ∪ {u} 
			for each vertex v in G.Adj[u]
				mod_relax(u, v, w)
```
`initialise_single_source(G,s)`: $\Theta(|V|)$
`mod_relax(u, v, w)`: require `decrease_key` operation when assigning new $d$ value, which has complexity $O(\log{|V|})$, assuming we implement $Q$ as a min-heap. To do so, start with $G.V$ represnted as an array, then run `build_min_heap` on this array, which I will not show here as it is not part of the question. I assume that $Q$ is a ready made min-heap.
Initialise S as empty set: $\Theta(1)$
`extract_min(Q)`: implement Priority Queue as a min-Heap: $O(\log{|V|})$
Checks if target reached and reachable and return answer: $\Theta(1)$
S <- S ∪ {u}: $\Theta(1)$

Overall complexity of `Mod_Dijkstra` using binary min-heaps: $O((|V| + |E|)\log{|V|})$


## 6) bonus
In many graphs, there could be several minimum-discomfort-level paths from vertex $s$ to vertex $t$, and we may wish to find a shortest minimum-discomfort-level path. More precisely, by “shortest”, we mean that among all the possible paths from $s$ to $t$ that achieve the minimum possible discomfort level, we want to find one such path whose distance (which is not the same as discomfort level) is minimized among these paths. (Again, it is possible that there could be several such shortest minimum-discomfort-level paths, and we want to find any one such shortest minimum-discomfort-level path.) We can model this new pathfinding problem with the same directed weighted graph $G$ and the same weight function $w$ representing discomfort level, but with an additional weight function $w′$ representing distance. Assume that for all edges $e$ of $G$, we have that $w′(e)$ is a non-negative value representing the distance of the edge $e$.

Design an algorithm that takes as its five inputs $G, w, w′, s, t$, where $G, w, s, t$ are the same four inputs for your algorithm in Question 5 and $w′$ is an additional weight function representing distance (as described above), and returns as its output an array $[u_1, . . . , u_k]$ of vertices in $G$, such that $u_1 = s$, $u_k = t$, and $⟨u1, . . . , uk⟩$ represents a shortest minimum-discomfort-level path from $s$ to $t$. In the case that there are multiple possible shortest minimum-discomfort-level paths from $s$ to $t$, your algorithm should return any one such shortest minimum-discomfort-level path.  
You may assume that $w(e)$ is a positive integer, and $w′(e)$ is a non-negative numerical value, for any edge $e$ of $G$. You may use any operations discussed in the lectures or cohort classes. To get full credit for this question, your algorithm should still run in $O((|V | + |E|) log |V |)$ time, where $|V |$is the number of vertices in $G$, and $|E|$ is the number of edges in $G$, and you should explain why your algorithm has running time complexity $O((|V | + |E|) log |V |)$.
***
```php
function initialise_single_source(G,s):
	'''
	Require: G = (V, E) is a weighted directed graph
	Require: s in V is a vertex
	'''
	for every vertex v in V:
		v.d <- \infty     // discomfort
		v.dist <- \infty  // distance
		v.pi <- NIL
	s.d <- 0
	s.dist <- 0


function mod_relax(u, v, w, ww)
	'''
	Require: A weight function w for G, representing discomfort
	Require: A weight function ww, representing distance
	Require: (u, v) is a directed edge of G
	Require: priority queue Q has decrease_key operation that can be accessed here
	'''
	// priority is to find min discomfort
	if u.d < w(u, v) then // current edge has higher discomfort
		v.d <- w(u, v) // retain largest discomfort
	else // infty or previous edges has larger discomfort
		v.d <- u.d // keep previous largest discomfort recorded
	
	// track pi here as path to return is shortest distance
	if u.dist + ww(u, v) < v.dist then
		v.dist <- u.dist + ww(u, v)
		v.pi <- u


function Mod_Dijkstra(G, w, ww, s, t)
	'''
	Require: A weight function w for G, representing discomfort
	Require: A weight function ww, representing distance
	Require: A vertex s and t of G
	Require: A DAG G represented as an adj list, where G.Adj[u] isthe LL of vertices adj to u
	'''
	initialise_single_source(G,s)
	S <- ∅ // initialise S as empty set
	Q <- G.V // Q is a min-priority queue. Elements of Q are vertices, and keys of these elements are the d values (discomfort)
	while Q != ∅
		u <- extract_min(Q) // u has smallest discomfort among vertices in Q, and it is removed from Q

		// if least discomfort vertex (u) found
		if (u == t) then
			// if reachable
			if (u.dist != \infty) then
				// implemented as array that elements are pushed
				// to the left. i.e. t at last position
				path <- Stack()
				path.push(u) // also t
				while u.pi != NIL
					path.push(u.pi)
					u <- u.pi
				return path
			else
				return "target is unreachable"
		else // target not extracted from Q yet
			S <- S ∪ {u} 
			for each vertex v in G.Adj[u]
				mod_relax(u, v, w, ww)
```
`initialise_single_source(G,s)`: $\Theta(|V|)$
`mod_relax(u, v, w)`: require `decrease_key` operation when assigning new $d$ and `dist` value, which each has complexity $O(\log{|V|})$, assuming we implement $Q$ as a min-heap. So overall `mod_relax` is also $O(\log{|V|})$
Initialise S as empty set: $\Theta(1)$
`extract_min(Q)`: implement Priority Queue as a min-Heap: $O(\log{|V|})$
Checks if target reached and reachable and return answer: $\Theta(1)$
S <- S ∪ {u}: $\Theta(1)$
Push to stack: $O(|V|)$ if path has all vertices

Overall complexity of `Mod_Dijkstra` using binary min-heaps: $O((|V| + |E|)\log{|V|})$
