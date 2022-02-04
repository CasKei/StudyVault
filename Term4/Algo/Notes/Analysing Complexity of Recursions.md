---
aliases: recursion complexity, analysing recurrences
tags: #50.004
---
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
T(n) $= 2T(n/2) + n
\end{align}
$$