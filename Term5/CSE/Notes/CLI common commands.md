---
aliases: cmd
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

## alias
An `alias` lets you create a **shortcut** name for a command, file name, or any shell text. By using aliases, you save a lot of time when doing tasks you do frequently. You can see current aliases using the `alias` command:
![](https://natalieagus.github.io/50005/assets/images/lab1/7.png)
Or **create** an alias:
-   `alias name=’command’`
-   Example: `alias gst=’git status’`

![](https://natalieagus.github.io/50005/assets/images/lab1/8.png)
`alias` is particularly useful when you define them in your shell’s setup script.

## General system usage and statistics
Note that each of the commands below accept **OPTIONS**. Read their manuals for more information using the `man` command.

### man
`man <command>`
Shows **documentation** of the `<command>` (press q to exit the window after you’re done reading).

### ls
`ls <options>`
Shows the **list of files** in the current directory.

### ps
`ps <options>`
Shows the **list of processes** in the system.

### sudo
`sudo <command>`
`sudo apt install <packagename>`

`sudo` **Executes** the command with **administrative** privileges.

`apt` is a **package manager**, it installs packages for **Debian-based Linux distributions**.
We can use it to install anything, eg install `node` and `npm`. Using package manager is recommended since you can simply `update` or `remove` (uninstall) it too (`sudo apt remove <packagename>`, etc).

-   `sudo apt update`
-   `sudo apt install nodejs npm`

For mac users, you can use [brew](https://brew.sh) as your package manager instead.

### chmod +x
`chmod +x <path/to/filename>`

Make a file **executable**. However, firstly, you need to declare in your script **which [[Interpreter and Compiler|interpreter]] to use.**

-   You state the path to this interpreter as the **first line** in your file
-   This is called a **shebang**.
    -   In Unix-like [[Operating System]]s, the shebang line provides the **path** to an executable program (e.g. `bash`, `python`) that can interpret the following lines as executable instructions, allowing the user to **run the text file as an executable program** by typing the name of the file directly in the shell **provided the execute permission bit is set**.
-   For instance, if this file is a [[shell]] script, it should be `#!/bin/sh` or `#!/bin/bash`. If it is a python script, the interpreter should be something like `#!/usr/bin/env python`

### df
`df <options>...`
Shows the **available disk space** in each partition.

### top
`top`
**Monitors** processes and system resource usage on Linux.

### ifconfig
`ifconfig <options>`
Displays **information** about all network interfaces currently in operation.

### kill
`kill -9 <pid>`
`pkill <process_name>`
**Kills** (ends) the process matching the given pid, the same thing happens when you click the close (x) button on the window of a running app.

### ping
`ping <servername> <options>`
**Checks connection** to a server. For example, `ping google.com` tells you whether your connection is active or not.

## File creation and manipulation
Note that each of the commands below accept **OPTIONS**. Read their manuals for more information using the man command.

### mkdir
`mkdir <dirname>`
Creates a directory (folder).

### rmdir
`rmdir <dirname>`
`rm -r <dirname>`
Deletes an **empty** directory, and the latter removes a directory that contains files. 
**Be careful!** Deleting things from the command line doesn’t allow you to retrieve it back. **Unlike deleting from the GUI, it won’t be found in the trash**.

### touch
`touch <newfilename.format>`
**Creates** a new file with whatever name and format you want.

### mv
`mv <source> <destination>`
**Moves** a file from the source path to destination path. Commonly used to **rename** files.

### cp
`cp <source> <destination>`
**Copies** a file from a location to another.

### locate
`locate <filename>`
**Locate** a particular filename in your file system, if you have set it up in the first place. Will return a path to that `<filename>`.

### cat
`cat <path/to/filename>`
**Displays** the **contents** of a file, and

### wc
`wc <path/to/filename>`
**Prints** a **count** of newlines, words, and bytes for each input file.

## Command-Line Text Editor
[[nano, vim]]

## Standard Streams
[[Standard stream]]

## Output management

### pipe
Pipe is a command in Linux that lets you use **two** or **more** commands such that **output** of one command serves as **input** to the next.

It may sound similar to [[Standard stream|stream redirection]], but the general rule of thumb is that if you’re connecting the output of a command to the input of another command, use a pipe, denoted as `|` symbol. If you are outputting to or from a file use the redirect.

1.  Suppose we want to pass the want to pass the output of `cat` command as the input of `sort` command. We can’t do this with redirection: ![](https://natalieagus.github.io/50005/assets/images/lab1/15.png)
    
2.  However, using **pipe** works. It serves as a way to allow **interprocess** communication (Week 3 materials): ![](https://natalieagus.github.io/50005/assets/images/lab1/16.png)

### curl
`curl`
The curl command allows us to transfer data (download, upload) online. For instance, we can download the GNU general public license text file using the command:

```
curl -o GPL-3 https://www.gnu.org/licenses/gpl-3.0.txt
```

-   The `-o` option: Write output to `<filename>` instead of `stdout`

### grep or awk
Output **filtering**. The [`grep` or `awk`](https://techviewleo.com/awk-vs-grep-vs-sed-commands-in-linux/) command will scan the document for the desired information and present the result in a format you want. The command `grep` also accepts [regex](https://regexr.com) to search for more complex patterns.

A filter takes input from one command, does some processing, and gives output.

Suppose we have a long document, that GNU license we downloaded from the task above.

1.  To download the license, type the command: `curl -o GPL-3 https://www.gnu.org/licenses/gpl-3.0.txt`
2.  Now search for a string inside a file using the commands:
    -   `grep "<string>” <path/to/file>`
    -   For example: `grep “GNU” GPL-3` prints every line containing “GNU” word. ![](https://natalieagus.github.io/50005/assets/images/lab1/17.png)

Here are the common grep options to try:

-   `-i`: both lower and upper case
-   `-v`: search everything that does not contain the `<string>`
-   `-n`: prints the line number too

The `<string>` argument of the grep command can accept **regex** too, for instance:

-   `grep "^[A-Z]" GPL-3 -n`
-   This search for every line starting with **capital** letters ![](https://natalieagus.github.io/50005/assets/images/lab1/18.png)

You can also **pipe** the output of a command to the `grep` command so that you can filter it out. For example, `ps -ax` will report all running processes in your system (by all users, including your own). If we want to filter some processes by name, we can use grep and pipe to filter the Telegram process: `ps -ax | grep -i Telegram`

![](https://natalieagus.github.io/50005/assets/images/lab1/19.png)