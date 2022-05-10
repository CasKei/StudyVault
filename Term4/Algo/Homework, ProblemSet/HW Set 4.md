---
tags: #50.004
---

# 50.004 HW4 Cassie Chong 1005301 CC01
## 1)
![[Pasted image 20220319092551.png]]
### i)
Give the adjacency-list representation of $G$. When giving your answer, please order the vertices alphabetically.
***
![[Pasted image 20220319102825.png]]

### ii)
Give the adjacency-matrix representation of $G$. When giving your answer, please order the vertices alphabetically.
***

| **a**   | **b**   | **c**  | **d**   | **e**   | **f**   | **g**   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 0   | 0   | 0   | 0   | 0   | **a**   |
| 0   | 0   | 1   | 0   | 0   | 0   | 0   | **b**   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | **c**   |
| 1   | 1   | 0   | 0   | 0   | 0   | 0   | **d**   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | **e**   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | **f**   |
| 1   | 0   | 0   | 1   | 0   | 0   | 0   | **g**   |
<br>
## 2) 
Consider the directed graph $G$ in Fig. 1, and run the breadth-first search on $G$, with vertex $c$ as the source vertex. Assume that at each level, the vertices are traversed in alphabetical order.

### i)
Show the $d$ and $\pi$ values that result from running breadth-first search on the directed graph $G$. Note that $d$ is the attribute representing the distance/level for the breadth-first search, while $\pi$ is the attribute representing the pointer that points to the previous vertex.  
You can write in the form of $Vertex(d, \pi)$. For example, if $x$ is a vertex such that $x.d = 1$ and $x.\pi = y$, then you can write $x(1, y)$.
***
| $Vertex$ | $d$ (distance) | $\pi$ (parent) | Ans        |
| -------- | -------------- | -------------- | ---------- |
| c        | 0              | NIL            | $c(0,NIL)$ |
| e        | 1              | c              | $e(1,c)$   |
| f        | 1              | c              | $f(1,c)$   |
| b        | 2              | e              | $b(2,e)$   |
| g        | 2              | f              | $g(2,f)$   |
| a        | 3              | g              | $a(3,g)$   |
| d        | 3              | g              | $d(3,g)$   |


### ii)
Based on your answers from the previous part, find a shortest path from vertex $c$ to vertex $d$. Make sure you use the $d$ and $\pi$ values of the vertices of $G$.
***
![[Pasted image 20220319111556.png]]
One shortest path is $c \to f \to g \to d$.
<br>
## 3)
Given an undirected graph $G$, we define $G − v$ to be a ==subgraph of $G$ formed by removing the vertex $v$ and all edges incident to $v$ from $G$.== We define a vertex $v$ in a connected undirected graph $G$ to be a ==cut vertex if the subgraph $G − v$ is not connected==.
For this question, let $G$ be a given undirected graph, let $r$ be some vertex of $G$, and let $T$ be any DFS tree of $G$ rooted at $r$. Note that any DFS tree of an undirected graph must be directed by definition.

### i)
Show that $r$ is a cut vertex of $G$ if and only if $r$ (treated as a vertex in $T$ ) has more than one child in $T$ .
***
$r$ is the root of the DFS tree $T$.

Suppose $r$ has no children. Since it is the root, it is the sole vertex in the whole graph. Removing it will result in an empty subgraph $G-r$ that by definition cannot be disconnected. So $r$ is not a cut vertex.

Suppose $r$ has one child in $T$. If $r$ is removed, the affected edges include the tree edge between $r$ and its child in $T$, and the back edges of $r$ linking it to its ancestors , not shown in $T$ but in $G$. However, from the DFS graph, the removal of the root with one child does not disconnect the rest. So $r$ is not a cut vertex.

Suppose then $r$ has more than one child in $T$. A DFS traversal goes from $r$ to one of its children, and to all its unvisited descendants, before backtracking to its next child and its descendants. So if a constructed DFS tree from a DFS traversal from $r$ has more than one child, that means that the traversal has had to backtrack back to $r$ to access unvisited vertices that are not in the path of the first child accessed. Therefore, there is only one path connecting the children of $r$ in $T$, in $G$. If $r$ is removed from $G$, its children in $T$ will find no path connecting each other in $G$ as its sole path through $r$ is removed. Hence, removing $r$ when $r$ has more than one child will cut off $G$ into disjoint subgraphs, making it disconnected.

### ii)
Show that a vertex $v \not = r$ (i.e. $v$ is not $r$) is a cut vertex of $G$ if and only if, when $v$ is treated as a vertex in $T$ , there is at least one child $c$ of $v$ such that no descendant of $c$ (including $c$ itself) shares an edge (in $G$) with a proper ancestor of $v$.
Hint: CLRS Theorem 22.10 states that every edge in a depth first search of an undirected graph is either a tree edge or a back edge.
***
Now $v$ is not the root of the DFS tree $T$. It has an ancestor connecting to the root, if not the root itself. It may or may not be a leaf of $T$.

