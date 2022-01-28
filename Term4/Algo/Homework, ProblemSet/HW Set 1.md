# 50.004 Homework Set 1
## Cassie Chong 1005301 CC01
### Qn 1
![[Pasted image 20220128100714.png]]
#### i)![[Pasted image 20220128101028.png]]
We have $f(n) = O(g(n))$.
This means there exists positive constants $c$ and $n_0$ such that $0 \leq f(n) \leq cg(n) \forall n \geq n_0$.

Suppose $2^{f(n)} = O(2^{g(n)})$ is true.
This implies there exists positive constants $c$ and $n_0$ such that $0 \leq 2^{f(n)} \leq c2^{g(n)} \forall n \geq n_0$.
That is, $2^{f(n)} \leq c2^{g(n)}$ should be true for positive $c$ and $n$.

Raise $f(n) = 3n$ and $g(n) = n$ as example.
$f(n) = O(g(n))$ is true as $3n = O(n)$.
Check $2^{3n} \leq c 2^{n}$:
	$$\begin{align}
	\Rightarrow \dfrac{2^{3n}}{2^n} &\leq c \\
	2^{2n} &\leq c
	\end{align}$$
There is no constant $c$ that can make this true as $n \to \infty$.
**Hence this statement is ==False==.**

#### ii)![[Pasted image 20220128101107.png]]
We have $f(n) = O(g(n))$ and $g(n) = O(h(n))$.
This means there exists positive constants $c$ and $n_0$ such that $0 \leq f(n) \leq c_0g(n) \forall n \geq n_0$, and $0 \leq g(n) \leq c_1h(n) \forall n \geq n_0$.
Hence, $$
\begin{align}
&0 \leq f(n) \leq c_0 g(n) \leq c_0c_1h(n)&, \forall n \geq n_0 \\
&\Rightarrow 0 \leq f(n) \leq c_3h(n)&, \text{where } c_3 = c_1 \cdot c_2, \forall n \geq n_0
\end{align}
$$
**Thus** $f(n) = O(h(n))$ **hence the statement is ==True==**

#### iii)![[Pasted image 20220128101117.png]]
$\Omega$ is a lower bound.
All algorithms take time, at least a constant time, so the lower bound running time is always at least $\Omega(1)$.
**Statement is ==True==.**

#### iv)![[Pasted image 20220128101128.png]]
$$\lim_{n \to \infty} \dfrac{f(n)}{n} = c_1, \lim_{n \to \infty} \dfrac{g(n)}{2n} = c_2, \text{ where }0<c<\infty$$


#### v)![[Pasted image 20220128101143.png]]
$$\log{n} \leq n \ \forall n \geq 0$$
Since upper bound of $f(n)$ is always larger than the upper bound of $g(n)$, we can conclude that the worst-case running time of B is lower than A.
However, this does not imply that B must always be faster than A for all $n$, only when $n \to \infty$. A might be faster than B for some small $n$ which we have no information about.
**Statement is ==False==.**

### Qn 2
![[Pasted image 20220128101153.png]]
#### i)
![[Pasted image 20220128101210.png]]
$$f(n) = 0 + 1^3 + 2^3 + \cdots + n^3$$
Lower bound 0 when $i = 0$
Upper bound $n^3$ or higher order
Adam True (discrete), Beatrice False, Colin True, Diana True
==**Ans: c**==

#### ii)
![[Pasted image 20220128101221.png]]


#### iii)
![[Pasted image 20220128101239.png]]
#### iv)
![[Pasted image 20220128101249.png]]
(edit: Errata: What is the ***biggest*** possible value of $k$...)
#### v)
![[Pasted image 20220128101302.png]]
### Qn 3![[Pasted image 20220128101312.png]]
#### i)
![[Pasted image 20220128101323.png]]
#### ii)
![[Pasted image 20220128101331.png]]
(Edit: Errata: last line is `print(f(n))`)
#### iii)
![[Pasted image 20220128101341.png]]
#### iv)
![[Pasted image 20220128101350.png]]
#### v)
![[Pasted image 20220128101401.png]]
### Qn 4![[Pasted image 20220128101413.png]]
![[Pasted image 20220128101422.png]]

### Qn 5![[Pasted image 20220128101430.png]]
#### i)
![[Pasted image 20220128101442.png]]
#### ii)
![[Pasted image 20220128101504.png]]
#### iii)
![[Pasted image 20220128101513.png]]
