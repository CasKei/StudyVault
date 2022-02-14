---
tags: #50.004
---

# 50.004 Homework Set 2
## Cassie Chong 1005301 CL01
Note: In this homework set, log denotes the natural logarithm, i.e. the logarithm in base e.  
Following the notation used in the textbook, we write A[1..n] to mean an array A indexed from  1 to n. This means the first entry of A is A[1].

## Q1
### i) $T(n) = \sqrt{2}T(n/2)+\log{n}$
We have $a = \sqrt{2}$ and $b = 2$, and $f(n) = \log{n}$.
Making a comparison between $n^{\log_b{a}}$ and $f(n)$,
$n^{\log_b{a}} = n^{\log_2{\sqrt{2}}} = n^{0.5\log_2{2}} = \Theta(n^{0.5})$. 
We thus have $f(n) = \log{n} = O(n^{0.5- \epsilon})$, with $f(n)$ being asymptotically smaller than $n^{0.5}$.
$$\begin{align*}
\epsilon &> 0 &\text{, but this is only true if the exponent}\\
0.5 - \epsilon &> 0 &\text{, hence we have a condition that}\\
\epsilon &< 0.5
\end{align*}$$
So there exists $\epsilon$ where $0 < \epsilon< 0.5$ where $f(n) = O(n^{0.5- \epsilon})$.
This satisfies case 1 of the master theorem.
$$T(n) = \Theta(n^{0.5})$$
<br>
### ii) $T (n) = 2^nT (n/2) + 2^n/ \log{n}$
We have $a=2^n$ and $b=2$, and $f(n) =\dfrac{2^n}{\log{n}}$.
Master theorem cannot apply as $a$ is not a constant, hence not in the form we need in order to apply the theorem.
<br>
### iii) $T (n) = 3T (n/3) + n/2$
We have $a=3$ and $b=3$, and $f(n) = n/2$.
$n^{\log_b{a}} = n^{\log_3{3}} = \Theta(n)$.
We thus have $f(n) = \Theta(n^{\log_b{a}})$.
We can apply case 2 of the master theorem since $f(n) = \Theta(n)$ and conclude
$$T(n) = \Theta(n \log_2{n})$$
<br>
### iv) $T (n) = 3T (n/4) + n \log{n}$ 
We have $a=3$, $b=4$ and $f(n) = n \log n$.
We compare $n^{log_b{a}}$ and $f(n)$.
$n^{log_{b{a}}} = n^{log_4{3}}$ 
We have $f(n) = \Omega(n^{{\log_4{3}}+ \epsilon})$ where $0 < \epsilon< 1-\log_4{3}$.
Since there exists a constant $\epsilon> 0$ where $f(n) = \Omega(n^{{\log_4{3}}+ \epsilon})$, we can apply case 3 of the master theorem if we prove the regularity condition to be true.

