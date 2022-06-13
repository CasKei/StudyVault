---
aliases: daemon
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]


## Daemon Processes
> A **daemon** is a background process that performs a specific function or system task. It is created in user mode.

In keeping with the UNIX and Linux philosophy of modularity, daemons are programs rather than parts of the kernel. Many daemons start at boot time and continue to run as long as the system is up. Other daemons are started when needed and run only as long as they are useful.

The daemon process is designed to run in the background, typically managing some kind of ongoing service. A daemon process might listen for an incoming request for access to a service. For example, the `httpd` daemon listens for requests to view web pages. Or a daemon might be intended to initiate activities itself over time. For example, the `crond` daemon is designed to launch cron jobs at preset times.

When we refer to a daemon process, we are referring to a process with these characteristics:

-   Generally **persistent** (though it may spawn temporary helper processes like xinetd does)
-   **No controlling terminal** (and the controlling `tty` process group (`tpgid`) is shown as -1 in `ps`)
-   **Parent** process is generally init (process 1)
-   Generally has its own process group `id` and session `id` (daemon group)