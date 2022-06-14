---
tags: 50.042
---
[[50.042 Foundations of Cybersecurity|50.042]]
[[Multiplicative Inverse]]

## Affine mapping
The following equation expresses an affine transformation of $GF(2^8)$ viewed as an 8-dimensional vector space over $GF(2)$, that is used in the crypto-algo [[AES]]:
$$\set{a'} = \set{a} \oplus \set{v}$$
where $\begin{bmatrix}M\end{bmatrix}$ is the matrix below, $\set{v}$ is a fixed vector and $\set{a} = (a_0, a_1, a_2, ..., a_7)$.
$$
M\set{a} = 
\begin{bmatrix}
1&0&0&0&1&1&1&1\\
1&1&0&0&0&1&1&1\\
1&1&1&0&0&0&1&1\\
1&1&1&1&0&0&0&1\\
1&1&1&1&1&0&0&0\\
0&1&1&1&1&1&0&0\\
0&0&1&1&1&1&1&0\\
0&0&0&1&1&1&1&1\\
\end{bmatrix}
\begin{bmatrix}
a_0\\a_1\\a_2\\a_3\\a_4\\a_5\\a_6\\a_7
\end{bmatrix}

\text{ and }
\set{v} =
\begin{bmatrix}
1\\1\\0\\0\\0\\1\\1\\0
\end{bmatrix}
$$

So overall:
$$
\begin{pmatrix}
b_0\\b_1\\b_2\\b_3\\b_4\\b_5\\b_6\\b_7
\end{pmatrix} =
\begin{pmatrix}
1&0&0&0&1&1&1&1\\
1&1&0&0&0&1&1&1\\
1&1&1&0&0&0&1&1\\
1&1&1&1&0&0&0&1\\
1&1&1&1&1&0&0&0\\
0&1&1&1&1&1&0&0\\
0&0&1&1&1&1&1&0\\
0&0&0&1&1&1&1&1\\
\end{pmatrix}
\begin{pmatrix}
b'_0\\b'_1\\b'_2\\b'_3\\b'_4\\b'_5\\b'_6\\b'_7
\end{pmatrix}
+
\begin{pmatrix}
1\\1\\0\\0\\0\\1\\1\\0
\end{pmatrix}
\text{ mod } 2
$$
