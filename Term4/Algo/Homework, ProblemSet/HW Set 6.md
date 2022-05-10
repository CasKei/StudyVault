---
tags: 50.004
---

# 50.004 HW6 Cassie Chong 1005301 CL01
## 1)
For each of the following statements, determine if it is true, false, or an open  
problem (i.e. we do not know yet). You do not have to justify your answers. [5 points]
### i) 
All NP-complete problems are solvable in polynomial time
==Open problem==

### ii) 
If P != NP, then no problem in NP is solvable in polynomial time.
==False==

### iii) 
A problem X is NP-hard if and only if there is a polynomial time reduction from 3-SAT to X.

X is NPcomplete if X in NP and X NPhard
X is NPhard if all problems Y in NP reduces to X
==True==

### iv) 
If P=NP, then 2-SAT is NP-complete.
==True==

### v) 
A problem in class NP is by definition ==only== solvable using non-deterministic algorithms.
==False==
## 2)
We have covered several $NP$-complete problems in Weeks 12, and we will cover more $NP$-complete problems in Week 13. Many other problems have been shown to be $NP$-complete, such as the 3-partition problem and the longest path decision problem on graphs, which can be easily found on Wikipedia. Please give **two** NP-complete problems other than those mentioned above or in class (Weeks 12–13). One of your NP-complete problems should be a *graph-related* problem (that is NOT the longest path decision problem on graphs); and the other should be a *non-graph-related* problem (that is NOT the 3-partition problem). 
To get full credit for each NP-complete problem, you would have to *specify exactly what the problem is* (not just the name of the problem), and you would have to indicate very clearly what the *input*(s) to the problem is/are, and what the *output*(s) to the problem is/are. In particular, is the output a “yes/no” answer, a numerical answer (e.g. the minimum number satisfying a certain condition), or something else (e.g. a path in a graph)? Is the input a set of objects, or a sequence of numbers, or something else? If your input is a graph, is this graph directed or undirected? Weighted or unweighted? Simple, or non-simple? Also, if your $NP$-complete problems involve any terminology, notation, or concepts, not covered in this course, you would have to define them. [5]
***
### Dominating set problem
> **Dominating set**:
> A dominating set for a graph $G = (V, E)$ is a subset $D$ of $V$ such that every vertex not in $D$ is adjacent to at least one member of $D$.

> **Domination number**:
> The domination number $\gamma(G)$ is the  number of vertices in a smallest dominating set for $G$.

> **Dominating set problem**:
> Tests whether $\gamma (G) \leq K$ for a given graph $G$ and input $K$.
> Inputs: $G$, $K$.
> Output: Yes/No $\implies$ $\gamma (G) \leq K$ or $\gamma (G) \not\leq K$

Type: Decision problem.
Graph: every kind of graph has an odd dominating set, so any graph can be applied.

### Maximising the number of rows cleared while playing the given piece sequence in Tetris
Assume: The sequence of all pieces that will be dropped is known.
Goal: to maximise number of rows cleared given the piece sequence, placing each piece one at a time, where rotations are possible (normal offline Tetris game)
Inputs: sequence of all pieces that will be dropped.
Outputs: The  way to play to maximise number of rows cleared. (piece placement and rotation per every piece in sequence).

## 3)
We define a simple undirected graph $G$ to be **almost-3-colourable** if we can assign one of 3 colours to each vertex such that there are at most **two** edges in G, each of whose two endpoints have the same colour. (The two endpoints of an edge are the two vertices that the edge is incident to.) We shall call such a colouring an almost-3-colouring. We can also define the *almost-3-colouring problem* to be the problem of deciding whether a given simple undirected graph G is almost-3-colourable. In this question, we will show that this problem is NP-complete.
### i)
Show that there is a polynomial time reduction from the 3-colouring problem (as defined in L13.01 Slide 12, i.e. the k-colouring problem with k = 3) to the almost-3-colouring problem. [2.5 points]
***
Observe that:
Any undirected graph that can satisfy 3-colouring is also definitely almost 3-colouring based on the above definition.
The converse, however, is not true, as there exists problems that are almost 3-colouring satisfiable but not 3-colouring.
Thus some additional procedure must exist to consider if, for each vertex, there are any of its adjacent vertexes with the same colour, in order to reduce the 3-colouring to almost 3-colouring problem.
This procedure is done within the algorithm, so it is also at least NP-hard since 3-colouring is NP hard.

