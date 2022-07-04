---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Week 6 - Files]]
![[File System Mapping#Case 1]]

```c
  int fd_a, fd_b, fd_c, n;
  char str;

  /* open an input file in read mode */
  fd_a = open("input.txt", O_RDONLY, 0);    // open
  // fd_b will be the LOWEST available fd, which is 4
  fd_b = dup(fd_a);                         // dup
  fd_c = dup2(fd_a, 9); // custom fd 9      // dup2
```
The difference between the two system calls is that `dup()` will return the **lowest** available `fd`, which is 4 (since 0, 1, and 2 are _reserved_ (set by default due to convention) as `stdin`, `stdout`, and `stderr`, and 3 is already used for `open()`, while `dup2(old fd, new fd)` allows us to explicitly set the `new fd`.

> If the new fd is **already in use** then the existing one will be closed first before being reused again. Note that fd 0, 1, and 2 can be closed or changed to point to another file as per other fds. The only difference is that upon process creation, these 3 fds are _already_ set as convenience to stdin, stdout, and stderr.

Can cause process to [[Types of system calls|block]] itself ([[UNIX File System Data Structure#Example]] use `scanf` or some blocking operation that waits for user input) and meanwhile `print` its [[File Descriptor Table]] content (use `ps` to get `pid` and then `lsof -p pid`)

Since they share the ==same pointer== to the [[System-Wide Open File Table (swoft)]], the actions from `fd_a` and `fd_b` **affect each other**.

e.g.
```c
/* read the data from fd_a */
  printf("From fd_a: ");
  int counter = 0;
  while ((n = read(fd_a, &str, 1)) > 0) {
          printf("%c", str);
          counter++;
          if (counter > 9) break;
  }
  printf("\n");

  /* read the data from fd_b */
  printf("From fd_b: ");
  counter = 0;
  while ((n = read(fd_b, &str, 1)) > 0) {
          printf("%c", str);
          counter++;
          if (counter > 9) break;
  }
  printf("\n");

  int fd_d = open("input.txt", O_RDONLY, 0);
  /* read back the data from fd_a */
  printf("From fd_d: ");
  counter = 0;
  while ((n = read(fd_d, &str, 1)) > 0) {
          printf("%c", str);
          counter ++;
          if (counter > 9) break;
  }
  printf("\n");
```

If read first 10 char from `fd_a`, `cp` in [[System-Wide Open File Table (swoft)]] would have been advanced by 10 bytes. Next 10 bytes read by `fd_b` will read from byte 10 to 19.
Assuming that `input.txt` contains all 26 alphabets as mentioned above, the output of the program above will be:

```whatever
From fd_a: abcdefghij
From fd_b: klmnopqrst
From fd_d: abcdefghij
```

Note that `fd_d` is a **different entry** in the [[System-Wide Open File Table (swoft)]] because a read operation using `fd_a` and `fd_b` does not affect the read operation using `fd_d`.

> `fd_d` does not share the same **pointer** `cp` as both `fd_a` and `fd_b`.