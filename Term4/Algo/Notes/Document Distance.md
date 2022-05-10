---
aliases: reading pseudocode, case analysis, cost model, document distance
tags: #50.004
---
[[Basic Definitions and Complexity]]
[[algo - C01]]
[[Algo week 1]]
[[Algo]]

## How to read code and find its T(n)
### Constants
`print "great"`
This takes T(n) = 1
i.e. the numebr of steps required to complete this program is 1.
This code has complexity $\Theta(1)$
<br>
```python
print "great"
print "great"
print "great"
```
This takes T(n) = 4
i.e. the numebr of steps required to complete this program is 4.
This code has complexity $\Theta(1)$
### Loops
```python
for (i=0; i<5; i++)
	print('great')
```
Iterator i: 0,1,2,3,4
T(n) = 5
i.e. the number of steps required to complete the program is 5
Complexiy $\Theta(1)$
<br>
```python
for (i=0; i<n; i++)
	print('great')
```
Iterator i: 0 to n-1
T(n) = n
i.e. the number of steps required to complete the program is n
Complexiy $\Theta(n)$
<br>
```python
for (int i=0; i<n; i++)
	for (int j=0; j<n; j++)
		print('great')
```
$T(n) = n^2$
i.e. the number of steps required to complete this program is n^2
This code has complexity $\Theta(n^2)$
<br>
```python
for (int i=0; i<n; i++)
	for (int j=0; j<n; j++)
		print('great')
for (k=0; k<n; k++)
	print('great')
```
$T(n) = n^2 + n$
This code has complexity $\Theta(n^2)$
<br>
```python
for (i=0; i<n^0.5; i++)
	print('hi')
```
$T(n) = \Theta(\sqrt{n})$ 
<br>
```python
for (i=0; i<n^0.5; i++)
	for (j=0; j<n^0.5; j++)
		print('great')
```
$T(n) = \Theta(\sqrt{n} \cdot \sqrt{n}) = \Theta(n)$
<br>
```python
for (i=0; i<n; i++)
	for (j=0; j<=i; j++)
		print('hi')
```
$T(n) = \Theta\left(\dfrac{n(n+1)}{2}\right)=\Theta(n^2)$
<br>
![[Pasted image 20220125154704.png]]
j: 2 to n
i: j-1 to 1
$T(n) = \Theta\left(\dfrac{n(n+1)}{2}\right)=\Theta(n^2)$

## Worst-case and Average-case analysis
- Always use worst-case
- We should not hope that the 'worst case' will not happen
- For some algorithms, the worst case occurs fairly often
- The 'average case' is often as bad as the worst case.
<br>
## Cost model of code
Python cost model

**List: $L = [a_1, a_2, \dots, a_n]$**

|Commands|Time Complexity|
|---|---|
|`L[i] = x`|$\Theta(1)$|
|`L.append(x)`|$\Theta(1)$|
|`L1.extend(L2)`|$\Theta(len(L2))$|
|`A = L1 + L2_`|$\Theta(len(L1) + len(L2))$|
|`x in L`|$\Theta(len(L))$|

**Dictionary: $D = \set{x_1: y_1, x_2: y_2, \dots, x_n:y_n}$**

|Commands|Time Complexity|
|---|---|
|`D[x] = y`|$\Theta(1)$|
|`x in D`|$\Theta(1)$|
<br>

## Document Distance
**Document**: sequence of words
**Problem**: Given 2 documents, find out how similar they are
**Algorithm**: below

### Usage
1. Plagiarism detection
2. Website update checking

### Problem definition
**document `D`**: raw input consisting of a string of characters
**word array `Dwords`**: An array of words as they appear in `D`
**word dictionary `W`**: a dictionary of unique words and their corresponding number of occurences
**word frequency `D(w)`**: For each `w` in `W`, word frequency is the number of occurrences of word `w` in `D`

### Vector Space Model
-> Treat each document as a vector of its own words
	-> One coordinte per word of the English dictionary
	```doc1 = "the cat"
	doc2 = "the dog"```
The **dot product** of `D1` and `D2` represents their similarity.
$$D_1 \cdot D_2 \equiv \sum_w{D_1(w)\cdot D_2(w)}$$
e.g. 
$$
\begin{align}
\text{'the cat'} \cdot \text{'the dog'} &= [the \times the + cat \times dog]\\
&= 1+0\\
&= 1
\end{align}
$$
$$
\begin{align}
\text{'the the cat cat'} \cdot \text{'the the dog dog'} &= [the \times the + the \times the + cat \times dog+ cat \times dog]\\
&= 1+1+0+0\\
&= 2
\end{align}
$$
 Both are 50% similar so we need to **normalise** the result
 $$
\begin{align}
[\text{'the cat'} \cdot \text{'the dog'}]/\sqrt{2\times2} &= [the \times the + cat \times dog]/2\\
&= [1+0]/2\\
&= 0.5=50%
\end{align}
 $$
<br>

***Normalisation***: divide by the length of the vectors
$$\dfrac{D_1 \cdot D_2}{|D_1||D_2|}$$
**Measure distance by angle**:
$$\cos{\theta} = \dfrac{D_1 \cdot D_2}{|D_1||D_2|}$$
$$
\begin{align}
\theta &= 0, &\text{Documents are identical, } &D_1=aD_2\\
&&(\text{If of the same, permutations of each other})\\
\theta &= \dfrac{\pi}{2}, &\text{No word is shared at all. Documents completely different.}
\end{align}
$$

### Algorithm
- Read file
- Divide file into words and make word list
- Count frequency of words in either dictionary or list of tuples
- Compute dot product
	- for every word in D1:
		- if word in D2:
			- dotproduct += ( D1(word) * D2(word) )
	- Worst case time: order of numwords(D1) * numwords(D2)
- Micro-optimisation
	- Sort documents into word order
	- Compute inner product in time numwords(D1) * numwords(D2)

### Python Implementation
Try using the file.
`docdist1.py`: 3.7s, wordList = wordList + words_in_line, $\Theta(n^2)$
`docdist2.py`: 2.722s, wordList.extend(words_in_line) +, $\Theta(n)$
`docdist3.py`: 2.657s, sort data first
`docdist4.py`: 0.735s, Insert words in dictionary instead of list
`docdist5.py`: 0.138s, process words instead of chars
`docdist6.py`: 0.069s, mergesort instead of insertion
`docdist7.py`: 0.052s, dictionary instead of sort
`docdist8.py`: best

## Appendix - the mindset of optimising the code
### Iterative improvements
**Objective**: arrive at the most efficient implementation in terms of running time
**Approach**
	- At each iteration, analyse the running times of various parts of the code
	- Based on the biggest consumer of running time, refactor the code by
		- Introducing faster algorithms
		- Using features of the language
		- Simplifying and optimising code
Refer to pdf slides appendix for full detail.