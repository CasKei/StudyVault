---
aliases:
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]
![[Cache Design Issues#^249c20]]

## Motivation
To further improve [[Cache]] preformance, we can
> increase the capacity of each cache line by fetching `B` words of data at a time.

This is especially useful if there is high [[Memory Hierarchy#Reason why this works|locality of reference]].

## Block size
Recall 1 word = 32 bits.
[[Word addressing]] - address the entire word by its smallest byte address.

> **Block size:** number of data words in each cache line.
> Always a power of 2.

> Hence we need $b = \log_2{B}$ bits to index or address each word in the cache line.

## Example
A cache line with `B=4`

![](https://dropbox.com/s/ceamhyfon0dsofw/blocksize.png?raw=1)

We need `b = 2` to address each column, taken from `A[3:2]` (assuming `A` uses byte addressing).

## Pros & Cons
| Pros                                                                                                                                                                                                                  | Cons |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| If high locality of reference present, high chance words from same block will be required together. Fetching a large block upon the first `MISS` will be beneficial later on, thus improving the average performance. | Risk of fetching *unused* words. Larger block size = fetch more words on cache `MISS`, and `MISS` penalty grows linearly with increasing block size if there is low locality of reference.     |