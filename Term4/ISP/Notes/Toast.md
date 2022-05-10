---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Toasts
**Toast**: a message on an android app that disappears after a while.
Displayed to notify users of an event occurring.

Code recipe of a toast:
- Call **static factory method** `makeText()` of the toast class and give its required inputs:
	- `Context` object: a superclass of `AppCompatActivity` [docs](https://developer.android.com/reference/android/support/v7/app/AppCompatActivity): specifying context means to say on which Activity will your Toast be seen
	- Either a resource `id` or a `String`: hardcoded String not recommended
	- Duration of Toast. Specify one of two static variables in this
		- `Toast.LENGTH_SHORT` or `Toast.LENGTH_LONG`
- `makeText()` returns a `Toast` object. Can then call the `show()` instance method to display the toast.

e.g.
```java
Toast.makeText(MainActivity.this,
			   R.string.warning_blank_edit_text, Toast.LENGTH_LONG).show();
```
If you read documentation,
- Toast class [[Week 2 - Constructors|constructor]] is **public**. It is used when you want to customise the design of your toast.
- Most of the time, there is no need to, so `makeText()` gives the standard Toast design.

