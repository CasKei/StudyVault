---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]

> As a process executes, it changes its **scheduling state** which reflects the **current** activity of the process.

[[Process Manager|scheduler]] manages these. [[Process scheduling]]

In general these states are:
1.  **New**: The process is being created. [[Process creation]]
2.  **Running**: Instructions are being executed (this process is in the CPU) Only 1 program at a time. [[Process Control|process load]]
3.  **Waiting**: The process is waiting for some event to occur (such as an I/O completion or reception of a signal). 
4.  **Ready**: The process is waiting to be assigned to a processor[[Process Control|process execute]] 
5.  **Terminated**: The process has finished execution. [[Process Termination]] [[Process Control|process abort]]

## Scheduling state transition diagram of a typical process
![[sk6ydc1a.bmp]]