### ii)
Show that there is a polynomial time reduction from the almost-3-colouring problem to the 3-colouring problem. [2.5 points]
***
Same observation as above:
Any undirected graph that can satisfy 3-colouring is also definitely almost 3-colouring based on the above definition.
The converse, however, is not true, as there exists problems that are almost 3-colouring satisfiable but not 3-colouring.
Thus, if we have the almost 3-colouring problem solution, some additional procedure must exist to consider if any adjacent vertices have the same colour.
This procedure is done within the algorithm, so it is also at least NP-hard since 3-colouring is NP hard.
From the slides, we have
$$\text{If } A \leq_p B \text{ and } B\leq_p A \text{, then we write } A \cong_p B$$
A is almost 3-colouring, B is 3-colouring. Since they are both harder than the other, both are NP-hard. Since both are NP and algorithm can verify a solution in some polynomial time, both are NP-complete.

## 4)
Suppose that $\text{Independent\_set}(G, k)$ is a procedure that takes as its two inputs a simple undirected graph $G$ and a non-negative integer $k$, and returns as its output a “yes/no” answer, whether an independent set of size $k$ exists in $G$. (For the definition of an independent set, please see *L13.02 slide 13*). Suppose further that this procedure has polynomial time complexity in terms of the number of vertices in the input graph G.
![[Pasted image 20220417003618.png]]

### i)
**Describe** an algorithm that uses the above procedure as a subroutine to determine the ==maximum size of an independent set== in $G$, such that your algorithm runs in *polynomial* time in terms of the number of vertices in the input graph $G$. You may present your algorithm either in words or in pseudocode. **Justify** why your algorithm works *AND* why it runs in polynomial time, in as much details as possible. [1 point]
***
Utility function: `independent_set(G, k)`
- Polynomial time complexity

Require: $G$ has $n$ vertices.
```php
maxsize <- 0
for i from n downto 1:
	if (independent_set(G, i) == true)
		maxsize ++
print maxsize
```
The algorithm is correct as `independent_set(G, k)` checks if the given graph $G$, at the $i^{th}$ vertex, has its subgraph pairwise non-adjacent or not. We check every vertex in $G$ and if this condition is satisfied, add to the count. Then the count is the answer.

### ii)
**Describe** an algorithm that uses the above procedure as a subroutine to find ==any one independent set of maximum size== in the input graph $G$, such that your algorithm runs in *polynomial* time in terms of the number of vertices in the input graph $G$. (If there are multiple possible independent sets of maximum size, then your algorithm should return just one of them.) You may present your algorithm either in words or in pseudocode. **Justify** why your algorithm works *AND* why it runs in polynomial time, in as much details as possible. [4 points]
***
We only need one independent set of maximum size.
Utility function: `independent_set(G, k)`
- Polynomial time complexity

Require: $G$ has $n$ vertices.
Run an algorithm that has some polynomial reduction from `independent_set(G, k)`. For `independent_set(G, k)`, a coompleted set of maximum size must be found first, hence the set can be found in some complexity at most equal to that of `independent_set(G, k)`. 
## 5)
In Lecture 12.2, we showed that the knapsack problem is $NP$-hard by demonstrating a polynomial-time reduction of the ($NP$-complete) partition problem to the knapsack problem, and in Cohort Class 10.3 we derived a (dynamic programming) algorithm to solve the knapsack problem in $O(nm)$ time, where n is the number of items and m is the capacity of the knapsack. Why does this **NOT** imply that $P=NP$? (Hint 1: Look at Lecture 12.1 Slide 3 very carefully. Hint 2: What does “polynomial-time” mean exactly?)
***
NP - Non-deterministic polynomial time.
The yes answer can be verified, but not the no answer.
This implies there is different behaviours of algorithms on different runs (non-deterministic definition), whereby some lucky guess of the algorithm can solve it in polynomial time. However it is not verifiable.
If we have $P=NP$, then the answer is both solvable and verifiable in polynomial time.
Finding one solution of knapsack may be polynomial, but we cannot verify that it is correct in a surely polynomial way.