---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## onCreate is called when the Activity is first launched
Within the **MainActivity** class, you would see this code

```java
@Override
protected void onCreate(Bunble savedInstanceState) {
	super.onCreate(savedInstanceState);
	setContentView(R.layout.activity_main);
}
```
The **onCreate** method is called whenever your Activity is first launched e.g. when user clicks your app icon.

This method is part of the methods in the **Android activity life cycle**, which will be discussed in the [[Android 2|next lesson]].

You write code in **onCreate** to implement what you want the user to see when the activity is launched.

## In OnCreate, the [[The layout editor|layout]] is first inflated
`R.layout.activity_main` is passed to the `setContentView` method to **inflate the layout**.\
In this process, Android reads to [[Editing XML directly|XML]] code in the layout file and instantiates objects in the memory that represent each of the widgets on the Activity.