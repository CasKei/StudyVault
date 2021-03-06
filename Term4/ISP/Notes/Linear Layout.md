---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]
[Doc for Linear Layout](https://developer.android.com/guide/topics/ui/layout/linear)

# Linear Layout
## Overview
Edit the XML file generated for you by replacing `ConstraintLayout` with `LinearLayout`.
In LinearLayout:
- Widgets are stacked in sequence according to orientation
- Two possible orientations: **horizontal** and **vertical**
- If no orientation attribute is specified, the default orientationis horizontal.

```xml
<LinearLayout
	android:orientation = "vertical"
>
```
```xml
<LinearLayout
	android:orientation = "horizontal"
>
```

## Detail
`LinearLayout` is a view group that aligns all children in a single direction, vertically or horizontally. You can specify the layout direction with the [`android:orientation`](https://developer.android.com/reference/android/widget/LinearLayout#attr_android:orientation) attribute.

**Note:** For better performance and tooling support, you should instead [build your layout with ConstraintLayout](https://developer.android.com/training/constraint-layout).

![[Pasted image 20220311120933.png]]

All children of a `LinearLayout` are stacked one after the other, so a vertical list will only have one child per row, no matter how wide they are, and a horizontal list will only be one row high (the height of the tallest child, plus padding). A `LinearLayout` respects _margins between children and the gravity_ (right, center, or left alignment) of each child.

## Layout Weight
[`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout) also supports assigning a _weight_ to individual children with the [`android:layout_weight`](https://developer.android.com/reference/android/widget/LinearLayout.LayoutParams#attr_android:layout_weight) attribute. This attribute assigns an "importance" value to a view in terms of how much space it should occupy on the screen. A larger weight value allows it to expand to fill any remaining space in the parent view. Child views can specify a weight value, and then any remaining space in the view group is assigned to children in the proportion of their declared weight. Default weight is zero.

### Equal Distribution
To create a linear layout in which each child uses the same amount of space on the screen, set the [`android:layout_height`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#attr_android:layout_height) of each view to `"0dp"` (for a vertical layout) or the [`android:layout_width`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#attr_android:layout_width) of each view to `"0dp"` (for a horizontal layout). Then set the [`android:layout_weight`](https://developer.android.com/reference/android/widget/LinearLayout.LayoutParams#attr_android:layout_weight) of each view to `"1"`.
### Unequal Distribution
You can also create linear layouts where the child elements use different amounts of space on the screen:
-   If there are three text fields and two of them declare a weight of 1, while the other is given no weight, the third text field without weight doesn't grow. Instead, this third text field occupies only the area required by its content. The other two text fields, on the other hand, expand equally to fill the space remaining after all three fields are measured.
-   If there are three text fields and two of them declare a weight of 1, while the third field is then given a weight of 2 (instead of 0), then it's now declared more important than both the others, so it gets half the total remaining space, while the first two share the rest equally.

The following code snippet shows how layout weights might work in a "send message" activity. The **To** field, **Subject** line, and **Send** button each take up only the height they need. This configuration allows the message itself to take up the rest of the activity's height.
```xml
<?xml version="1.0" encoding="utf-8"?>  
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"  
	android:layout_width="match_parent"  
	android:layout_height="match_parent"  
	android:paddingLeft="16dp"  
	android:paddingRight="16dp"  
	android:orientation="vertical" >  
	<EditText  
		android:layout_width="match_parent"  
		android:layout_height="wrap_content"  
		android:hint="@string/to" />  
	<EditText  
		android:layout_width="match_parent"  
		android:layout_height="wrap_content"  
		android:hint="@string/subject" />  
	<EditText  
		android:layout_width="match_parent"  
		android:layout_height="0dp"  
		android:layout_weight="1"  
		android:gravity="top"  
		android:hint="@string/message" />  
	<Button  
		android:layout_width="100dp"  
		android:layout_height="wrap_content"  
		android:layout_gravity="right"  
		android:text="@string/send" />  
</LinearLayout>
```
![[Pasted image 20220311121500.png]]

For details about the attributes available to each child view of a [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout), see [`LinearLayout.LayoutParams`](https://developer.android.com/reference/android/widget/LinearLayout.LayoutParams).

[[Android 0]]
[[Android 1]]