---
aliases: XML attributes
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]
[[XML Syntax|XML]]

It is sometimes quicker and easier to edit the XML code directly, especially when copying and pasting the code for similar views.

To view and edit the XML code, open the XML layout file. The layout editor appears with the **Design** tab at the bottom highlighted. Click the **Text** tab to see the XML code. The following shows the XML code for a `LinearLayout` with two `Button` elements with a `TextView` in the middle:

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context="com.example.android.hellotoast.MainActivity">

    <Button
        android:id="@+id/button_toast"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginEnd="8dp"
        android:layout_marginStart="8dp"
        android:layout_marginTop="8dp"
        android:background="@color/colorPrimary"
        android:onClick="showToast"
        android:text="@string/button_label_toast"
        android:textColor="@android:color/white" />

    <TextView
        android:id="@+id/show_count"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:layout_marginBottom="8dp"
        android:layout_marginEnd="8dp"
        android:layout_marginStart="8dp"
        android:layout_marginTop="8dp"
        android:background="#FFFF00"
        android:text="@string/count_initial_value"
        android:textAlignment="center"
        android:textColor="@color/colorPrimary"
        android:textSize="160sp"
        android:textStyle="bold"
        android:layout_weight="1"/>

    <Button
        android:id="@+id/button_count"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="8dp"
        android:layout_marginEnd="8dp"
        android:layout_marginStart="8dp"
        android:background="@color/colorPrimary"
        android:onClick="countUp"
        android:text="@string/button_label_count"
        android:textColor="@android:color/white" />
</LinearLayout>
```

### XML attributes (view properties)
Views have _properties_ that define where a view appears on the screen, its size, how the view relates to other views, and how it responds to user input. When defining views in XML or in the layout editor's **Attributes** pane, the properties are referred to as _attributes_.

For example, in the following XML description of a `TextView`, the `android:id`, `android:layout_width`, `android:layout_height`, `android:background`, are XML attributes that are translated automatically into the `TextView` properties:

```xml
<TextView
       android:id="@+id/show_count"
       android:layout_width="match_parent"
       android:layout_height="wrap_content"
       android:background="@color/myBackgroundColor"
       android:textStyle="bold"
       android:text="@string/count_initial_value" />
```

Attributes generally take this form:

`android:`_attribute_name_=`"`_value_`"`

The _attribute_name_ is the name of the attribute. The _value_ is a string with the value for the attribute. For example:

```xml
android:textStyle="bold"
```

If the _value_ is a resource, such as a color, the `@` symbol specifies what kind of resource. For example:

```xml
android:background="@color/myBackgroundColor"
```

The background attribute is set to the color resource identified as `myBackgroundColor`, which is declared to be `#FFF043`. Color resources are described in [Style-related attributes](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-1-build-your-first-app/1-2-c-layouts-and-resources-for-the-ui/1-2-c-layouts-and-resources-for-the-ui.html#style_related) in this chapter.

Every `View` and `ViewGroup` supports its own variety of XML attributes:

