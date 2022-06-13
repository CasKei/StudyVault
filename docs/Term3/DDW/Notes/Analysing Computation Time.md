---
aliases: Computation Time, complexity, Complexity
---
Back to [[Data Driven World|DDW]]
# Computation Time
A performance of a program can be measured using ==computation time== and its ==memory space== that it occupies. here we focus on measuring computation time.
## Asymptotic Notation
A shorthand used to give a quick measure of the behaviour of a function $f(n)$ as $n$ grows large.
Here we introduce several notations that is common in analysing computer programs.
### Little O
This notation is to indicate that $f$ is *asymptotically smaller* than $g$, or
$$f(x) = o(g(x))$$
This is True if and only if
$$\lim_{x\to\infty} \frac{f(x)}{g(x)} = 0$$
### Big O
Most frequently used. Gives upper bound on the growth of a function.
$$f=O(g)$$
if and only if,
$$\lim_{x\to\infty} \text{sup}\frac{f(x)}{g(x)} < \infty$$
Where "sup" means superior or above, as it indicates upper bound.
### Big Omega
Big Oindicates upper bound, Big Omega indicates lower bound.
$$ f=\Omega(g)$$
if and only if there exists a constant $c$ and a $x_0$ such that $\forall$ $x \geq x_0$ , we have
$$f(x) \geq c|g(x)|$$
In other words, this simply means that $f(x)$ is greater than or equal to $g(x)$. As you can guess, this sounds like big O in reverse.
$$f(x) = O(g(x)), \text{if and only if } g(x) = \Omega (f(x))$$
We can use the definition of Big O to prove this by exchanging the terms $f$ and $g$. We are going to prove that $x=O(x^2)$
This is true because
$$\lim_{x \to \infty} \frac{x}{x^2} = \lim_{x \to \infty} \frac{1}{x} < \infty$$
Therefore,
$$x^2 = \Omega(x)$$
### Little Omega
This denotes that one function grows strictly faster than another function.
$f(x) = \omega (g(x))$ if and only if, $\lim_{x \to \infty} \frac{g(x)}{f(x)} = 0$
This is the reverse of little O:
$$f(x) = \omega (g(x)), \text{if and only if } g(x) = o(f(x))$$
### Theta
Sometimes we want to specify both upper and lower bound at the same time. We use this notation $$f=\Theta (g)$$ if and only if $$f = O(g) \text{ and } g= O(f)$$
### Analogies with Relation Operators
|Relational Operator| Asymptotic Notation|
|---|---|
|$f=g$|$f=\Theta (g)$|
|$f<g$|$f=o(g)$|
|$f\leq g$|$f=O(g)$|
|$f>g$|$f=\omega (g)$|
|$f \geq g$|$f=\Omega (g)$|
## Measuring Computation Time
We are interested in the trend on the computation time as the number of input changes. In analysing this, we are interested in the upper bound, so we normally use the Big O notation to indicate the upper bound of a computation time of a program.

We can investigate this by creating a list of different sizes. Then ask the algorithm to sort them. We can also comparethe performance of the algo when the input list is already sorted or randomly shuffled.
### Setup
We generate the input array of integers with different number of elements from 10 up to 10,000. We run the sorting algorithms two times, one is when the input array is randomly shuffled and the second one is when the input array is already sorted from the smallest to the largest. We present the results for different algorithms in the next sections.
### [[Bubble Sort and Insertion Sort#Bubble Sort|Bubble Sort]]
If we run version 1 of Bubble Sort algorithm on the randomly shuffled array. The output time in seconds are shown here.

