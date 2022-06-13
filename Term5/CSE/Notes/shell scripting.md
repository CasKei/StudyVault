---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]

## Why
Now that we have learned _how_ to execute some commands, it is natural to **question** _why_ we need to use the command line. What can you do here with CLI that you cannot do through your common graphical user interface?

-   Well, it **depends** on your **purpose**. There’s a lot of debate on that, some might say that CLI allows you to do tasks **fast**, but that depends: depends on how **well versed you are** in using the CLI.
-   If you are just a basic user, i.e: browse, watch your favorite tv series, edit photos, or text your friends then chances are you don’t need to use the command line.
-   *If you’re a computer science graduate who intends to work in the field then CLI is probably your new best friend.*

The most common use of the command line is ”system administration” or, basically, **managing** computers and servers.

This includes **installing** and **configuring** software, **monitoring** computer resources (manage logs, setup cron jobs, daemons), **setting** up web servers (renaming or modifying thousands of files), and **automating** processes (setup databases / servers) on many hosts.

Obviously these tasks are **repetitive** and **tedious** such that it is impossible to be done manually or one by one via the GUI.

## Scripting
In this section, we briefly overview how shell scripts work, eg: `.sh`, `.zsh` scripts. A shell script is simply lines of code for the shell to interpret (if you use z/bash shell, you can use z/bash shell script. Since both bash and z are derived from the Bourne shell family, both scripts have similar syntax).

Why do we need to write a shell script? Imagine you want to create thousands of text files (using touch). You wouldn’t want to type the command one by one, but rather just run a script that does this task in one shot.

Open `nano` and type the following:
```bash
#!/bin/bash

start_time=$(date +%s)

# the following substitute the arguments as a list, without re-splitting them on whitespace
"$@" 

end_time=$(date +%s)

echo "Time elapsed: $(($end_time - $start_time)) seconds"
```
Then, save it with a name `run.sh`, and change its mode to be executable: `chmod +x run.sh`. Now you can run any script and **time** it. For instance, suppose we have the following python script:
```python
import time
print("Loading.....")
time.sleep(2.5)
print("Done")
```
Running it with our script will **time** the execution of the python script above:
```bash
bash-3.2$ ./run.sh python3 hello.py
Loading.....
Done
Time elapsed: 3 seconds
bash-3.2$ 
```

From the task above, you have just created and run a super simple bash script. Note that the first line is the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)). Similar to coding in any other language, you can use variables, functions, conditional statements, loops, comparisons, etc in your bash script. You can learn more in your own time, and see [examples of awesome bash scripts](https://github.com/awesome-lists/awesome-bash).

For example, you can [customize your prompt](https://github.com/arialdomartini/oh-my-git) in a git repo: ![](https://natalieagus.github.io/50005/assets/images/lab1/20.png)