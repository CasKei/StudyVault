---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]
[[Using the Log]]

## Logcat
The **Logcat** tab of your Android Studio displays messages as your app runs. You may display your own messages to the Logcat using the **Log** class.

Messages in the Logcat are divided into one of the following levels
- `d`: debug
- `w`: warning
- `e`: error
- `i`: info

In addition, every message has a tag for added filtering.
Typically, the apps we do are small, so just stick to one of these levels.

A typical statement to print a message as follows:
```java
Log.i(TAG, "Empty String");
```

**TAG**: a `String` variable that is declared **final** and **static**. Here, we are specifying that the message uses the `i` level.

Having your app print messages to the Logcat is useful for
- viewing data without having to display it on the UI
- Checking and debugging your code
