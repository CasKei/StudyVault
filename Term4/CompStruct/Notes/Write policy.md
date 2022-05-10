---
aliases:
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]
![[Cache Design Issues#^842e09]]

## Motivation
When [[Anatomy of the Beta CPU|CPU]] executes a `ST` instruction, it will first\
**write** `TAG = Address`-`Content = new content` to the [[Cache]].

Then we have to decide *when* to actually update the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

	Note: sometimes we do not need to update physical memory at each `ST`, as what was stored might only be intermediary or temporary values.
	This is where the act of "writing to cache first" instead of directly to physical memory speeds up execution.

To update [[Dynamic Random-Access Memory (DRAM)|physical memory]], [[Anatomy of the Beta CPU|CPU]] must first fetch data from [[Cache]], and then write it to [[Dynamic Random-Access Memory (DRAM)|physical memory]].\
This **pauses** execution of the ongoing program as the [[Anatomy of the Beta CPU|CPU]] will be busy.

There are 3 common write strategies.

## Write-Through
> [[Anatomy of the Beta CPU|CPU]] writes are done in the [[Cache]] first, by setting
> `TAG = Address` and `Content = new content`
> in an available cache line, and is also
> **immediately written to** [[Dynamic Random-Access Memory (DRAM)|physical memory]].

Stalls [[Anatomy of the Beta CPU|CPU]] until write to memory is complete, but memory always holds most updated value.

## Write-back
> [[Anatomy of the Beta CPU|CPU]] writes are done in the [[Cache]] first, by setting
> `TAG = Address` and `Content = new content`
> in an available cache line, 
> **but is not immediately written to memory.**

Contents in [[Dynamic Random-Access Memory (DRAM)|physical memory]] can be "stale" / outdated.

To support this policy, the [[Cache]] must have a [[Helper Bits|helper bit]] called the **dirty bit** to indicate whether the corresponding copy of the content in the [[Dynamic Random-Access Memory (DRAM)|main memory]] is outdated.
The [[Anatomy of the Beta CPU|CPU]] will *write* only if the data in cache line *needs to be replaced* **and** *cache line is dirty*. If data not dirty, then cache line can simply be replaced without any writes.

## Write-behind
> [[Anatomy of the Beta CPU|CPU]] writes are done in the [[Cache]] first, by setting
> `TAG = Address` and `Content = new content`
> in an available cache line,
> **and write to [[Dynamic Random-Access Memory (DRAM)|physical memory]] is immediate, but buffered or pipelined.**

[[Anatomy of the Beta CPU|CPU]] will not stall and will executed next instructions while *writes are **completed in the background***.

Also needs [[Helper Bits|helper bit]] **dirty bit** indicator that will be cleared once the background write finishes.

Might require slightly complex hardware, e.g. pipeline and background, asynchronous write system.