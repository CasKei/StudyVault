---
aliases: algo class 1
tags: #50.004, #practice
---
[[L01.01 - Basic Definitions and Complexity]]
[[L01.02 - Document Distance]]
[[Algo week 1]]
[[Algo]]

# C01
### Problem 1
![[Pasted image 20220125155603.png]]

|f(n)| 1s| 1min| 1hr| 1day| 1mth| 1yr| 1century|
|---|---|---|---|---|---|---|---|
|lg n|$2^{10^6}$|||||||
|$n^{0.5}$  |$10^{12}$|||||||
|n|$10^6$|||||||
|n lgn||||||||
|n^2|$10^3$|||||||
|n^3|$10^2$|||||||
|2^n||||||||
|n!||||||||

### Problem 2
$$
\begin{align}
f(x) &= x\\
g(x) &= x+2
\end{align}
$$
$f \in O(g)$?: True
$g \in \Omega(f)$?: True
$g \in O(f)$?: True

### Problem 3
$$x+2 \leq x \cdot ?$$
Any constant greater than 1.
$$g \in O(f)?$$
### Problem 4
$$
\begin{align}
f(x) &= x^2 \\
g(x) &= x^2 + 2 \\
h(x) &= x^2 + 3x + 2
\end{align}
$$
$f \in O(g)$?: True
$f \in O(h)$?: True
$f \in \Omega(g)$?: True
$f \in \Omega(h)$?: True

### Problem 5
$$
\begin{align}
f(x) &= x^2 \\
g(x) &= 1000x^2 + 500x + 100 \\
\end{align}
$$
$f \in \Omega(g)$?: True
$100x^2 + 500x + 100 \in \Theta(x^2)$

### Problem 6
$1000x^2 \in \Theta(x^3)$?: False

### Problem 7
$$
\begin{align}
f(x) &= 1000x^2 \\
g(x) &= x^3 \\
\end{align}
$$
$g \in O(f)$?: False
$g \in \Omega(f)$?: True
$f \in O(g)$?: True
$f \in \Omega(g)$?: False
$f \in \Theta(g)$?: False
$g \in \Theta(f)$?: False

### Problem 8
$$
\begin{align}
f(x) &= x \\
g(x) &= \log_2{x} \\
\end{align}
$$
$f \in O(g)$?: False
$f \in \Omega(g)$?: True
$g \in O(f)$?: True
$g \in \Omega(f)$?: False
$f \in \Theta(g)$?: False

### Problem 8.1
$$
\begin{align}
f(x) &= x \\
g(x) &= (\log_2{x})^2 \\
\end{align}
$$
$f \in O(g)$?: False
$f \in \Omega(g)$?: True
$g \in O(f)$?: True
$g \in \Omega(f)$?: False
$f \in \Theta(g)$?: False
Same. Does not matter how many.

### Problem 9
$$\begin{align}
f(x) &= n \log_2{n} \\
g(x) &= n^2 \\
\end{align}$$
$f(n) \leq g(n)$ so
$f \in O(g)$?: True
$f \in \Omega(g)$?: False
$g \in O(f)$?: False
$g \in \Omega(f)$?: True
$f \in \Theta(g)$?: False

### Problem 10
$$
\begin{align}
g(n) &= n^2 \\
f(n) &= n\log_2{n} \\
h(n) &= n\\
b(n) &= \log_2{n}
\end{align}
$$
$g \in O(100f)$: False
$g \in \Omega(f)$: True
$b \in O(f)$: True
$b \in \Theta(f)$: False
$h \in O(b + h)$: True
$g \in \Omega(g + h)$: True
$g \in \Theta(g + h)$: True

### Problem 11
We are given that an algo has complexity $O(\log{n})$ in the given input size n.
Explain why the complexity for this is also $O(\log_b{n})$, regardless of the choice of any base $b > 1$ for the logarithm appearing in the expression.

Since big O notation, $0 \leq f(n) \leq c \cdot g(x)$, where $g(x) = \log{n}$.
We have $\log_b{n} = \dfrac{\log{n}}{\log{b}}$ where $\log{b} > 0$.
$$
\begin{align}
0 &\leq f(n) \leq c \cdot g(x)\\
0 &\leq \dfrac{f(n)}{\log{b{}}} \leq \dfrac{c \cdot \log{n}}{\log{b}} = \log_b{n}\\
0 &\leq f(n) \leq \log{b} \cdot c \cdot \log_b{n}
\end{align}
$$
Where $\log{b} \cdot c$ is $c_1$.

---

Interpreting the given complexity to have a base 2, applying change of base to base b, we have
$$
\begin{align}
O(\log_2{n})&=O\left(\dfrac{\log_b{n}}{\log_b{2}}\right)\\
&= O \left(\dfrac{1}{\log_b{2}} \cdot \log_b{n}
\right)\\
&= O \left(\log_b{n}\right)
\end{align}
$$
Since $O\left(\dfrac{1}{\log_b{2}}\right)$ is a constant and of lower order than $O(\log_b{n})$.