-   Some attributes are specific to a `View` subclass. For example, the `TextView` subclass supports the `textSize` attribute. Any elements that extend the `TextView` subclass inherit these subclass-specific attributes.
-   Some attributes are common to all `View` elements, because they are inherited from the root [`View`](https://developer.android.com/reference/android/view/View.html) class. The `android:id` attribute is one example.

For descriptions of specific attributes, see the overview section of the [`View`](https://developer.android.com/reference/android/view/View.html) class documentation.

### Identifying a View

To uniquely identify a `View` and reference it from your code, you must give it an `id`. The `android:id` attribute lets you specify a unique `id`—a resource identifier for a `View`.

For example:
```xml
android:id="@+id/button_count"
```

The `@+id/button_count` part of the attribute creates an `id` called `button_count` for a `Button` (a subclass of `View`). You use the plus (`+`) symbol to indicate that you are creating a new `id`.

### Referencing a View
To refer to an existing resource identifier, omit the plus (`+`) symbol. For example, to refer to a `View` by its `id` in _another_ attribute, such as `android:layout_toLeftOf` (described in the next section) to control the position of a `View`, you would use:

```xml
android:layout_toLeftOf="@id/show_count"
```

In the attribute above, `@id/show_count` refers to the `View` with the resource identifier `show_count`. The attribute positions the element to be "to the left of" the `show_count` `View`.

### Positioning a View
Some layout-related positioning attributes are required for a `View` or a `ViewGroup`, and automatically appear when you add the `View` or `ViewGroup` to the XML layout.
#### LinearLayout positioning
[[Linear Layout]]
`LinearLayout` is required to have these attributes set:
-   [`android:layout_width`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.html#attr_android:layout_width)
-   [`android:layout_height`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams.html#attr_android:layout_height)
-   [`android:orientation`](https://developer.android.com/reference/android/widget/LinearLayout.html#attr_android:orientation)

The `android:layout_width` and `android:layout_height` attributes can take one of three values:
-   `match_parent` expands the UI element to fill its parent by width or height. When the LinearLayout is the root `ViewGroup`, it expands to the size of the device screen. For a UI element within a root `ViewGroup`, it expands to the size of the parent `ViewGroup`.
-   `wrap_content` shrinks the UI element to the size of its content. If there is no content, the element becomes invisible.
-   Use a fixed number of `dp` ([density-independent pixels](https://developer.android.com/training/multiscreen/screendensities.html)) to specify a fixed size, adjusted for the screen size of the device. For example, `16dp` means 16 density-independent pixels. Density-independent pixels and other dimensions are described in "[Dimensions](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-1-build-your-first-app/1-2-c-layouts-and-resources-for-the-ui/1-2-c-layouts-and-resources-for-the-ui.html#dimensions)" in this chapter.

The `android:orientation` can be:
-   `horizontal`**:** Views are arranged from left to right.
-   `vertical`**:** Views are arranged from top to bottom.

Other layout-related attributes include:
-   `android:layout_gravity`: This attribute is used with a UI element to control where the element is arranged within its parent. For example, the following attribute centers the UI element horizontally within the parent `ViewGroup`:

```
android:layout_gravity="center_horizontal"
```

-   Padding is the space, measured in density-independent pixels, between the edges of the UI element and the element's content, as shown in the figure below.![ Padding](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/dg_padding_annotated.png " Padding")

In the figure above: (1) _Padding_ is the space between the edges of the `TextView` (dashed lines) and the content of the `TextView` (solid line). Padding is not the same as _margin_, which is the space from the edge of the `View` to its parent.

The size of a `View` includes its padding. The following are commonly used padding attributes:
-   `android:padding`: Sets the padding of all four edges.
-   `android:paddingTop`: Sets the padding of the top edge.
-   `android:paddingBottom`: Sets the padding of the bottom edge.
-   `android:paddingLeft`: Sets the padding of the left edge.
-   `android:paddingRight`: Sets the padding of the right edge.
-   `android:paddingStart`: Sets the padding of the start of the view, in pixels. Used in place of the padding attributes listed above, especially with views that are long and narrow.
-   `android:paddingEnd`: Sets the padding of the end edge of the view, in pixels. Used along with `android:paddingStart`.

**Tip**: To see all of the XML attributes for a `LinearLayout`, see the Summary section of the [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout.html) class definition. Other root layouts, such as [`RelativeLayout`](http://developer.android.com/guide/topics/ui/layout/relative.html) and [`AbsoluteLayout`](https://developer.android.com/reference/android/widget/AbsoluteLayout.html), also list their XML attributes in the Summary sections.

#### RelativeLayout Positioning
Another useful `Viewgroup` for layout is [`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout.html), which you can use to position child `View` elements relative to each other or to the parent. The attributes you can use with `RelativeLayout` include the following:

-   [`android:layout_toLeftOf`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_toLeftOf): Positions the right edge of this `View` to the left of another `View` (identified by its `ID`).
-   [`android:layout_toRightOf`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_toRightOf): Positions the left edge of this `View` to the right of another `View` (identified by its `ID`).
-   [`android:layout_centerHorizontal`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_centerHorizontal): Centers this `View` horizontally within its parent.
-   [`android:layout_centerVertical`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_centerVertical): Centers this `View` vertically within its parent.
-   [`android:layout_alignParentTo`p](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_alignParentTop): Positions the top edge of this `View` to match the top edge of the parent.
-   [`android:layout_alignParentBottom`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html#attr_android:layout_alignParentBottom): Positions the bottom edge of this `View` to match the bottom edge of the parent.

For a complete list of attributes for `View` and `View` subclass elements in a `RelativeLayout`, see [`RelativeLayout.LayoutParams`](https://developer.android.com/reference/android/widget/RelativeLayout.LayoutParams.html).

### Style-related attributes
You specify style attributes to customize the appearance of a `View`. A `View` that _doesn't_ have style attributes, such as `android:textColor`, `android:textSize`, and `android:background`, takes on the styles defined in the app's theme.

The following are style-related attributes used in lesson on using the layout editor:
-   `android:background`: Specifies a color or drawable resource to use as the background.
-   `android:text`: Specifies text to display in the view.
-   `android:textColor`: Specifies the text color.
-   `android:textSize`: Specifies the text size.
-   `android:textStyle`: Specifies the text style, such as `bold`.