If there is no child of $v$, it is a leaf in the DFS tree, and removing it will not disconnect the graph since all other edges of $T$ are untouched other than the one removed.

If $v$ has children, we denote one of it by $c$ as in the question. Suppose we remove $v$. Since $v$ is connected to the subtree rooted at $c$ in $T$ via the edge $(v,c)$, if $v$ is removed, then the child subtree rooted at $c$ will be separated from the subtree rooted at $r$ of $T$, if we only look at the DFS tree $T$. Since every edge in the DFS tree of an undirected graph is either a tree edge or a back edge, and only the tree edges are visible in $T$, for the subtree rooted at $c$ to be connected to the subtree at $r$ after removing the tree edges connecting them by removing $v$, there must exist back edges from any vertex in the subtree of $c$ connecting to an ancestor that lead to $v$. If no such back edge exists, then the removal of $v$ disconnects the graph $G$ and hence $v$ is a cut vertex.
<br>
## 4)
Suppose you have just enrolled into Singapore University of Technical Difficulties, and you wish to graduate as fast as possible. 
To graduate, you are required to take a total of $n$ modules. For simplicity, we assign each of these $n$ modules a unique number in $\set{1, \dots , n}$. Each of these $n$ modules has a set of pre-requisite modules. You may assume that all pre-requisite modules must be modules from among $\set{1, \dots , n}$. To be clear, if module $a$ is a pre-requisite course for module $b$, and if module $b$ is a pre-requisite module for module $c$, then module a is also a pre-requisite module for module $c$. You may also assume that it is possible to graduate, so in particular, there is at least one module with no pre-requisite modules that you can take in your first semester. In any given semester, you may take any number of modules for which you have already taken all necessary pre-requisite modules in previous semesters.  

Design an algorithm that takes as its single input an array $P [1..n]$ whose entries are linked lists, and returns as its output a number representing the minimum number of semesters you will need to take to graduate. For the input array $P [1..n]$, assume that its length $n$ represents the total number of modules, and that its $m$-th entry $P [m]$ is a linked list whose elements are integers in $\set{1, \dots , n}$, representing the pre-requisite modules for module $m$. (The elements of each linked list may be arranged in arbitrary order. Hint: You can think of $P [m]$ as an adjacency list.) Analyse the running time complexity of your algorithm in terms of $n$ and $p$, where $n$ is the total number of modules, and $p$ is the sum of the total number of pre-requisite modules for all $n$ modules, i.e. $p$ is the sum of the sizes of all $n$ linked lists in $P$ . You may use any operations or algorithms discussed in the lectures or cohort classes in your algorithm.  
Please state any additional assumptions that you use. For full credit, your algorithm should have time complexity $O(n + p)$.
***
Assumption: this university does not allow me to repeat modules (module path is acyclic), and given the pre-requisites of some modules, the modules can be represented as a directed acyclic graph (DAG).

Input: array $P[1\dots n]$ of linked lists, which $m^{th}$ entry $P[m]$ is a LL with elements are integers in $\set{1 \dots n}$ that are the prereq for module $m$.
An array of linked lists is already a representation of a graph in adjacency list, so we can take the input as a graph in this form.
Output: number of semesters needed to graduate.
```php
// Searching O(n), but n decreases every time
function thisSem(P)
	Create new list ls[]
	for mod in P
		if mod.next == NIL: // mod is a LL with attribute next.
			ls.add(mod) // or append
			takenMod(P, mod)
	return ls[]

// Search in P: O(n), seaching prerequisites: O(p) in total since they get deleted
function takenMod(P, mod)
	for module in P
		if mod == module
			P.delete(mod) // delete from P since module considered taken
		for prereq in module
			if prereq == mod
				P[prereq].delete(mod) // delete prerequisite since satisfied

// Constant multiple of O(n) and O(p) added
function solution(P)
	Create Map<Integer, List> sems_mods
	semCount <- 0

	while P is not empty do
		thisSemLs <- thisSem(P) // mods to take this sem
		semCount += 1 // start from 1 and increment
		sems_mods.put(semCount, thisSemLs) // put this into a key value pair in the map
	return sems_mods.size //semCount is the number of semesters needed
```
Create a map, with its keys being the semester number, and its values being the modules that can be taken during that semester.
As we keep deleting taken mods from P, even though for loops are used, the number of iterations keep decreasing. We will delete mods n times to take n mods. As we go along, we will also delete all prerequisites as they get taken.
In the worst case, we have to take n mods in n semesters, where each mod's prerequisites includes all the mods that came before it. If we run this algorithm, we delete 1 mod + its prerequisites, which is n, then delete n-1, then delete n-2, up until n is 0. This is equivalent to going through every mod and its prerequisite once.
Hence its complexity is worst case $O(n + p)$.