Prove for sufficiently large $n$, $3f(\frac{n}{4})\leq cf(n)$, where $c<1$
$$\begin{align*}
LHS &= 3f\left(\frac{n}{4}\right)\\
&= 3 \left( \frac{n}{4}\right) \log \frac{n}{4}\\
&= \frac{3}{4}\log{}\left(\left(\frac{n}{4}\right)^n\right)\\
&= \frac{3}{4}\left[ \log n^{n} -\log 4^n\right]\\
&= \frac{3}{4}\left[ n\log n -n\log 4\right] & \leq \frac{3}{4}n\log n &\text{,  since $n\log 4 > 0$ }\\
&&\leq cf(n) &= RHS \text{, where c = $\frac{3}{4} < 1$, (for large n)}
\end{align*}$$
Hence we can conclude
$$T(n) = \Theta(n \log n)$$
<br>
### v) $T (n) = T (n/2) + n(2 − \cos{n})$
We have $a=1$, $b= 2$ and $f(n) = n(2-\cos n )$.
We compare $n^{\log_b{a}}$ and $f(n)$.
$$\begin{align*}
n^{\log_b{a}}&= n^{\log_2{1}}\\
&= 1
\end{align*}$$
$$\begin{align*}
f(n) = &n(2-\cos{n}) \\
-1\leq &\cos n \leq 1\\
n \leq &n(2-\cos{n}) \leq 3n\\
f(n) = &\Theta(n)
\end{align*}$$
Hence $f(n) - \Omega(1^{\epsilon})$, for any $\epsilon>0$
We can only apply case 3 if we prove the regularity condition to be true.
Prove $f\left(\frac{n}{2}\right)\leq cf(n)$ for some constant $c<1$ and all sufficiently large $n$.
$$
\begin{align*}
f(n/2) = \frac{n}{2}\left(2-\cos \frac{n}{2}\right) &\leq cn(2-\cos n )\\
1-\frac{\cos{(n/2)}}{2} &\leq c(2-\cos n )
\end{align*}
$$
We look at when $\cos(n/2)$ is at minimum, when LHS is $1-(-\frac{1}{2}) = \frac{3}{2}$. $n$ is a odd multiple of $2\pi$. In this case, $\cos{n} = 1$ => RHS is $c$. This implies $c\geq \frac{3}{2}$, but $c<1$.
The regularity condition failed, so the master theorem does not apply here.
<br>
## Q2
### i)
```php
function Merge(A1, A2)
//Require: A[1...n] is an array with numerical entries
//Indexing starts from 1
	MergedA = new []
	l1, l2 = A1.length, A2.length
	i, j, k = 1, 1, 1

	while i <= l1 and j <= l2 do //both arrays have items
		if A1[i] <= A2[j] then //add the smaller of the two indexes
			MergedA[k] = A1[i]
			i ++
			k ++

		else do
			MergedA[k] = A2[j]
			j ++
			k ++
			
	while i <= l1 do //A2 depleted
		MergedA[k] = A1[i]
		i ++
		k ++

	while j <= l2 do //A1 depleted
		MergedA[k] = A2[j]
		j ++
		k ++

	return MergedA


function MergeFive(A1, A2, A3, A4, A5)
	Merged1 = new []
	Merged2 = new []
	Merged3 = new []
	Merged = new []

	Merged1 = Merge(A1, A2)
	Merged2 = Merge(A3, A4)
	Merged3 = Merge(Merged1, Merged2)
	Merged = Merge(Merge3, A5)
	return Merged
```
This algorithm consists of 2 functions, `Merge(A1, A2)` and `MergeFive(A1, A2, A3, A4, A5)`.
`Merge(A1, A2)`:
	Takes in 2 arrays `A1` and `A2`. Returns a new array which has items of the 2 input arrays sorted. No loss of items even if there are repeats, as the condition in the `if` block in the first `while` block presets that if the items are similar, assign the item on `A1` to `MergedA`, so the item on `A2` still remains available to be assigned.
	As `A1` and `A2` are already sorted, choosing the smaller of the two as we traverse both arrays, and subsequently adding the smallest item to the new array will result in a sorted `MergedA`.
	This relies on 3 pointer indexes, `i`, `j` and `k` which help us to traverse `A1`, `A2` and `MergedA` respectively. The indexes are incremented as needed.
	`while` blocks ensure that index at hand does not exceed the array lengths, and if indexes are incremented over the array length, we are sure that all items in that input array has been sorted into the new array.

`MergeFive(A1, A2, A3, A4, A5)`:
	Takes in 5 arrays.
	Using the `Merge(A1, A2)` function, assign `Merged1` to reference the new sorted and merged array with the items of `A1` and `A2`.
	Repeat this for `A3` and `A4`, assigning to `Merged2`
	Join `Merged1` and `Merged2` to form `Merged3` which is another new array with all the items in input arrays `A1`, `A2`, `A3` and `A4`.
	Finally do the same for this massive `Merged3` and `A5` to have a final array we want with all items in all five input arrays in sorted order, without change in the total number of items.
<br>
### ii)
Running `MergeFive(A1, A2, A3, A4, A5)`,
	 In worst case scenario, we spend the most time looping through the first `while` block, which makes 2 comparisons for the while loop check, and 1 more comparison for the `if` block check.
	 Worst case is when items **alternate** being placed in the new array from the two, fully completing **3 comparisons for each item for as long as the minimum of the two array lengths**.
	 The **remainder** items after such alternation, after one of the arrays have been fully iterated through, will result in **1 comparison per item**, constituted of the two remaining `while` blocks.
