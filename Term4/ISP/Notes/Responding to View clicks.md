---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

>A _click event_ occurs when the user taps or clicks a clickable `View`, such as a [`Button`](https://developer.android.com/reference/android/widget/Button.html), [`ImageButton`](https://developer.android.com/reference/android/widget/ImageButton.html), [`ImageView`](https://developer.android.com/reference/android/widget/ImageView.html), or [`FloatingActionButton`](https://developer.android.com/reference/android/support/design/widget/FloatingActionButton.html).

When such an event occurs, your code performs an action. In order to make this pattern work, you have to:
-   Write a Java method that performs the specific action you want the app to do when this event occurs. This method is typically referred to as an _event handler_.
-   Associate this event-handler method to the `View`, so that the method executes when the event occurs.

### The onClick attribute
Android Studio provides a shortcut for setting up a clickable `View`, and for associating an event handler with the `View`: use the `android:onClick` attribute in the XML layout.

For example, the following XML attribute sets a `Button` to be clickable, and sets `showToast()` as the event handler:
```xml
<Button
    android:id="@+id/button_toast"
    android:onClick="showToast"
```
When the user taps the `button_toast` `Button`, the button's `android:onClick` attribute calls the `showToast()` method. In order to work with the `android:onClick` attribute, the `showToast()` method must be `public` and return `void`. To know which `View` called the method, the `showToast()` method must require a `view` parameter.

Android Studio provides a shortcut for creating an event handler _stub_ (a placeholder for a method that you can fill in later) in the code for the `Activity` associated with the XML layout. Follow these steps:
1.  Inside the XML layout file (such as `activity_main.xml`), click the method name in the `android:onClick` attribute statement (`showToast` in the XML snippet above).
2.  Press **Alt-Enter** in Windows or **Option-Return** in Mac OS X, and select **Create onClick event handler**.
3.  Select the `Activity` associated with the layout file (such as **MainActivity**) and click **OK**. Android Studio creates a placeholder method stub in `MainActivity.java` as shown below.

```java
public void showToast(View view) {
        // Do something in response to the button click.
}
```

### Updating a View
To update a `View`, for example to replace the text in a `TextView`, your code must first instantiate an object from the `View`. Your code can then update the object, which updates the screen.

To refer to the `View` in your code, use the [`findViewById()`](https://developer.android.com/reference/android/view/View.html#findViewById(int)) method of the `View` class, which looks for a `View` based on the resource `id`. For example, the following statement sets `mShowCount` to be the `TextView` in the layout with the resource id `show_count`:
```xml
mShowCount = (TextView) findViewById(R.id.show_count);
```

From this point on, your code can use `mShowCount` to represent the `TextView`, so that when you update `mShowCount`, the `TextView` is updated.

For example, when the following `Button` with the `android:onClick` attribute is tapped, `onClick` calls the `countUp()` method:
```xml
android:onClick="countUp"
```

You can implement `countUp()` to increment the count, convert the count to a string, and set the string as the text for the `mShowCount` object:
```java
public void countUp(View view) {
        mCount++;
        if (mShowCount != null)
            mShowCount.setText(Integer.toString(mCount));
}
```
Since you had already associated `mShowCount` with the `TextView` for displaying the count, the `mShowCount.setText()` method updates the `TextView` on the screen.