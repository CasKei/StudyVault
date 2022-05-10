---
aliases: 
tags: 50.002
---
[[Comp Struct|50.002]]
[[Cache Design Issues]]

## What
The caching algorithm computes what the [[Cache]] must do in general when
- [[Anatomy of the Beta CPU|CPU]] sends a **read** or **write** request
- [[Cache]] is full and has to make room for new items based on the chosen [[Replacement policy]]
- Needs to write updated vlues back to [[Dynamic Random-Access Memory (DRAM)|physical memory]], based on chosen [[Write policy]].

Actual implementation is done via **hardware** for fastest possible performance.

## Read/LD request
```php
On CPU READ/LOAD request for address A:

	check for A in TAG field of cache lines with V==1

	if HIT: 
		update all helper bits necessary (e.g: if LRU used)
		return the corresponding content from cache to CPU
		
	else if MISS:
		if DM cache:
			selected cache line to replace 
			is cache line with index matching last K bits of A
		else if FA cache:
			selected cache line to replace 
			depends on replacement policy
		else if NWSA cache:
			selected cache line to replace 
			depends on replacement policy in the set with index matching last K bits of A
		
		if cache line is dirty:
			if write policy == WRITE-BACK:
				compute the content address 
				and update physical memory
			else if write policy == WRITE-BEHIND: 
				wait until update is done

		// at this point, selected cache line is safe to be overwritten 
		
		fetch A and Mem[A] from physical memory
		
		if DM cache:
			write higher T bits of A to the 
			TAG field of the selected cache line, 
			and Mem[A] as its content

		if FA cache:
			write A to TAG field of the 
			selected cache line, and Mem[A] 
			as its content

			if replacement policy == LRU:
				update LRU bit
			else if replacement policy == LRR:
				update LRR pointer

		return Mem[A] to CPU
```

## Write/ST request
```php
On CPU WRITE/STORE (new_content) request to address A:

	check for A in TAG field of cache lines with V==1
	
	if MISS:
		if DM cache:
			selected cache line to replace 
			is cache line with index matching last K bits of A
		else if FA cache:
			selected cache line to replace 
			depends on replacement policy
		else if NWSA cache:
			selected cache line to replace 
			depends on replacement policy in 
			the set with index matching last K bits of A
			
		if cache line is dirty:
			if write policy == WRITE-BEHIND:
				wait
			else if write policy == WRITE-BACK:
				compute the contents address 
				and update physical memory
		
		// at this point the cache line is safe to be overwritten
	if DM cache:
		write higher T bits of A to the 
		TAG field of the selected cache line, 
		and  new_content from CPU as its content

	if FA cache:
		write A to TAG field of the 
		selected cache line, 
		and new_content from CPU as its content

		if replacement policy == LRU:
			update LRU bit
		else if replacement policy == LRR:
			update LRR pointer
		
	if write policy == WRITE-THROUGH:
		compute the content address 
		and update physical memory
		return to CPU
	else:
		set cache line's dirty bit to 1
		return to CPU
			
```