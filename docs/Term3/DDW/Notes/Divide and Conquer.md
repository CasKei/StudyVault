Back to [[Data Driven World|DDW]]
# Divide and Conquer
Many computing problems are recursive in structure.
Recursive: to solve a given problem, they call themselves one or more times to solve a closely related problem.
These algorithms follow a *divide-and-conquer* approach.

The divide and conquer approach breaks the problem into several subproblems that are similar to the original problem but smaller in size.
Then the algorithm solves the smaller problems and combines the solutions to create the solution to the original problem.
The divide and conquer paradigm involves 3 steps at each level of the recursion:
1. Divide the problem into a number of smaller problems
2. Conquer the smaller problems by solving them recursively and when the problem is small enough, hopefully, it can be solved trivially
3. Combine the solutions of the smaller problems into the solution for the original problem.

## Recursive Basic Structure
In all recursive solutions, we always identify 2 cases.
1. Base Case
2. Recursve Case

## Example 1: Summing the Elements of an Array
Given an array, sum by iterating or recursion.
Iterative:
```py
def sum(array):
    result = 0
    for number in array:
        result += number
    return result
```
Recursive:
```py
def sum(arr):
	if len(arr) == 1:
		return arr[0]
	else:
		return arr[0] + sum(arr[1:])
```
### [[Analysing Computation Time|Computation Time]]
The iterative solution, this problem takes $O(n)$ time. This means that computation time increases linearly as the number of input increases.

For recursive solution, one way to find this is to draw the recursion tree.
Each node rpresents the cost of a single subproblem somewehre in the set of recursive function invocations. We have to do 2 sums, one to sum all the costs on each level of the tree to obtain a set of cost-per-level, another to sum all cost-per-level over all levels to get total cost.
![[Pasted image 20211224144213.png]]
This is recursion tree for [[#Example 1 Summing the Elements of an Array|summing elements in an array]].
The first figure on the left shows that the computation time for $n$ elements is a constant $c$ plus $T(n-1)$.
The second figure in the middle shows the tree when we expand $T(n-1)$ to $c$ plus $T(n-2)$.
We can continue until we are only left with one element, shown with the figure on the right with $T(1)$. The tree only has one child on each node and each level has the same cost which is shown by the arrow pointing to the right.
We can show that there are $n$ levels fo $n$ elements of input in the original call.

The cost fo each level is a constant $c$ and we have $n$ levels, so the total cost is $cn$, and therefore we can say that computation time for this recursion is ==$T(n)=O(n)$==
## Example 2: Factorial
Factorial iterative:
```py
def fact(n):
	if n < 0:
		return "invalid"
	result = 1
	for i in range(1, n+1):
		result *= i
	return result
```
Factorial recursive:
```py
def fact(n):
	if n == 0 or n == 1:
		return 1
	return n * fact(n - 1)
```
### [[Analysing Computation Time|Computation Time]]
- Check base case: constant time $O(1)$
	- If base case: return immediately: $O(1)$
- Else: $T(n)=O(1)+T(n-1)$. Constant time is time it takes to multiply $n$ with factorial of $n-1$. Second term is computation time to calculate the factorial of $n-1$.
We have the same recursive tree.
Computation time is also linear ==$T(n)=O(n)$==, a function of the input integer.

## Example 3: Tower of Hanoi
Given $n$ disks and three towers, one has to move the $n$ disks from the _source_ tower to the _destination_ tower using the other _auxilary_ tower.

The rules in moving the disks are as follows:
-   We can only move one disk at a time
-   A bigger disk cannot be placed on top of a smaler disk
Note that $n$ can be $1$ or greater.
### Base Case: $n=1$
1.  Move disk 1 from A to B
and we are done.
### Case: $n=2$
1.  Move disk 1 from A (source) to C (auxiliary)
2.  Move disk 2 from A (source) to B (destination)
3.  Move disk 1 from C (auxiliary) to B (destination)
### Case: $n=3$
The first step is to move the first two disks from A (source) to C (auxiliary).
We can use the steps above with the difference in the destination and auxiliary towers.
**Step 1**
1.  Move disk 1 from A (source) to B (destination)
2.  Move disk 2 from A (source) to C (auxiliary)
3.  Move disk 1 from B (destination) to C (auxiliary)

The next step is to move disk 3 from A (source) to B (destination).
**Step 2**
1.  Move disk 3 from A (source) to B (destination)

The last step is to move the two disks from C (auxiliary) to the destination tower B.
 This again involves a similar three steps with differences in the source and destination towers.
 **Step 3**
1.  Move disk 1 from C (auxiliary) to A (source)
2.  Move disk 2 from C (auxiliary) to B (destination)
3.  Move disk 1 from A (source) to B (destination)

We can see Step 1 as Moving two disks with tower A as the source and tower C as the destination using tower B as the auxiliary tower. Similarly, we can see Step 3 as moving two disks with tower C as the source and tower B as the destination with tower A as the auxiliary tower.
### General case for $n$ disks
```py
def ToH(n, A, B, C):
	result = []
	if n == 1:
		return [f'{n} from {A} to {B}']
	else:
		result = ToH(n-1, A, C, B)
		result += [f'{n} from {A} to {B}']
		result += ToH(n-1, C, B, A)
	return result
```
### [[Analysing Computation Time|Computation Time]]
Check base case: $O(1)$
If base case return: $O(1)$
Else: $T(n-1)$, $O(1)$, $T(n-1)$

Recursion tree:
![[Pasted image 20211224191233.png]]
There will be $n$ levels from $i=0$ up t $i=n-1$.
At each level, the sum total time is $2^2 \times c$. If we sum up all the levels, we have the following series:
$$
\begin{align}
T(n) &= \sum^{n-1}_{i=0}2^ic \\
&= c \sum^{n-1}_{i=0} 2^i \\
&= \frac{c(1-2^n)}{1-2} \\
&= c(2^n - 1) \\
&= O(2^n)
\end{align}
$$
This means that the computational time for the Tower of Hanoi proble is *exponential* with respect to the input.
As the input increases, the time it takes increases exponentially.

Notice that in this case $c=1$ as we can get the number of steps from $2^n-1$.