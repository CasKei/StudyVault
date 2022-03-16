---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

### Using ConstraintLayout

The layout editor offers more features in the **Design** tab when you use a `ConstraintLayout`, including handles for defining constraints.

A _constraint_ is a connection or alignment to another UI element, to the parent layout, or to an invisible guideline. Each constraint appears as a line extending from a circular handle. After you select a UI element in the **Component Tree** pane or click it in the layout editor, the element shows a resizing handle on each corner and a circular constraint handle in the middle of each side.![ The constraint and resizing handles on Views](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_layout_constraint_2_handles_annot.png " The constraint and resizing handles on Views")

The figure above shows the constraint and resizing handles on `View` elements in a layout:
1.  **Resizing handle**.
2.  **Constraint line and handle**. In the figure, the constraint aligns the left side of the **Toast** `Button` to the left side of the layout.
3.  **Constraint handle** without a constraint line.
4.  **Baseline handle**. The baseline handle aligns the text baseline of an element to the text baseline of another element.

In the blueprint or design panes, the following handles appear on the `TextView` element:
-   **Constraint handle**: To create a constraint, click a constraint handle, shown as a circle on each side of an element. Then drag the circle to another constraint handle or to a parent boundary. A zigzag line represents the constraint.![ Constraint handle](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/handles.png " Constraint handle")
    
-   **Resizing handle**: You can drag the square resizing handles to resize the element. While dragging, the handle changes to an angled corner.![ Constraint handle](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/handle_resize.png " Constraint handle")
    

You can drag the resizing handles on each corner of the UI element to resize it, but doing so hard-codes the width and height dimensions, which you should avoid for most elements because hard-coded dimensions don't adapt to different screen densities.

#### Constraining a UI element
To add a constraint to a UI element, click the circular handle and drag a line to another element or to the side of a layout, as shown in the two animated figures below. To remove a constraint from an element, click the circular handle.![ Deleting and adding a constraint](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/hello_world_textview_constraints.gif " Deleting and adding a constraint")

![](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/hello_toast7_drag_buttons_constrain.gif%20Constrain%20the%20two%20Button%20elements)

The constraints you define in the layout editor are created as XML attributes, which you can see in the **Text** tab as described in "[Editing XML directly](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-1-build-your-first-app/1-2-c-layouts-and-resources-for-the-ui/1-2-c-layouts-and-resources-for-the-ui.html#xml)" in this chapter. For example, the following XML code is created constraining the top of an element to the top of its parent:

```xml
app:layout_constraintTop_toTopOf="parent"
```

#### Using a baseline constraint

You can align one UI element that contains text, such as a `TextView` or `Button`, with another UI element that contains text. A _baseline constraint_ lets you constrain the elements so that the text baselines match. Select the UI element that has text, and then hover your pointer over the element until the baseline constraint button ![](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/ic_ab_baseline_icon.png%20Baseline%20constraint%20button) appears underneath the element.

Click the baseline constraint button. The baseline handle appears, blinking in green as shown in the animated figure. Drag a baseline constraint line to the baseline of the other UI element.![](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/hello_toast8_align_baselines.gif%20Constrain%20the%20baselines%20of%20the%20two%20Button%20elements)

**Tip**: For an in-depth tutorial on using `ConstraintLayout`, see [Using ConstraintLayout to design your views](https://codelabs.developers.google.com/codelabs/constraint-layout/index.html).