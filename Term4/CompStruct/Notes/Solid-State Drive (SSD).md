---
aliases: SSD, flash, secondary storage, NAND flash, flash memory
tags: 50.002
---
[[Comp Struct|50.002]]
[[Memory Hierarchy]]

## What
> A non-volatile memory that we can use as storage with **faster** read/write operation in general

More expensive than [[Hard Disk Drive (Disk)|HDD]] of the same saize.

SSDs use a type of memory chip called _NAND flash memory._

NAND devices: store a small amount of electrical charge on a floating gate when the cell is programmed. \
Its cell has very high resistance, and its capacitance can hold a charge for a long period of time.

## Welp
Unlike [[Anatomy of the Beta CPU|RAM]], we cannot change one cell value quickly at a time in SSD.

Charge stored in NAND flash can still fade over time if we never power it back anymore.

Therefore it is important to power up the flash storage from time to time to retain its data.

## Reading and Writing
To change its values, we nede to reset and rewrite an entire large block at once, which is a much **slower** process for a write as compared to a RAM.

## More
Although not needed for our course syllabus, if you’re curious you can read more about how HDD and SSD work [here](https://dropbox.com/s/tlaek0wyljpr74s/Hard%20Drives%3A%20How%20Do%20They%20Work%3F%20%E2%80%93%20Techbytes.pdf?dl=1) to understand how each of the work and the pros and cons of each device.