```
bubbletime = [5.7220458984375e-06, 2.2649765014648438e-05, 0.0014679431915283203, 0.2126140594482422, 25.051520347595215]
```
We can plot this and see the relationship between the number of elements and the computation time. To see the relationship better in this big range of number, we plot the log of $y$ and the log of $x$
```py
import matplotlib.pyplot as plt
import numpy as np

nelements = [10, 100, 1000, 10000, 100000]
bubbletime = [5.7220458984375e-06, 2.2649765014648438e-05, 0.0014679431915283203, 0.2126140594482422, 25.051520347595215]

plt.title("Bubble Sort on Randomly Shuffled Array")
plt.xlabel("log(number of input)")
plt.ylabel("log(computation time (s))")
plt.plot(np.log(nelements), np.log(bubbletime),'o-')
```
![[Pasted image 20211223161937.png]]
We see that the computation time increases as the input increases.
Almost a straight line when we plot logarithmic.
Its a quadratic.
This means [[Bubble Sort and Insertion Sort#Analysing Computation Time Computation Time|computation time]] of Bubble Sort is quadratic:
$$ T(n) = O(n^2)$$
On the other hand, this is the computation time when the input is already sorted.

```
bubbletimeSorted = [6.4373016357421875e-06, 1.9073486328125e-06, 4.291534423828125e-06, 3.147125244140625e-05, 0.00030159950256347656]
```
Plotting this again with the same input,
```py
nelements = [10, 100, 1000, 10000, 100000]
bubbletimeSorted = [6.4373016357421875e-06, 1.9073486328125e-06, 4.291534423828125e-06, 3.147125244140625e-05, 0.00030159950256347656]

plt.title("Bubble Sort on an Already Sorted Array")
plt.xlabel("log(number of input)")
plt.ylabel("log(computation time (s))")
plt.plot(np.log(nelements), np.log(bubbletimeSorted),'o-')
```
![[Pasted image 20211223162238.png]]
Taking the slope between 8 to 11, slope approx 1.
We don't take the first few data points because it is limited by the accuracy of the floating point number in Python when the number is too small e.g. $\approx 10^{-12}$.
Notice that the computation time now falls in a straight line with a slope of about 1. This shows that when the input is already sorted, the computation time increases linearly instead of quadratically as the input increases. This means that in the best case scenario for the computation time is linear.
$$T(n) = O(n)$$
### [[Bubble Sort and Insertion Sort#Insertion Sort|Insertion Sort]]
We can do the same for insertion sort. Below is the output when the input is randomly shuffled
```
insertiontime = [6.198883056640625e-06, 7.867813110351562e-06, 0.0006382465362548828, 0.06774091720581055, 6.839613199234009]
```
We can plot this with the same input.
```py
nelements = [10, 100, 1000, 10000, 100000]
insertiontime = [6.198883056640625e-06, 7.867813110351562e-06, 0.0006382465362548828, 0.06774091720581055, 6.839613199234009]

plt.title("Insertion Sort on Randomly Shuffled Array")
plt.xlabel("log(number of input)")
plt.ylabel("log(computation time (s))")
plt.plot(np.log(nelements), np.log(insertiontime),'o-')
```
![[Pasted image 20211223162634.png]]
We can again notice that the computation time increases in this logarithmic scales with a slope of about 2. This means that the computation time is also quadratic.

For now, we can say that the [[Bubble Sort and Insertion Sort#Analysing Computation Time Computation Time|computation time]] for Insertion Sort is quadratic.
$$T(n) = O(n^2)$$
On the other hand, this is the output when the input is already sorted.

```
insertiontimeSorted = [5.7220458984375e-06, 1.430511474609375e-06, 4.0531158447265625e-06, 3.123283386230469e-05, 0.0003333091735839844]
```
If plotted,
```py
nelements = [10, 100, 1000, 10000, 100000]
insertiontimeSorted = [5.7220458984375e-06, 1.430511474609375e-06, 4.0531158447265625e-06, 3.123283386230469e-05, 0.0003333091735839844]

plt.title("Insertion Sort on an Already Sorted Array")
plt.xlabel("log(number of input)")
plt.ylabel("log(computation time (s))")
plt.plot(np.log(nelements), np.log(insertiontimeSorted),'o-')
```
![[Pasted image 20211223162925.png]]
Similarly, in this plot, looking at the x axis between 7 to 11, the slope is about 1 indicating that the computation time is linear. So the computation time when the input is already sorted is linearly increasing with the input numbers, similar to Bubble Sort. This means that in the best case scenario, the computation time for Insertion Sort is linear.
$$T(n)=O(n)$$
### [[Binary Heap and Heapsort|Heapsort]]

We can now check the computation time for heapsort algorithm. The computation time for randomly shuffled array is as shown below.

```
heapsorttime = [5.0067901611328125e-06, 7.867813110351562e-06, 9.512901306152344e-05, 0.0012400150299072266, 0.015644311904907227, 0.21677017211914062]
```

A quick look actually shows that heapsort is much faster the other two. Let's plot it.
```py
nelements = [10, 100, 1000, 10000, 100000, 1000000]
heapsorttime = [5.0067901611328125e-06, 7.867813110351562e-06, 9.512901306152344e-05, 0.0012400150299072266, 0.015644311904907227, 0.21677017211914062]

plt.title("Heapsort on Randomly Shuffled Array")
plt.xlabel("log(number of input)")
plt.ylabel("log(computation time (s))")
plt.plot(np.log(nelements), np.log(heapsorttime),'o-')
```
![[Pasted image 20211223170412.png]]
We see the slope is about $\frac{2}{4} \approx 0.5$
We found that it is not linear or quadratic.
It turns out that the computation time for Heapsort is logarithmic.
Computation time for Heapsort is $T(n) = O(n\log{n})$

### Summary
|Sorting Algorithm| Random List| Sorted List $T(n)$|
|---|---|---|
|Bubble Sort|$O(n^2)$|$O(n)$|
|Insertion Sort|$O(n^2)$|$O(n)$|
|Heapsort|$O(n\log{n})$|$O(n\log{n})$|
## Analysing Computation Time Using Model
Can we analyse what is the computation time without resolving to the experimentation?
Here we just look at the code and apply some computational time model.
To do so, we are going to indicate using asymptotic notation, particularly big O notation.
### [[Bubble Sort and Insertion Sort#Analysing Computation Time Computation Time|Bubble Sort Computation Time]]
```
Bubble Sort 
Version: 1
Input: array
Output: None, sort in place
Steps:
1. n = length of array
2. For outer_index from 1 to n-1, do:
    2.1 For inner_index from 1 to n-1, do:
        2.1.1 first_number = array[inner_index - 1]
        2.1.2 second_number = array[inner_index]
        2.1.3 if first_number > second_number, do:
            2.1.3.1 swap(first_number, second_number)
```
Computation time:
-   step 1: constant time, $O(1)$.
-   steps 2: $n-1$ times, so $O(n−1)=O(n)$
    -   step 2.1: $n-1$ times, so $O(n)$
        -   step 2.1.1 to 2.1.3, are all constant time, so it's $3 \times O(1) = O(1)$
So we can compute the computational time as follows:
$$
\begin{align}
T(n) &= O(1) + O(n) \times (O(n) \times O(1))\\
&= O(1) + O(n) \times O(n)\\
&= O(1) + O(n^2)\\
&= O(n^2)
\end{align}
$$
This agrees with the previous section that computation time is quadratic.
### [[Bubble Sort and Insertion Sort#^e3453a|Computation Time]]
```
Insertion Sort 
Version: 2
Input: array
Output: None, sort in place
Steps:
1. n = length of array
2. For outer_index in Range(from 1 to n-1), do:
    2.1 inner_index = outer_index  # start with the i-th element
    2.2 temporary = array[inner_index]
    2.3 As long as (inner_index > 0) AND (temporary < array[inner_index - 1]), do:
        2.3.1 array[inner_index] = array[inner_index - 1]) # shift to the right
        2.3.2 inner_index = inner_index - 1  # move to the left
    2.4 array[inner_index] = temporary # save temporary to its final position
```
Computation time:
-   step 1 is $O(1)$
-   step 2 is executed $n−1$, so the time is $O(n)$.
    -   steps 2.1 and 2.2 are all constant time, so it is $O(1)$.
    -   step 2.3 is executed depending on the actual values in the array. In the worst case it is $n−1$ times, and in the best case it's already ordered and executed as constant time. In average, then the computation time is $O(n/2)$ or simply $O(n)$.
        -   steps 2.3.1 and 2.3.2 are constant time, i.e. $O(1)$.
    -   step 2.4 is also constant time, i.e. $O(1)$.
$$
\begin{align}
T(n) &= O(1) + O(n) \times (2 \times O(1) + O(n) \times (O(1) + O(1)))\\
&= O(1) + O(n) \times (O(1) + O(n) + O(1))\\
&= O(1) + O(n) \times O(n)\\
&= O(1) + O(n^2)\\
&= O(n^2)
\end{align}
$$
So Insertion Sort is similar to Bubble sort in computation time.
### [[Binary Heap and Heapsort|Heapsort]]
Now, we will consider heapsort algorithm's computation time. The pseudocode can be written as follows:
```
def heapsort(array):
Input:
  - array: any arbitrary array
Output: None
Steps:
1. call build-max-heap(array)
2. heap_end_pos = length of array - 1 # index of the last element in the heap
3. As long as (heap_end_pos > 0), do:
    3.1 swap( array[0], array[heap_end_pos])
    3.2 heap_end_pos = heap_end_pos -1 # reduce heap size
    3.3 call max-heapify(array[from index 0 to heap_end_pos inclusive], 0)
```
Computation time:
-   step 1 depends on computation time for `build-max-heap()` algorithm. We'll come to this later.
-   step 2 is constant time, i.e. ==$O(1)$==
-   step 3 is done from $n−1$ , which is the last element in the array, down to $1$, which is the second element. This means that it is executed $n−1$ times, so the computation time is ==$O(n)$==.
    -   steps 3.1 and 3.2 are constant time, ==$O(1)$==.
    -   step 3.3 depends on computation time for `max-heapify()`.

To get the computation time for heapsort, we need to check what is the computation time for `build-max-heap()` and `max-heapify`. Let's start with the first one.
```
def build-max-heap(array):
Input:
  - array: arbitrary array of integers
Output: None, sort the element in place
Steps:
1. n = length of array
2. starting_index = integer(n / 2) - 1 # start from the middle or non-leaf node
3. For current_index in Range(from starting_index down to 0), do:
    3.1 call max-heapify(array, current_index)
```
Computation time:
-   step 1 and 2 are constant time, ==$O(1)$==.
-   step 3 is fixed and executed for $n/2$ times. We can say that the computation time is ==$O(n)$==.
-   step 3.1 on the other hand depends on the computation time for `max-heapify`.
```
def max-heapify(A, i):
version: 2
Input: 
  - A = array storing the heap
  - i = index of the current node to restore max-heap property
Output: None, restore the element in place
Steps:
1. current_i = i # current index starting from input i
2. swapped = True
3. As long as ( left(current_i) < length of array) AND swapped, do:
    3.1 swapped = False
    3.2 max_child_i = get the index of largest child of the node current_i
    3.3 if array[max_child_i] > array[current_i], do:
        3.3.1 swap( array[max_child_i], array[current_i])
        3.3.2 swapped = True
    3.3 current_i = max_child_i # move to the index of the largest child
```
Computation time for `max-heapify()`:
-   step 1 and 2 are constant time, ==$O(1)$==.
-   step 3, in average is executed in ==$O(log⁡(n))$== time.
    -   steps 3.1 to 3.4 are all constant time, ==$O(1)$==.
        -   steps 3.3.1 and 3.3.2 are also constant time, ==$O(1)$==.
So computation time is
$$
\begin{align}
T(n) &= O(1) + O(\log{n}) \times (O(1) \times O(1))\\
&= O(\log{n})
\end{align}
$$
#### How did we get $\log{n}$ time for step 3?
Let's represent some example of binary tree and calculate the number of levels and its nodes or elements.

|Level|Diagram (Diff level using diff symbol)|Nodes at level i| Total number of nodes|
|---|---|---|---|
|0|o|1|1|
|1|o xx|2|3|
|2|o x x oo oo|4|7|
|3|o x x oo oo xx xx xx xx|8|15|

From the table we can see that the maximum number of elements at level *i* can be calculated from the level position known as $$n_i = 2^i$$
For example, at level $i=3$, the maximum number of elements can be up to $n=2^3=8$. The total number of elements, can therefore be calculated from $$n=\sum^{i_{max}}_{i=0} 2^i$$

In geometric series $a + ar + \dots + ar^{n-1} = \dfrac{a(1-r^n)}{1-r}$.
In the above sum, $a=1$ and $r=2$, and number of terms is $i_{max}+1$. Therefore
$$ \begin{align}
n &= \frac{1-2^{i_{max}+1}}{1-2}\\
&= 2^{i_{max}+1}-1
\end{align}
$$
For example, if there are three level, $i_{max}=3$, then the maximum total number of element is $n=24−1=16−1=15$.

This also means that we can get the number of level from the number of elements in the tree.
$$ \text{level} = \lfloor \log_{2}{n} \rfloor $$
Let's go back to step 3. This step is executed by moving `curr_i` from one node to another node. The movement is always from parent to child. This means it moves in the vertical direction in the binary tree across the level. So the naximum number of moves will be $\log{n} - 1$. That's why we say the computation time is $O(\log{n})$
#### Total Computation Time for Heapsort
Heapsort: $T(n) = T_{build-max-heap} (n) + O(n) \times T_{max-heapify}(n)$
Build-max-heap: $T_{build-max-heap} (n) = O(n) \times T_{max-heapify}(n)$
Max-heapify: $T_{max-heapify}(n) = O(\log{n})$

From this we can calculate
Build-max-heap: $T_{build-max-heap} (n) = O(n) \times O(\log{n}) = O(n \log{n})$
And substitute to heapsort:
Heapsort: 
$$
\begin{align}
T(n) &= O(n \log{n}) + O(n) \times O(\log{n})\\
&= O(n \log{n}) + O(n \log{n})\\
&= O(n \log{n})
\end{align}
$$
## Big O Cheatsheet
[External link to Big O Cheatsheet](https://www.bigocheatsheet.com/)