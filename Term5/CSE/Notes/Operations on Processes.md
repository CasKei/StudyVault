---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

## Operations on Processes
We can perform various **operations** on a process: spawning child processes, terminate the process, set up inter-process communication [[Interprocess Communication]] channels, change the process priority, and many more. All of these operations require a [[System calls]] (switching to [[Kernel mode and User mode|kernel mode]]). In this example, we use the **C API** to make the system call.

- [[Process creation]]
	- [[Process creation#Process Tree]]
	- [[Process creation#Process Id]]
	- [[Process creation#Child Process vs Parent process]]
		- [[Process creation#How fork works]]
			- [[Process creation#Example]]
			- [[Process creation#fork return value]]
			- [[Process creation#execlp]]
			- [[Process creation#wait]]
		- [[Process creation#The fork tree]]
- [[Process Termination]]
	- [[Process Termination#Orphaned processes]]
	- [[Process Termination#Zombie processes]]
		- [[Process Termination#Zombie making]]