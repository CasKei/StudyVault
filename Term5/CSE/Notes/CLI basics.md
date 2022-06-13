---
aliases: 
tags: 50.005
---
[[50.005 Computer System Engineering|50.005]]
[[Intro to Command Line Interface]]

## Commands
The CLI accepts **commands** (the **first** word, e.g. ps, that you type into the CLI is the command), **entered line by line** and it will be executed **sequentially**. There are two types of commands in general, commands **with** and **without** options or arguments.

## Without Options
Try the following basic commands in sequence `date`, `cal`, `pwd`, `who`, `clear`:

- Figure out what each command does using `man`
- You can use `man <command>` and press `q` to quit anytime.

## With Options
The commands you have typed above are those that **do not** require options or more arguments (although they do accept these too). Some commands require more input arguments.

For example, the command ps shows the list of processes for the current shell, while `ps -x` shows all processes that are owned by the current user even when it doesn’t have a **controlling terminal**.

Some commands accept single hyphen (-) as options, and some other accepts double hyphens (–), or no hyphen at all. It really depends on **convention**, so be sure to **read the manual properly**.

For example, the command: `git commit -v -a --amend` stands for:
-   Use git to **stage** new changes (`commit`)
-   Automatically stage **all** files that have been modified/deleted (`-a`)
-   Do it in a **verbose** way, with detailed message highlighting all diff (`-v`)
-   **Replace** the tip of the current branch by creating a new commit (`--amend`)


## Path
[[Directory]]
`pwd`
`ls`
`cd ../..`
`cd Desktop/Downloads`

[[Environment variables]]
`$HOME`
`env`
`echo`
`$PATH`

## Configuring a Terminal Session
[[Configuring a Terminal Session]]
`touch .bashrc`
...
`exec bash`

## Common Commands
[[CLI common commands]]


## Command-Line Text Editor: nano, vim
[[nano, vim]]


## Standard Streams
[[Standard stream]]

