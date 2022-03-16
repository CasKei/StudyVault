---
aliases: log
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

The log is a powerful debugging tool you can use to look at values, execution paths, and exceptions. After you add logging statements to an app, your log messages appear along with general log messages in the **Logcat** pane.

To see the **Logcat** pane, click the **Logcat** tab at the bottom of the Android Studio window.
1.  The **Logcat** tab for opening and closing the **Logcat** pane, which displays information about your app as it is running. If you add `Log` statements to your app, `Log` messages appear here.
2.  The `Log` level menu set to **Verbose** (the default), which shows all `Log` messages. Other settings include **Debug**, **Error**, **Info**, and **Warn**.

## Adding logging statements to your app
Logging statements add whatever messages you specify to the log. Adding logging statements at certain points in the code allows the developer to look at values, execution paths, and exceptions. For example, the following logging statement adds `"MainActivity"` and `"Hello World"` to the log:

`Log.d("MainActivity", "Hello World");`

The following are the elements of this statement:
-   `Log`: The [`Log`](http://developer.android.com/reference/android/util/Log.html) class for sending log messages to the **Logcat** pane.
-   `d`: The **Debug** `Log` level setting to filter log message display in the **Logcat** pane. Other log levels are `e` for **Error**, `w` for **Warn**, and `i` for **Info**. You assign a log level so that you can filter the log messages using the drop-down menu in the center of the **Logcat** pane.
-   `"MainActivity"`: The first argument is a tag which can be used to filter messages in the **Logcat** pane. This tag is commonly the name of the `Activity` from which the message originates. However, you can name the tag anything that is useful to you for debugging.
-   `"Hello world"`: The second argument is the actual message.

By convention, log tags are defined as constants for the `Activity`:
```java
private static final String LOG_TAG = MainActivity.class.getSimpleName(); 
```

Use the constant in the logging statements:
```shell
Log.d(LOG_TAG, "Hello World"); 
```

After you add the `Log.d` statement shown above, follow these steps to see the log message:
1.  If the **Logcat** pane is not already open, click the **Logcat** tab at the bottom of Android Studio to open it.
2.  Change the `Log` level in the **Logcat** pane to **Debug**. (You can also leave the `Log` level as **Verbose**, because there are so few log messages.)
3.  Run your app on a virtual device.

The following message should appear in the **Logcat** pane:

```shell
11-24 14:06:59.001 4696-4696/? D/MainActivity: Hello World
```

## Related practical

The related practical is [1.1 Android Studio and Hello World](https://codelabs.developers.google.com/codelabs/android-training-hello-world).