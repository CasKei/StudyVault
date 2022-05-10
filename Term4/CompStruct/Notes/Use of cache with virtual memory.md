---
tags: 50.002
---
[[Comp Struct|50.002]]
[[Virtual Memory]]

Recall a [[Cache]] is used to store copies of [[Memory Addressing|memory address]] and its content so that access to the [[Dynamic Random-Access Memory (DRAM)|physical memory]] can be reduced on average.

## Cache BEFORE or AFTER MMU
![](https://dropbox.com/s/j7l3t20a9cmt2ez/cacheMMU.png?raw=1)

## Observations
### For Case 1
If [[Cache]] before [[Pagetable|MMU]], then cache stores [[Virtual Address|VA]] instead of [[Memory Addressing|PA]] in `TAG` field.

### If cache line selection is based on [[Memory paging|PO]]
[[Memory paging|PO]]: page offset: unmapped, identical on both [[Virtual Address|VA]] and [[Memory Addressing|PA]]:
**2 computations can happen in parallel:**
1. VPN to [[Memory paging|PPN]] translation
2. Finding the correct cache line in [[Direct Mapped Cache (DM)|DM cache]] / [[Associativity|NWSA]] cache.

Therefore we can arrange the components as such:
![](https://dropbox.com/s/mdgucv6qubun01l/cachemmu2.png?raw=1)

Each cache line in the [[Associativity|NWSA]]/[[Direct Mapped Cache (DM)|DM cache]] used in the design above stores a **single word** (not pages) in the `Content` field and its [[Memory Addressing|PA]] in the `TAG` field.

The index of the tag in the cache is set to be the [[Memory paging|PO]] of the [[Virtual Address|VA]] due to [[Memory Hierarchy|locality of reference]]. If higher order bit is used to index the cache lines then there will be [[Direct Mapped Cache (DM)|contention]].

### If page is resident but there is a cache MISS
Then [[Cache]] must be **updated** by fetching the data from the [[Dynamic Random-Access Memory (DRAM)|physical memory]].

### If page is not resident
Then page must be fetched from the swap space and copied over to the [[Dynamic Random-Access Memory (DRAM)|physical memory]]. 

Then we update the cache.


> Ask yourself these questions to enhance your understanding.
> 
> -   What happens if the page is `Not Resident` and if Physical Memory is full? Assume LRU policy is used.
>     
> -   Which part of the TLB that we need to update on each memory reference request? What about the cache? Why?
>     
> -   What should be done if TLB `MISS` happens?
>     
> -   _Is it possible_ for cache `HIT` to occur but the requested page is **not resident**? Why or why not?
>