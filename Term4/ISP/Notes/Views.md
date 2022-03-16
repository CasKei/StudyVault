---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

# Views
The UI consists of a hierarchy of objects called _views_ — every element of the screen is a [`View`](https://developer.android.com/reference/android/view/View.html). The `View` class represents the basic building block for all UI components, and the base class for classes that provide interactive UI components such as buttons, checkboxes, and text entry fields.

A `View` has a location, expressed as a pair of left and top coordinates, and two dimensions, expressed as a width and a height. The unit for location and dimensions is the density-independent pixel (dp).

The Android system provides hundreds of predefined `View` subclasses. Commonly used `View` subclasses described over several lessons include:
-   [`TextView`](http://developer.android.com/reference/android/widget/TextView.html) [[TextView]]for displaying text ^0d549a
-   [`EditText`](https://developer.android.com/reference/android/widget/EditText.html) to enable the user to enter and edit text
-   [`Button`](https://developer.android.com/reference/android/widget/Button.html) and other clickable elements (such as [`RadioButton`](https://developer.android.com/reference/android/widget/RadioButton.html), [`CheckBox`](https://developer.android.com/reference/android/widget/CheckBox.html), and [`Spinner`](https://developer.android.com/reference/android/widget/Spinner.html)) to provide interactive behavior
-   [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView.html) and [`RecyclerView`](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html) to display scrollable items [[Scrolling Views]]
-   [`ImageView`](https://developer.android.com/reference/android/widget/ImageView.html) for displaying images
-   [`ConstraintLayout`](https://developer.android.com/reference/android/support/constraint/ConstraintLayout.html) and [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout.html) for containing other views and positioning them

You can define a `View` to appear on the screen and respond to a user tap. A `View` can also be defined to accept text input, or to be invisible until needed.

You can specify `View` elements in layout resource files. Layout resources are written in XML and listed within the **layout** folder in the **res** folder in the **Project > Android** pane.

### ViewGroup groups
`View` elements can be grouped inside a [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup.html), which acts as a container. The relationship is parent-child, in which the _parent_ is a `ViewGroup`, and the _child_ is a `View` or another `ViewGroup`. The following are commonly used `ViewGroup` groups:

-   [`ConstraintLayout`](https://developer.android.com/reference/android/support/constraint/ConstraintLayout.html): A group that places UI elements (child `View` elements) using constraint connections to other elements and to the layout edges (parent `View`).
-   [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView.html): A group that contains one other child `View` element and enables scrolling the child `View` element.
-   [`RecyclerView`](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html): A group that contains a list of other `View` elements or `ViewGroup` groups and enables scrolling them by adding and removing `View` elements dynamically from the screen.

### Layout ViewGroup groups
The `View` elements for a screen are organized in a hierarchy. At the _root_ of this hierarchy is a [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup.html) that contains the layout of the entire screen. The `ViewGroup` can contain child `View` elements or other `ViewGroup` groups as shown in the following figure.![ The View hierarchy](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/dg_viewgroup_hierarchy.png " The View hierarchy")

In the figure above:
1.  The _root_ `ViewGroup`.
2.  The first set of child `View` elements and `ViewGroup` groups whose parent is the root.

Some `ViewGroup` groups are designated as _layouts_ because they organize child `View` elements in a specific way and are typically used as the root `ViewGroup`. Some examples of layouts are:

-   [`ConstraintLayout`](http://tools.android.com/tech-docs/layout-editor): A group of child `View` elements using constraints, edges, and guidelines to control how the elements are positioned relative to other elements in the layout. `ConstraintLayout` was designed to make it easy to click and drag `View` elements in the layout editor.
-   [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout.html): A group of child `View` elements positioned and aligned horizontally or vertically.
-   [`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout.html): A group of child `View` elements in which each element is positioned and aligned relative to other elements within the `ViewGroup`. In other words, the positions of the child `View` elements can be described in relation to each other or to the parent `ViewGroup`.
-   [`TableLayout`](https://developer.android.com/reference/android/widget/TableLayout.html): A group of child `View` elements arranged into rows and columns.
-   [`FrameLayout`](https://developer.android.com/reference/android/widget/FrameLayout.html): A group of child `View` elements in a stack. `FrameLayout` is designed to block out an area on the screen to display one `View`. Child `View` elements are drawn in a stack, with the most recently added child on top. The size of the `FrameLayout` is the size of its largest child `View` element.
-   [`GridLayout`](https://developer.android.com/reference/android/widget/GridLayout.html): A group that places its child `View` elements in a rectangular grid that can be scrolled.![ Visual representations of layouts](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/dg_common_layouts_visual_rep.png " Visual representations of layouts")

**Tip**: Learn more about different layout types in [Common Layout Objects](https://developer.android.com/guide/topics/ui/layout-objects.html).

A simple example of a `LinearLayout` with child `View` elements is shown below as a diagram of the layout file (`activity_main.xml`), along with a hierarchy diagram (top right) and a screenshot of the actual finished layout (bottom right).![ Layout concept (left), View hierarchy (right, top) and finished layout (right, bottom)](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/dg_layout_diagram_and_hierarchy.png " Layout concept (left), View hierarchy (right, top) and finished layout (right, bottom)")

In the figure above:
1.  `LinearLayout`, the root `ViewGroup`, contains all the child `View` elements in a vertical orientation.
2.  `Button` (`button_toast`). The first child `View` element appears at the top in the `LinearLayout`.
3.  `TextView` (`show_count`). The second child `View` element appears under the first child `View` element in the `LinearLayout`.
4.  `Button` (`button_count`). The third child `View` element appears under the second child `View` element in the `LinearLayout`.

The layout hierarchy can grow to be complex for an app that shows many `View` elements on a screen. It's important to understand the hierarchy, as it affects whether `View` elements are visible and how efficiently they are drawn.

**Tip**: You can explore the layout hierarchy of your app using [Hierarchy Viewer](https://developer.android.com/studio/profile/hierarchy-viewer-walkthru.html). It shows a tree view of the hierarchy and lets you analyze the performance of `View` elements on an Android-powered device. Performance issues are covered in a subsequent chapter.