`Merged1`: 20, 24. => $20\times 3 + 20\times 3 + 4 = 124$
`Merged2`: 30, 35. => $30\times 3 + 30\times 3 + 5 = 185$
`Merged3`: 44, 65. => $44\times 2\times 3 + 21 =285$
`Merged`: 109, 50. => $50\times 2\times 3 + 59$
***Total comparisons***: $124 + 185 + 285 + 59 = 653$.
<br>
## Q3
### i)
With insertion sort, sorting a list with length $k$ takes a worst case time complexity of $T(n) = \Theta(k^2)$.
We have a total of $\frac{n}{k}$ such lists to sort with insertion, hence a total of $T(n) = \Theta\left(\frac{n}{k}\times k^{2}\right)= \Theta(nk)$.
<br>
### ii)
To merge $\frac{n}{4}$ subarrays each of length $k$, take 2 subarrays and merge them, and continue for the other $\frac{n}{4}- 1$ subarrays.
In total even for worst case this is done $\log_2 \frac{n}{k}$times.
Each time we merge, we take a time of $O(n1 + n2)$, for length of subarrays $n1$ and $n2$, for a total of $n$ items.
Thus the worst time is $T(n) = O(nlog{\frac{n}{k}})$.
<br>
### iii)
$$T(n) = \Theta\left(nk + n\log{\frac{n}{k}} \right)$$
In order to have $\Theta\left(nk + n\log{\frac{n}{k}} \right) = \Theta(n\log{n})$,
$$\begin{align*}
LHS&=\Theta\left(nk + n\log{\frac{n}{k}} \right)\\
&=\Theta\left(nk + n\log{n} - n\log{k} \right)
\end{align*}$$
For $nk + n\log{n} - n\log{k}$ to be of complexity $\Theta(n\log{n})$, the most significant term must be of order $n\log{n}$.
Turn the most significant term $nk$ into $n\log{n}$ by letting $k=\log n$.
Now,
$$\begin{align*}
&\Theta\left(n\log{n} + n\log{n} - n\log{(\log{n})} \right)\\
&= \Theta(n\log n)=RHS
\end{align*}$$
$\therefore k=\Theta(\log n)$. 
<br>
## Q4
 ### i)
 We can derive this from the information given:
>If $AB$ results in hint `CC`, and $BC$ results in hint `CC`, then if $AC$ results in `CC`, then $ABC$ are either all Cash or all Empty.

If there are only 2 boxes, $n=2$, we can never tell whether any box is in any state. This is the trivial case. If the hint is `CC`, we cannot conclude that both boxes have cash as they might be both empty. If the hint is `CE` or `EC`, we cannot conclude anything about which box has cash or if they both are empty. If the hint is `EE`, none of that can tell us which box has cash either.
Hence we look at when $n \geq 4$.

When $n=4$,
We can use combinations and brute-force to split the boxes into 2 sets which gives `CC` as its result. Have a set $S_1 = \set{}$ , from the original set of boxes $S =\set{A, B, C, D}$.
If 3 boxes, $ABC$ satisfy the above, put them in the set. $S_{1}= \set{A,B,C}$ We have these 3 boxes in the same state. We can use these 3 boxes to test the remaining boxes in the original set. This arises 2 cases:
1. $ABC$ all have cash.
	If this is true, checking $D$ with any box in $S_1$ will verify if it has cash.
	If `CC` given for $AD$ and $BD$ and $CD$, then $D$ is sure to also have cash.
2. $ABC$ are all empty.
	If this is true, checking $D$ with any box in $S_1$ will not be conclusive. It may also yield a `CC` even if they all might be empty.

There is also a situation where we cannot find 3 boxes that give the state `CC` for all combinations of the 3 boxes. In this case, we have half the boxes having cash and the other half being empty. We then have the following situation:
1. $AB$ has cash while $CD$ is empty. Combinations $AB$ and $CD$ might both yield `CC` result especially if the host is toying with you. Then there is no way that you can tell which pair both has cash, or that they all do not in the first place and the host is turning you into a pathetic joke.

We can expand this argument to $n\geq 4$ for larger number of even number of boxes.
So we see that if the host is an evil bastard we might get hints that are the same for possible cases when at least half of the boxes are empty, and when more than half are true, which makes it impossible for us to determine which is true. We require information that tells us whether the situation we have is in which case, that is, if we have more than half of the boxes having cash or not. If not, it really is inconclusive and you should run away from this evil host.
<br>
### ii)
Using the following rule:
> If $AB$ results in hint `CC`, and $BC$ results in hint `CC`, then if $AC$ results in `CC`, then $ABC$ are either all Cash or all Empty.

