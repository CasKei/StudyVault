---
aliases: raw polling
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Interrupt-Driven IO Operations]]
[[Hardware Interrupt]]

It takes time to perform a [[Context switch]] to handle interrupt requests. In some specifically dedicated servers, raw polling may be faster. The CPU **periodically** checks each device for requests. If there’s no request, then it will return to resume the user programs. 

Obviously, this method is **not suitable** in the case of sporadic I/O usage, or in general-purpose CPUs since at least a fixed bulk of the CPU load will always be dedicated to perform routine polling. For instance, there’s no need to poll for anything periodically when a user is watching a video.

Modern computer systems are **interrupt-driven**, meaning that it **does not wait** until the input from the requested external device is ready. This way, the computer may **efficiently** fetch I/O data **only when the devices are `ready`,** and will not waste CPU cycles to “poll” whether there are any I/O requests or not.