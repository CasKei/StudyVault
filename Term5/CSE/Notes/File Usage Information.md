---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]

Not good to pass file name to every file system operation (`read()`, `open()`, `write()`, etc)
- Name can be long and variable length
- Mapping of name to internal data structures takes time

A program **translates** name into file descriptor (file 'handle') at the beginning of a usage session.

`fd` is integer **index** into a per-process [[File Descriptor Table]]. Its numerical index has meaning only in the [[Complete Process Context|context]] of its process.
```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
int main() {
     int fd_a, fd_b, n;
     char str[100];
     /* 1. open a file in read mode */
     fd_a = open("input.txt", O_RDONLY, 0);
     /* create an output file with read write permissions, 0666 is the file permission created, the 0 in front means OCTAL notation --- 666 is the octal notation 

        if you want to create a directory, the same permission logic can be made also, but directories ARE EXECUTABLES:
            if (mkdir("myFolder", 0777) == -1)
                cerr << "Error :  " << strerror(errno) << endl;
          
            else
                cout << "Directory created!";
    */

    /* then, open a  file in RW mode */
     fd_b = open("output.txt", O_CREAT | O_RDWR, 0666);
     /* 2. read the data from input file and write it to output file */
     while ((n = read(fd_a, str, 10)) > 0) {
             write(fd_b, str, n);
     }
     /* 3. move the cursor to the 13th byte of the input file */
     lseek(fd_a, 12, 0);
     /* write the given text in output file */
     write(fd_b, "\nMoved cursor to 13th byte:\n", 28);
     /* writes the contents of input file from 12 byte to EOF */
     while ((n = read(fd_a, str, 10)) > 0) {
             write(fd_b, str, n);
     }
     /* 4. close both input and output files */
     close(fd_a);
     close(fd_b);
     return 0;
}
```
1.  The system call `open()` with different arguments: one to _read_, the other to _write_.
    -   Two file descriptors, **fd_a** and **fd_b** are returned from the system call. Now the program can read the content of `input.txt`.
    -   `input.txt` is a text file with content “abcdefghijklmnopqrstuvwxyz” (the entire 26 alphabets, 26 bytes in content size).
2.  We can perform `read` system call and `write` system call with opened files through `fd_a` and `fd_b`.
    -   We no longer have to associate it with the name input.txt and output.txt
3.  Afterwards, we **change** the current pointer (`cp`) of the file using system call `lseek`.
    -   This updates the entry for this file in the system-wide opened file table. We move the pointer to point to the 13th byte, which is the letter ‘m’
4.  Do not forget to **close** the file descriptor using the `close()` system call.

Upon execution, we found that the output.txt contains:

```
abcdefghijklmnopqrstuvwxyz

Moved cursor to 13th byte:
mnopqrstuvwxzy
```