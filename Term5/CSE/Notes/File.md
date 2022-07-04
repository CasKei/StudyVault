---
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

## File
> A **file** is a ==**named collection of related information**== that is stored on the [[Solid-State Drive (SSD)|secondary storage]].
> Acts as a **logical storage unit** in the computer, defined by the [[Operating System]].

Layman:
> A group of data bytes which are stored neatly in a known location with a unique name (**path**)

Files are mapped by the OS onto physcial devices that are non-volatile. Sometimes memory-[[Cache]]d for performance.

Volatile: cannot store data without power
- [[Dynamic Random-Access Memory (DRAM)|RAM]]: volatile
- [[Solid-State Drive (SSD)|SSD]], [[Hard Disk Drive (Disk)|HDD]], thumbdrives: non-volatile

## Types of files
| Directories                                         | Regular files                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Has structured namespace <br> e.g. `/users/Desktop` | Can represent programs or data<br> Can take any fomat: `.txt`, `.bin`, etc <br> Can contain any info defined by creator |

## File Example
File has: **attributes** and **content**.

| Attributes                                                                            | Content             |
| ------------------------------------------------------------------------------------- | ------------------- |
| Stored in inode                                                                       | Group of data bytes |
| Contain **important** metadata such as name, size, datetime of creation, user ID, etc |                     |

When we use this file, we don't care about its physical address, only the ==path==. The path is the ==logical storage unit==.

## Content structure
Varies depending on computer.

| Structure | Description                                                                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| None      | Uninterpreted sequence of bytes                                                                                                                                                      |
| Simple    | <ul><li>Lines (text files)</li><li>Fixed Length Records (structured database, e.g. NRIC)</li><li>Variable Length Records (unstructured database, e.g. audio, video, books)</li></ul> |
| Complex   | Executable files (`ELF` files)                                                                                                                                                                                     |

## Format and Type
> Format is the actual data structure of a certain file, defining the ==syntax== (permitted values, formal structure or grammar) and ==semantics== (meaning and interpretation) of data within a file.

> Type is a group of file formats that serve similar functions.
> e.g. `arc`, `tar`, `zip` are all the format of archive file type.

| Type           | Usual extension          | Function                                                                           |
| -------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| executable     | exe, com, bin or none    | ready-to-run machine-language program                                              |
| object         | obj, o                   | compiled, machine language, not linked                                             |
| source code    | c, cc, java, pas, asm, a | source code in various languages                                                   |
| batch          | bat, sh                  | commands to the command interpreter                                                |
| text           | txt, doc                 | textual data, documents                                                            |
| word processor | wp, tex, rtf, doc        | various word-processor formats                                                     |
| library        | lib, a, so, dll          | libraries of routines for programmers                                              |
| print or view  | ps, pdf, jpg             | ASCII or binary file in a format for printing or viewing                           |
| archive        | arc, zip, tar            | related files grouped into one file, sometimes compressed, for archving or storage |
| multimedia     | mpeg, mov, rm, mp3, avi  | binary file containing audio or A/V information                                    |

You can tell that different files have different formats from the ==extension==. Some OS replaces icons to give *visual representation* of the format.

### Extension vs Format
Extension is the char or group of chars after the `.` that makes up the file name.
Indicates type or format, but not always.
- Helps OS determine which program the file is associated with
- e.g. `.xls` tells computer to load this file into Excel when opened.

> Renaming the extension won't convert the format

PDF format file will not be comverted to ZIP format just by changing the extension name. You need a tool to convert.

## Interpreters
Who can read and understand file content?
- [[OS Kernel]]
	- UNIX-based OS implements ==directories== as special files
	- There is a ==difference== between directories and regular files
	- Supports ==executable== files
	- Doesn't otherwise require/interpret any formats of other regular files
- [[System programs]]
	- ==Linker== or ==Loader== that knows `ELF` formatted files
	- [[Interpreter and Compiler|Compilers]] that know certain file script formats (e.g. `.c` for `gcc`)
- [[User Programs]]
	- Browser understands [[HTML, CSS, JS intro|HTML]], web-assembly
	- Video players understands `.mp4` format
	- PDF readers understand `.pdf`

## Further
[[File Abstract Data Type]]