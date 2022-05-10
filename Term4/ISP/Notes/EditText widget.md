---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## EditText widget
Typical xml tag of an **EditText** widget:
```xml
<EditText
	android:id="@+id/editTextValue"
	android:hint="Enter amount"
	android:gravity="center"
	android:inputType="numberDecimal"
	android:layout_width="match_parent"
	android:layout_height="wrap_content" />
```
`android:hint` attribute displays a faint grey text telling the user what to enter in the box.
`android:inputType` attribute restricts the type of input into the box.
[Documentation on allowable inputs](https://developer.android.com/training/keyboard-input/style)