We avoid brute-forcing all combinations this time and make use of the possibility to set aside boxes into sets. This way we dont have to get all possible pair combinations, but splitting them into half for each recurrence is enough. Have a set $S_{1}= \set{}$ hold the items that obtain `CC` as the result. Since we know that more than half of the boxes hold cash, even if the host tries to be evil, if $S_1$ ends up containing less than half of the total number of boxes, we know that $S_1$ then contains empty boxes. This is the check to verify what we have in $S_1$ is what we want.

As for the algorithm, do the following.
- Have boxes test against its adjacent. We have a total of $\frac{n}{2}$ tests. 
- Retain only the pairs that yield a `CC` hint as only the `CC` hint can help us get any miserable form of a conclusion. Put them in 
	- This means that the rest either are empty pairs or pairs with only one with cash.
	- Since we know more than half has cash, what we retain will definitely have more cash than empty boxes.
	- Of what is retained, test by pairs the same way again, and repeat the similar process.
		- At the end, there should result in at least one box which pair consistently gives `CC` when tested against each other. We can put these in $S_1$ and conclude they have cash.
- Now that we definitely have sure cases of at least a box that has cash in $S_1$, we test the remaining boxes. If a remaining box yield `CC` with a box in $S_1$, put that box in into $S_1$ as well and conclude it also has cash. This will be done for all the remaining boxes.

Looking at the nature of the procedure above, it is recursive as we are discarding at most half the number of boxes in each recursion. There will be at most $n/2$ divisions.
This can be expressed in a recurrence, ignoring flooring and ceiling conditions, as $$T(n) = T\left(\frac{n}{2}\right) + \frac{n}{2}$$
We have $a=1$$, $ $b=2$, $f(n) = \frac{n}{2}$.
Compare $f(n)$ and $n^{log_b{a}}$.
$n^{\log_b{a}}=n^{\log_2{1}} = n^0 = 1$
We have $f(n) = \Omega(n^{\log_b{a}}) = \Omega(1)$. This is case 3 of the master theorem if we prove the regularity condition.
$$
af(n/b) = f(n/2) = \frac{n}{4} = \frac{1}{2} \cdot \frac{n}{2} = \frac{1}{2}f(n) = cf(n) \text{, where $c=\frac{1}{2}<1$}
$$
Hence we can conclude $T(n) = \Theta(n/2)$.
Subsequently we have to include the last procedure of using the confirmed cash box to check all the rest. Assuming we have the worst case where we only have one affirmed cash box, we have to make $O(n-1)$ more comparisons.
Hence overall we have
$$T(n) = \Theta(n/2 + n-1) = \Theta(n)$$
<br>
## Q5
Examining the pseudocode in `JOHNSORT(A)`, we see that the purpose of lines 1, 5, 6, 7 are to swap the elements of `A[j]` and `A[j - 1]`. The `if` statements express the condition for the swap.
Lines `2` and `3` are what we wish to look at.
Line `2`: outer iteration of `i` from `n` to `1`.
Line `3`: inner iteration per `i`=[`n`,`1`], from `n` to `i+1`.
This creates a situation whereby when outer iteration index `i` is `n`, the inner iteration will have `j` try to iterate through from `j` being `n` to `n+1`, which will fail the condition check of the `for` loop and exit the loop prematurely. This will fail if the array is still unsorted when this exit happens.

Example input array: `A = [5, 7, 4, 6]`. Result: `A = [5, 7, 6, 4]`.

```php
function ModdedJohnSort(A)
//Require: A[1...n] is an array with numerical entries
	temp <- 0
	for i from n down to 1 do
		for j from n down to 1 do
			if A[j] > A[j - 1] then
				temp <- A[j]
				A[j] <- A[j - 1]
				A[j - 1] <- temp
	return A.
```
The modified JohnSort has outer and inner iterations going through from `n` to `1`. This ensures that the code **does not exit prematurely** due to failing the loop check when the array may not have been sorted yet.
Now that the code loops for as long as it can possibly go, it is sure to work.