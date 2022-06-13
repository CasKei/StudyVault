---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 4 - Processes and Thread management]]
[[Interprocess Communication]]


## Application: Chrome Browser Multi-process Architecture

Websites contain multiple **active** contents: Javascript, Flash, HTML etc to provide a rich and dynamic web browsing experience. You may **open** several tabs and **load** different websites at the same time. However, some web applications contain bugs, and may cause the entire browser to **crash** if the entire Chrome browser is just **one** single huge process.

Google Chrome’s web browser was designed to address this issue by creating separate processes to provide **isolation**:

1.  The Browser process (manages user interface of the browser (not website), disk and network I/O); only one browser process is created when Chrome is _just opened_
2.  The Renderer processes to render web pages: a new renderer process is created for each website opened in a new tab
3.  The Plug-In processes for each type of Plug-In

All processes created by Chrome have to **communicate** with one another depending on the application. The advantage of such multi process architecture is that:

-   Each website runs in **isolation** from one another: if one website crashes, only its renderer crashes and the other processes are unharmed.
-   Renderer will also be unable to access the disk and network I/O directly (runs in sandbox: limited access) thus reducing the possibility of security **exploits**.
-   Each process can be scheduled **independently**, providing **concurency** and responsiveness.