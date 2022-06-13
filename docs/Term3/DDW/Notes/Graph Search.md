---
aliases: graph search, bfs, dfs
tags: #graph
---
Back to [[Data Driven World|DDW]]
# Graph Search
## Introduction
We may need to search a graph to solve problems such as shortest path.
The `Vertex` and `Graph` classes may need some additional attributes.
One way is to modify our classes to create a new class.
Here, however, we wish to introduce the concept of [[#Inheritance]], which allows us to ruse our existing class and create a new class that is derived from our existing class.
## Breadth First Search (BFS)

^7a8dcc

Normally used to find shortest path between 2 vertices.
![[Pasted image 20211227131010.png]]
Say we want shortest path from A to F.
Calculate distance of every vertex from A, find what leads to F shortest.
To do this, start with the starting vertex A. Then look into the neighbours, in this case B and D. Then explore the neighbours. We can draw the vertex that 
 we are exploring as a kind of tree. Then take turns to explore the neighbours of each child in the tree. If visited, mark it and don't revisit.
 ![[Pasted image 20211227132240.png]]
 Stop when all the vertices have been explored in terms of the children.
 Can use boolean or colour to indicate if the vertex has been visited.

 One way is to use a [[Stacks and Queues data structure#^55e4cd|queue]] data structure.
 When we visit a vertex, we put all its neighbours into a queue.
 This also ensures that we explore the vertices in a breadth-first manner.

 ```
 Input: Graph G, starting vertex s
 Output: Graph with distances on every vertex from s

 1. Initialise every vertex with
	 1. colour = white
	 2. distance = INF
 2. Start from s vertex
	 1. s.colour = grey
	 2. s.distance = 0
 3. Put s into queue
 4. while queue not empty
	 1. u = queue.pop
	 2. for neighbour of u:
		 1. if neighbour.colour = white:
			 1. neighbour.colour = grey
			 2. neighbour's distance to u's distance + 1
			 3. queue.push(neighbour)
	 3. all neighbours visited: u.colour = black
 ```
 The only thing about this is that we only get a graph with distances on each vertex, but we would not be able to retrieve the path to take from s to the destination.
 To find the shortest path, we need to store the parent vertex when we visit a neighbouring vertex.
  ```
 Input: Graph G, starting vertex s
 Output: Graph with distances on every vertex from s, parent vertex on every vertex that leads back to s

 1. Initialise every vertex with
	 1. colour = white
	 2. distance = INF
	 3. parent = NIL
 2. Start from s vertex
	 1. s.colour = grey
	 2. s.distance = 0
	 3. s.parent = NIL
 3. Put s into queue
 4. while queue not empty
	 1. u = queue.pop
	 2. for neighbour of u:
		 1. if neighbour.colour = white:
			 1. neighbour.colour = grey
			 2. neighbour's distance to u's distance + 1
			 3. neighbour.parent = u
			 3. queue.push(neighbour)
	 3. all neighbours visited: u.colour = black
 ```
 We have a new attribute called **parent**.
 In the beginning we set all vertices to have NIL as their parents.
 Since `s` is the starting vertex, it has no parent.
 Then we set `u` as the parent for all its neighbours, for all the `u`.

 Then from here we can write another algo to retrieve the path from `s` to some distination `v`.
 ```
 Find Path BFS
 Input: graph after running BFS G, start vertex s, end vertex v
 Output: list of vertices that gives the shortest path from s to v

 1. if v == s:
	 1. return [s]
 2. elif v.parent == NIL:
	 1. return "no path from s to v exist"
 3. else:
	 1. find-path(G, s, v.parent)
	 2. add v to the result from above^
 ```
 This uses recursion.
 There are 2 base cases: when destination = start, and when there is no path from s to v.
 We know that there is no path when along the path starting from v we find a vertex where parent is NIL.
 Recursion case is when we call the same function but with the destination vertex to be the parent of the current destination vertex.
 By moving hte destination vertex to the parent, we reduce the problem and make it smaller until we reach the base case.

 Before we can implement the algo, we need to modify the class `Vertex` to contain 3 more attributes: `colour`, `distance` and `parent`.
### Inheritance
An important concept in [[Object Oriented Programming|OOP]] that allows us to reuse existing classes.
Our previous [[Introduction to Graph#^aaec7e|`Vertex`]] only has `id` and `neighbours` as attributes.

Instead of modifying the existing class, we can create a new class with inheritance.
This allows us to create a new class without duplicating all the other parts that is the same.
We create a new class by deriving it from an existing base class.

Here we create `VertexSearch` that is derived from `Vertex`.
When a class inherits another class, it will possess all the attributes and methods of its parent class.
We will only need to specify the attributes and methods that the parent class does not have.
![[Pasted image 20211227140724.png]]
This **is-a** relationship is represented by the arrow iwth white triangle.
In python, 
```py
class NameSubClass(NameBaseClass):
    pass
```
So we have
```py
import sys

class VertexSearch(Vertex):
    def __init__(self, id=""):
        super().__init__(id)
        self.colour = "white"
        self.d = sys.maxsize
        self.parent = None
```
where
- `super().__init__(id)`: calls the parent class' initialisation method to initialise the parent attributes.
- `colour`: to be set to 'white'
- `d`: to be a large integer number
- `parent`: to be a `None` object

Redefining methods from parent class is called **method overriding**.
More about inheritance in next lessons.
## Depth First Search (DFS)

^729e6d

Explores neighbouring vertices in a depth-wise manner.
We go down the tree before moving to the next siblings.
![[Pasted image 20211227145430.png]]
Every time we visit a vertex, we put a timestamp on that vertex called **discovery time**.
Once we finish visiting all the neighbours of that vertex, we put another timestamp called **finishing time**.

We also identify edges differently
Tree edges: edges in the depth-first forest.
Back edges: edges connecting vertex u to ancestor v
This is the depth-first forest:
![[Pasted image 20211227145743.png]]

Use 2 functions, DFS and DFS-Visit
```
DFS
Input: graph G
Output: graph with the following attributes marked: colour, discovery time, finishing time, parent

1. Initialise each vertex with
	1. colour = white
	2. parent = NIL
2. set time = 0
3. for vertex in G:
	1. if vertex.colour == white:
		1. dfs-visit(G, u)
```
This initialises the vertices and goes through every vertex to perform the second function DFS-VISIT
```
DFS-Visit
Input: graph G, vertex to visit u
Output: graph with the following attributes marked: color, discovery time, finishing time, parent

1. current_time += 1
2. u.discovery_time = current_time
3. u.colour = grey
4. for vertex in u.neighbours:
	1. if vertex.colour == white:
		1. vertex.parent = u
		2. dfs_visit(G, vertex)
5. u.colour = black
6. current_time += 1
7. finishing_time = current time
```
This function simply sets the discovery time for the visited vertex u and begins to visit all the neighbouring vertices of u.
However, it only calls DFS-VISIT if the neighbours are white, which mans that these vertices have not been visited.
Once it finishes visiting all the neighbouring vertices, it marks vertex u to be black and sets the finishing time.

### Topological Sort
One application of DFS is to perform a topological sort.
For example, sort which task to be performed first given a list of tasks with dependencies.
We can use the finishing time of DFS to determine the sequence of tasks.

Performing DFS, the discovery time and the finishing time for each task is shown in the figure below.
![[Pasted image 20211227182906.png]]
In the process of DFS, it starts from 'undershirt' and traverses to all the children vertices in the tree.
After tis, it creates separate trees.
The depth-first forest looks like this
![[Pasted image 20211227183030.png]]
Reordering by finishing time from largest to smallest,
![[Pasted image 20211227183110.png]]
The first three are indepndent and interchangeable, but the rest are ordered.

```
TopSort
Input: graph G
Output: list of sorted vertices

1. DFS(G)
2. sort vertices based on finishing time from largest to smallest
3. return a list of sorted vertices
```