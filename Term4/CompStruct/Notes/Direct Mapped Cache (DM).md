---
aliases: DM cache, contention
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

[[Cache]]

## Structure
![](https://dropbox.com/s/eu74l2gi23380mp/dmcache.png?raw=1)

## Characteristics (in comparison to [[Fully Associative Cache (FA)|FA cache]])
### Cheaper
Less [[Static Random-Access Memory (SRAM)|SRAM]] used.
`TAG` field contains **only the T-upper bits** of [[Memory Addressing|address]] `A`

Also less of other hardwares: only 1 bit bitwise comparator (to compare T-bits) needed

But we need K-bits selector [[Logic Synthesis#Decoder Demux|Decoder]] to address each cache line and activate its word line.

### Not that flexible
A unique combination of K-bits of `A` is **mapped** to **exactly one** of the entries / row of DM cache.

Each cache line is addressable by the lower `K`-bits of the address.\
The lower `K`-bits of `A` decides which cache line we are looking for.
- Number of entries depends on `K`
- Can store up to $2^K$ `TAG-Content` entries.

## Content
The `Content` field contains a copy of all bits of data at `Mem[a]`

## Problems
### Contention

^8472d3

Contention ([[Intro to hashing|Collision]] problem) due to the way it maps the lower `K` address bits to each cache line.

2 or more different addresses `A1` and `A2` can be mapped to the same cache line if both have the same lower `K` bits.

Choosing to use `K`-**lower** bits for DM cache *mapping* is better than using the **upper** `T` bits due to [[Memory Hierarchy#Reason why this works|locality of reference]], but does not completely eliminate contention.

### Slower
There is no parallel searching.

At first, DM caches has to decode the K-bit address to find the correct cache line: `TAG-Content` entry

Then, perform comparison with between `TAG` and the upper T-bit address input.

## See also
[[Fully Associative Cache (FA)|FA cache]]