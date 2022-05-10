---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Android Activity Lifecycle
So far we have been writing code in `onCreate()`, which is called when the activity starts.
When interacting with the app, the user may find himself doing some of the following actions:
- Access a different activity
- Rotate the screen
- Access a new app
- Close the app

This changes the state of the current activity.
In doing so, other callbacks are executed. The callbacks are summarised in the following diagram of the Android Activity Lifecycle.
![[Pasted image 20220322144923.png]]
Implement the seven callbacks in your app, and write a logical message in each of them.
- Which methods are called as the activity starts?
- Which methods are called as you navigate from one activity to another?
- Which methods are called as you rotate the screen?

The next callback that we will write code in is `onPause()`

This is typically done when you want to carry out the following takss before the activity is destroyed:
- save data
- stop a timer