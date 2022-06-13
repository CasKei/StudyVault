---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 1 - Introduction to Operating System]]
[[Week 4 - Processes and Thread management]]

## Bootstrapping
Booting is the process of starting up a computer. **It is usually hardware initiated** — (by the start button that users press) — meaning that users physically initiate simple hardwired procedures to kickstart the chain of events that loads the firmware (BIOS) and eventually the entire OS to the main memory to be executed by the CPU. This process of loading basic software to help kickstart operation of a computer system after a hard reset or power on is called **bootstrapping**.

Recall that programs (including the operating system kernel) must **load** into the main memory before it can be executed. However, at the instance when the start button is pressed, there’s no program that resides in the RAM yet and therefore nothing can be executed in the CPU.

We require a software to load another software into the RAM — this results in a **paradox**.

## The Booting Paradox
To solve this paradox, the bare minimum that should be done in the hardware level upon pressing of the start button is to load a _special_ program onto the main memory from a dedicated input unit: **a **read-only-memory** (ROM) that comes with a computer when it is produced and that cannot be erased.** This special program is generally known as **firmware or BIOS**.

Firmware is not equivalent to BIOS, but unfortunately some resources and PC manufacturers might just use them interchangeably. Firmware generally refers to software stored on the motherboard (of any devices like computers, routers, switches,etc), containing basic settings of the device at startup. Some firmwares are upgradable, while some are Read-Only. BIOS is a term generally used specifically to refer to computer’s motherboard firmware in older computers. Modern computers use other Firmwares such as UEFI, also stored on chips on the motherboard. Note that UEFI / BIOS don’t form the entirety of a motherboard’s firmware.

After the firmware is loaded onto the main memory through hardwired procedures, the CPU may execute it and **initialise all aspects of the system, such as:**
1.  **Prepare** all attached devices in a state that is ready to be used by the [[Operating System|OS]]
2.  **Loads** other programs — which in turn loads more and more complex programs,
3.  **Loads** the [[OS Kernel]] from disk
4.  When the system boots, the hardware starts in the [[Kernel mode and User mode|kernel mode]]. After being loaded, the Kernel will perform the majority of system setups (driver init, memory management, interrupts, etc). Afterwards, the rest of the OS is loaded and then user processes are started in [[Kernel mode and User mode|user mode]].

![[xq4r038r.bmp]]

Note that the figure is heavily simplified for illustration purposes only.

## More on Linux Startup Process
The Linux startup process very much depends on the hardware architecture, but it can be simplified into the following steps:

1.  **Firstly**, the BIOS performs setup tasks that are specific to the hardware of the system. This is to prepare the hardware for the bootup process. After setup is done successfully, the bios loads the boot code (bootloader) from the boot device (the disk)
2.  The bootloader will **load** the default option of the operating system. If there’s more than 1 OS, then the user is presented with an option of selecting an OS to run.
3.  After an OS is selected, the bootloader **loads the kernel into memory**, and the CPU starts execution in kernel mode.
4.  The kernel will **setup** system functions that are crucial for hardware and memory paging, perform the majority of system setups pertaining to interrupts, memory management, device, and driver initialization.
5.  It then start up a bunch of [[Daemon Processes]]:
    -   The `idle` process and the `init` process for example, that runs in **user space**
6.  The `init` either consists of scripts that can be executed by the shell (sysv, bsd, runit) or configuration files that are executed by the binary components (systemd, upstart).
    -   The `init` process bascally invokes a specific set of services (daemons).
    -   These provide various **background** system services and structures and form the user [[Desktop environment]].