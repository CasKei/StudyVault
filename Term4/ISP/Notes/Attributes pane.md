---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

The **Attributes** pane offers access to all of the XML attributes you can assign to a UI element. You can find the attributes (known as _properties_) common to all views in the [`View`](http://developer.android.com/reference/android/view/View.html) class documentation.

To show the **Attributes** pane, click the **Attributes** tab on the right side of the layout editor. The **Attributes** pane includes a square sizing panel called the _view inspector_. The symbols inside the view inspector represent the height and width settings.![ Sizing panel in the Attributes pane](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_layout_width_height_box_annot.png " Sizing panel in the Attributes pane")

The figure above shows the **Attributes** pane:

1.  **Vertical view size control**. The vertical size control, which appears on the top and bottom of the view inspector, specifies the `layout_height` property. The angles indicate that this size control is set to `wrap_content`, which means the UI element expands vertically as needed to fit its contents. The "8" indicates a standard margin set to 8 dp.
2.  **Horizontal view size control**. The horizontal size control, which appears on the left and right of the view inspector, specifies the `layout_width`. The angles indicate that this size control is set to `wrap_content`, which means the UI element expands horizontally as needed to fit its contents, up to a margin of 8 dp.
3.  **Attributes** pane close button. Click to close the pane.

The `layout_width` and `layout_height` attributes in the **Attributes** pane change as you change the inspector's horizontal and vertical size controls. These attributes can take one of three values for a `ConstraintLayout`:

-   The `match_constraint` setting expands the UI element to fill its parent by width or height up to a margin, if a margin is set. The parent in this case is the `ConstraintLayout`.
-   The `wrap_content` setting shrinks the UI element to the size of its content. If there is no content, the element becomes invisible.
-   To specify a fixed size that's adjusted for the screen size of the device, set a number of `dp` ([density-independent pixels](https://developer.android.com/training/multiscreen/screendensities.html)). For example, `16dp` means 16 density-independent pixels.

**Tip**: If you change the `layout_width` attribute using its popup menu, the `layout_width` attribute is set to zero because there is no set dimension. This setting is the same as `match_constraint`—the UI element can expand as much as possible to meet constraints and margin settings.

The **Attributes** pane offers access to all of the attributes you can assign to a `View` element. You can enter values for each attribute, such as the `android:id`, `background`, `textColor`, and `text` attributes.