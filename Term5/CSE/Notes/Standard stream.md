---
aliases: standard input, standard output, stdin, stdout, stderr, stream redirection, stream redirect
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

## What
Standard streams are **input** **and** output communication channels between a **running process** and its **environment** when it begins execution. They are **streams** of data that travel from where a program was **executed**, to the places where the program is **processed** and then back again to where the program was **executed**.

The three input/output (I/O) connections are called standard input (stdin), standard output (stdout) and standard error (stderr).

Streams are usually connected to the **terminal** in which they are executed. By default, `stdin` is connected to your **keyboard**, and `stdout + stderr` are directed to your **terminal**. You might be wondering how your keyboard and display then is shared among so many processes? The details require Streams in Linux are treated as though they were files (**Week 6 Material**). E.g: you can **read** text from a file, and you can **write** text into a file. **Both of these actions involve streams of data**.

When you run a python script, e.g: `python3 playground.py`,
![](https://natalieagus.github.io/50005/assets/images/lab1/10.png)
-   **Input** from your keyboard is passed from the terminal into the python process, and
-   **Output** from your python process is passed back to your terminal **display**. Here’s a simplified illustration:

![[5e5sxlor.bmp]]

Where are these “files” for stdin, stdout, and stderr respectively?

Well, they’re **created** by your [[Operating System]]. You can witness this pretty easily if you run a python script on one terminal (and let it hang there, don’t let it terminate yet! Shown on the right side), find out its process id and then see its details on another terminal (shown on the left) using the `lsof` command.

![](https://natalieagus.github.io/50005/assets/images/lab1/12.png)
You can see in the last three lines that stdin (0u), stdout (1u), and stderr (2u) all point to the file `/dev/ttys004`. **This is the file that is created by the OS and watched by our terminal**.

## Standard output
A standard output is a **default** _place_ (it’s just a file actually) for output to go, also known as `stdout`. Your shell is constantly **watching** that output file, and whenever there’s something there, it will automatically print to your screen. For instance, `echo "hello"` is a command that means ”output the string hello to standard output”.

-   The process echo prints to `stdout` (probably `/dev/ttyx`),
-   …and your terminal in turn shows it in its GUI display.

## Standard input
The standard input (`stdin`) is a default place where processes listen for information. For example, all the commands above with no other arguments listen for input on `stdin`. Try typing `cat` on the command line and press enter:
-   Notice you can type any character from your keyboard, because it watches for input on `stdin`,
-   Then, output what you type to `stdout` (and your shell is watching that output place so it is being printed on your screen), until you type an EOF (end of line) character: `CTRL + d`.

## Standard error
The standard error (`stderr`) is the place where error messages go. Try this command that will prompt an error such as: `cat <inexistent_path/to/filename>`.

What is the output that you see? Similar to stdout, stderr is printed directly to your screen by your shell. ![](https://natalieagus.github.io/50005/assets/images/lab1/13.png)

## Stream redirection
`stdin`, `stdout`, and `stderr` for every process is symbolized with [file descriptor](https://en.wikipedia.org/wiki/File_descriptor) `0`, `1`, and `2` respectively. Each file associated with a process is allocated a unique number to identify it, this number is called the **file descriptor**.

We can **redirect** stdin using the `<` operator, stdout using the `>` operator, and stderr using the `2>` operator.
-   If we do `<command> > <filename>`, it means we are **redirecting** the `stdout` of `<command>` to the file `<filename>`. That means, we will write whatever that was printed out by the process `<command>` to the file with `<filename>`.
-   If we do `<command> < <filename>`, it means that we are **redirecting** the `stdin` of `<command>`, e.g: use the **content** of filename as an **input** to command. This is particularly useful for commands that only take in input streams, and are unable to read the content of a file given a filename.

Note that `stdout` redirection will **truncate** (erase) the original content of the `<filename>`. If you want to append to the **existing** content of file instead, you can use the `>>` operator.

One example of a program that benefits from stream redirection is `tr`. It is a command line utility for **translating** or **deleting** characters. Do the following:
1.  Create a text file with the following content: ”Hello, have a good day today!”, name it `test.txt` and **save** it to your current directory.
2.  Then, type the following in the command line (don’t forget to navigate to your current directory first using `cd`!): `tr "[a-z]" "[A-Z]" test.txt`
3.  You will see such usage suggestion instead:
    
    ```
    usage: 	tr [-Ccsu] string1 string2 
         tr [-Ccu] -d string1
         tr [-Ccu] -s string1
         tr [-Ccu] -ds string1 string2 
    ```
    
    This is because tr **CANNOT** get input directly from a file. It only reads from `stdin`.
    
4.  Now try `tr "[a-z]" "[A-Z]" < test.txt`. Your console should print ”HELLO, HAVE A GOOD DAY TODAY!”, capitalizing the content of the `test.txt` file (but not changing its content).
5.  So based on your observation, can you deduce what is the difference between these two commands:
    1.  `tr "[a-z]" "[A-Z]" < test.txt`
    2.  `tr "[a-z]" "[A-Z]" test.txt`
6.  Now what if we want to store the capitalized content to another file? Try: tr “[a-z]” “[A-Z]” < test.txt > new_test.txt. You should find that “HELLO, HAVE A GOOD DAY TODAY!” exists within `new_test.txt`, since we **redirect** `stdout` to create this new file.
7.  What if we want to write back to `test.txt`? What can you deduce from the output?