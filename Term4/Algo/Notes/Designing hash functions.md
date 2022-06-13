---
aliases: simple uniform hashing
tags: #50.004
---
[[Algo]]
[[Algo week 5]]

## What is a good hash function?
Suppose `A` is a hash table with `n` elements and `m` slots.
- ==Worst==: all key values are **hashed to same slot**
	- may have to search at most up to `n` elements
- ==Bad==: **many empty** slots, few slots with many elements
- ==Good==: **Most slots filled**, not many elements in each slot
- ==Best==: Key values are **equally distributed** over all slots
	- only need to search up to $\approx n/m$ elements

## Simple Uniform Hashing
> Assumption:
> Any given key value is equally likely to be hashed to any of the slots, independent of where the other key values are hashed to.

> Intuition:
> The design of a good hash function should be as close as possible in satisfying this simple uniform hashing assumption.

> For any hash function satisfying this assumption, the key values would be on average distributed equally over all slots (best case scenario)

Suppose $K=[0, 1]$ is the unit interval representing all possible key values.
Let `A` be a [[Hash Table]] with $m$ slots, and consider the [[Algo Hash functions|hash function]] $h:K\to \set{0,1,\dots ,m-1}$ given by 
$$h(x) = \lfloor mx \rfloor$$
If the key values are uniformly distibuted, i.e. every value in $K$ is equally likely to be a key value, then the simple uniform hashing assumption is satisfied.

Example: If 𝑚 = 10, then the hash function maps each 𝑥 to the first digit of 𝑥 after the decimal point. 
e.g.$ℎ( 0.0291) = 0$; $ℎ (0.42461) = 4$; $ℎ (0.987654) = 9$; $ℎ (0.333) = 3$.

## Hashing with non-numerical key values
### ASCII
> American Standard Code for Information Interchange

128 characters [[Basics of Information|encoded]] in 7-bit integers.

Each character in a string can be converted into its ASCII number, so a string can be interpreted as a base-128 number

e.g. ‘ABC’ interpreted as $65 ⋅ 128^2 + 66 ⋅ 128^1 + 67 = 1073475$, can be given the hash value 734 (3rd to 5th digits from the right).

### Unicode
> Vast extension of ASCII

Has characters from almost all written languages (inc. all characters in Arabic, Chinese, Greek, Hebrew, Japanese, Korean, Tamil, etc.)

Similarly, each character can be converted into its Unicode number.

## Designing [[Algo Hash functions]]
> Designing good hash functions requires knowing at least some information about the possible key values

It is not always easy to achieve the [[#Simple Uniform Hashing]] assumption.
- Distribution of key values of objects to be inerted is usually unknown
- Key values of objects could have certain correlations that result in many of them being hashed to the same slot
	- e.g. strings that are not arbitrary and could follow certain language patterns
	- e.g. key values representing student IDs usually have same first few digits

## Things to ponder
### Distribution of hash values
Did we achieve, or are we close to achieving, the [[#Simple Uniform Hashing]] assumption? Are the hash values "well distributed"?

### Data privacy issues
Even if we know someone's hash value, can we retrieve the person's pw/id? 
### Tampering detection / integrity of data
Thought experiment:
Suppose we use a hash function to hash the actual content of an entire large file.
If the file has been tampered with, then there is a good chance that the hash value would change.
Hence, keeping track of the hash value is a good way to detect tampering, without having to know the content of the file.

## Comments on [[Algo Hash functions#Division Method|division]] and [[Algo Hash functions#Multiplication Method|multiplication method]]
### Division
Recall `m` is the number of slots in the [[Hash Table]]
- Avoid letting `m` be a power of 2 unless you know what you are doing (e.g you know the distribution of the key values)
	- Data is usually stored in chunks where the number of bits in each chunk is a power of 2
	- If $m=2^p$, then the hash values depend only on the last `p` bits of the key values, which is typically not uniformly distributed.
- Values close to powers of 2 may yield surprising effects
	- e.g. If 𝐾 = {8-character password ASCII strings as base-128 integers}, and if $𝑚 = 2^7 − 1 = 127$, then all permutations of the password string would be hashed to the same slot. (Why?)

### Multiplication
Recall `m` is the number of slots in the [[Hash Table]]
- The value of `m` is not critical. Powers of 2 can be used for `m`
	- Instead the choice of $\beta$ is more important
- In course textbook, the value $\beta$ is restricted to $0<\beta<1$
- However this still makes sense even if $\beta > 1$ or $\beta < 0$.
- For this course we shall allow $\beta$ to be any strictly positive value.
- A suggested 'good default' value for $\beta$ is $\dfrac{\sqrt{5} - 1}{2} \approx 0.618034$
- This method is slower than  [[Algo Hash functions#Division Method|division]] method.