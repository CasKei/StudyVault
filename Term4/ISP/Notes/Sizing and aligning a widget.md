---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## Sizing a widget
For **layout_width** and **layout_height** attributes:
- **wrap_content**: widget fits content
- **match_parent**: widget fits screen size
```xml
<TextView
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:text="AA"/>
<TextView
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:text="AA"/>
```

## Alignment
Note the difference between the two: 
- To align a widget **within a layout**, use the **`layout_gravity`** attribute (*child to parent*)
	- `android:layout_gravity="center"`
- To align the contents of a widget **within itself**, use the **`gravity`** attribute (*parent to child*)
	- `android:gravity="center"`

`gravity` will have no effect when: layout wrap content\
`layout_gravity` will have no effect when: layout match parent