In hindsight the map isn't needed in this case as the question is asking for number of semesters only, so simply incrementing the count is enough. But with the map, we can see and store what mods to take at each sem.
<br>
## 5) 
A 1-dimensional variable jumping maze can be represented as an array of integers $A[1..n]$, and an initial jump distance $j_1$. A token starts on the left-most square (index 1), and your goal is to bring the token to the rightmost square at index n.
![[Pasted image 20220319093848.png]]
For each turn $t$, starting from turn $t = 1$, you are allowed to move your token exactly $j_t$ steps left or right. These $j_t$ steps must all be in the same direction in that turn, which means that at each turn you are deciding between the two directional choices. Then, your jump distance $j_t+1$ in the next turn $t + 1$ will change by the value under the token, meaning that $j_t+1 = j_t + A[x_t]$. 
For example, the maze in Figure 2 can be solved in the following steps:
1. Move the token from 1 to 4. $j_2 = 3 − 1 = 2$  
2. Move the token from 4 to 2. $j_3 = 2 + 0 = 2$  
3. Move the token from 2 to 4. $j_4 = 2 − 1 = 1$  
4. Move the token from 4 to 3. $j_5 = 1 + 1 = 2$  
5. Move the token from 3 to 5. $j_6 = 2 + 0 = 2$
6. Move the token from 5 to 7.

Note that for any valid solution, your token is not allowed to go out of bounds (of the indices from $1$ to $n$), and strictly negative jump distances are not allowed. You may also assume that $A[n] = 0$. (This means that in any valid solution, the jump distance cannot become $0$ in any turn.)

Design an algorithm that takes as its two inputs an integer array $A[1..n]$ (whose last entry $A[n]$ has value $0$) and a positive integer $j_1$ (representing the initial jump distance), and returns as its output either the minimum number of steps required to solve the maze, if a solution exists; or the value $−1$, if no such solution exists. For example, given the input integer array depicted in Figure 2 and an input initial jump distance $j_1 = 3$, your algorithm should return as its output the number $6$. Analyse the running time complexity of your algorithm in terms of $n$. You may use any operations or algorithms discussed in the lectures or cohort classes in your algorithm. Please state any additional assumptions that you use. (In particular, for any graph that you initialize, please state explicitly what graph representation you are using.)
***
Inputs: int array $A[1...n]$, initial jump distance $j_1$
Output: maximum number of steps required to solve maze if have solution, else -1

We need a way to track the nature of the positions we visit.
```php
class Point()
	Point(val)
		this.color = "WHITE"
		this.currentDists = []
		this.val = val

function solution(A, j1)
	count = 0
	position = 1
	position_arr = []

	for (i = 1; i <= A.length; i++)
		pos = Point(A[index])
		position_arr.append(pos)

	count = helper(position_arr, position, j1, count)
	return count

function helper(position_arr, position, jump, count)
	// out of range or no jump available
	if (position <= 0 || position > position_arr.length || jump == 0)
		return -1
	// reached end
	else if position == position_arr.length
		return count
	// more possible moves
	else if position_arr[position].color == "grey"
		if jump in position_arr[position].currentDists // jump same as old position == loop
			return -1

	jump += position_arr[position+1].value // change jump according to array entry (use next entry to get next jump value)
	count += 1 // moves are valid. increase count.

	position_arr[position].color = "GREY"
	position_arr[position].currentDists.append(jump) // add jump to distance arr

	// recurse for next 2 possible positions
	nextPos1 = position - jump
	nextPos2 = position + jump
	count1 = helper(nextPos1, position, jump, count)
	count2 = helper(nextPos2, position, jump, count)

	if count1 < 0 // out of range
		ans = count2
	else if count2 < 0 // out of range
		ans = count1
	else 
		ans = min(count1 , count2) // return shortest path if both paths valid

	position_arr[position].color = "BLACK" // mark visited since all paths from node explored
	return ans // shortest path required
```
The helper function branches into the moves' two possible moves, to the left or to the right, whilst checking for loop, and out of range base cases, done recursively for all possible moves any branch can go.
A DFS graph is used to find if the maze has a solution for each possible move.
If more than one possible move is found, it is to return the shortest path.
This DFS search takes $O(V+E)$ time complexity. The graph will only reach one correct answer if there is one. In the worst case where there is a solution and the pointer has to jump to $n$ vertices out of a total of $n$ vertices where each vertex represents one possible state in the path the pointer can ever jump to, the graph DFS can reach a total of $n$ vertices with $n-1$ edges.
Total time complexity is then $O(n + (n-1)) = O(2n-1) = O(n)$.