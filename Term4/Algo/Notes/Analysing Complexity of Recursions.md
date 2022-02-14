---
aliases: recursion complexity, analysing recurrences
tags: #50.004
---
[[Algo]]
[[Algo week 2]]
[[L02.01 - Sorting, solving recursion]]
[[Insertion Sort and Merge Sort]]

## Technicalities in recurrences
In practice, we neglect certain technical details when we state and solve recurrences
- Assume $T(1) = \Theta(1)$, because the running time of an algo on a constant sized input is a constant
- Assume $n$ is divisible by the constant denominator in recurrences

When we state and solve recurreces, we forge ahead without these details since they usually do not influence the order of growth
<br>
## Solving Recurrences by Expansion (Recursion Tree)
Recursion tree = sum of cost of nodes
**e.g. draw the tree of** $T(n) = 2T(n/2) + \Theta(n)$:
![[Pasted image 20220204115926.png]]
Height of the tree: $\log{n}$ levels.
Sum each level, then sum all levels.
$T(n) = nT(1) + cn\log{n} = \Theta(n\log{n})$
<br>
**Another example**
![[Pasted image 20220204115830.png]]
<br>
**Another example**
![[Pasted image 20220204120302.png]]
<br>
## Solving Recurrences by Induction (Substitution)
- Make a guess
- Use substitution method to prove it

### Example
For $T(n) = 2T(n/2) + \Theta(n)$, prove $T(n) = O(n\log{n})$.

According to Big O definition, we need to prove that there is a $n_0$ that when $n \geq n_0$, there is a constant $c>0$ such that $T(n) \leq cn\log{n}$.

Assume that $T(n) \leq cn\log{n}$ is true for all $m < n$, expecially $m = n/2$.
Then we have
$$
\begin{align}
T(n) &= 2T(n/2) + n\\
&\leq 2c\left(n/2\right)\log{(n/2)} + n\\
&= cn(\log{n} - \log{2})+n\\
&= cn\log{n} - cn\log{2} + n\\
&= cn\log{n} + n(1-c\log{2}) \leq cn\log{n} &(\text{when }1\leq c\log{2})
\end{align}
$$
We can easily find such a $c \geq \frac{1}{\log{2}} \approx 1.44$
This is second step

**Boundary conditions**
The substitution method requires us to test the boundary cases.
> **Boundary conditions:** the smallest or biggest value that a variable of a function could be.

For our case, no upper limit, so lower limit $n=1$
However, when $n=1$, $cn\log{n} = c\log{1} = 0$.
We know our $T(1) = \Theta(1) > 0$ as there is no algorithm that takes no time.

==CONT==.