---
aliases: environment variable
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]
[[CLI basics]]

Another way of providing context is through something called **environment** **variables**.

## $HOME
Tryout the command: `cd $HOME`
-   The `$HOME` part is a reference to the **HOME variable, and is replaced by the path to your home directory** when the command is run.
-   In other words, running cd `$HOME` is the *same as* running `cd <actual path to your home>`, or `cd ~` (~ is a default **shell variable** that points to the current User’s home directory, and it also has [other usages](https://www.baeldung.com/linux/tilde-bash) that you can read if you’re free).
-   To checkout what the value of your `$HOME` variable is, type the command: echo `$HOME`

## env
To **find out about your current environment variables**, you can enter the command `env`. Look at the values of common variables such as `HOME` and `PATH`. You can also create your own environment variables using the command `export`.

For example:
1.  Run the command: `export MESSAGE1="This is message 1"`
2. You can now execute `echo $MESSAGE1` and observe get the string output

In the example below, the environment variable `$MESSAGE1` initially did not exist. After we `export` it, we can now print the environment variable `$MESSAGE1`.
![](https://natalieagus.github.io/50005/assets/images/lab1/4.png)

## $PATH
One of the most important environment variables you’ll work with on the command line is **$PATH**.
-   This is the key to how our shell **knows** which file to execute for commands like cd or echo or other built-in or installed programs.
-   The PATH variable provides the **additional context** that the command line needs to figure out where that particular file is in the system.
-   Hence, if you have installed an app (e.g: Telegram) and tried to execute the binary from the command line and met with the error `command not found`, it simply means you haven’t added the path where that binary is to the `$PATH` environment variable.

For example, you can add the **binary** of the **Telegram** app onto the `$PATH` using the command `export`, and now you can simply execute it from anywhere (a new Telegram window is opened on the second Telegram command):
![](https://natalieagus.github.io/50005/assets/images/lab1/5.png)