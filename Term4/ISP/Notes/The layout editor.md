---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

You define layouts in the layout editor, or by entering XML code.

The layout editor shows a visual representation of XML code. You can drag `View` elements into the design or blueprint pane and arrange, resize, and specify attributes for them. You immediately see the effect of changes you make.

To use the layout editor, double-click the XML layout file (**activity_main.xml**). The layout editor appears with the **Design** tab at the bottom highlighted. (If the **Text** tab is highlighted and you see XML code, click the **Design** tab.) For the Empty Activity template, the layout is as shown in the figure below.

  
![ Exploring Android Studio](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_activity_main_in_project_pane_annot.png " Exploring Android Studio")

1.  XML layout file (**activity_main.xml**).
2.  **Design** and **Text** tabs. Click **Design** to see the layout editor, or **Text** to see XML code.
3.  **Palette** pane. The Palette pane provides a list of UI elements and layouts. Add an element or layout to the UI by dragging it into the design pane.
4.  **Component Tree**. The Component Tree pane shows the layout hierarchy. Click a `View` element or `ViewGroup` in this pane to select it. `View` elements are organized into a tree hierarchy of parents and children, in which a child inherits the attributes of its parent. In the figure above, the `TextView` is a child of the `ConstraintLayout`.
5.  Design and blueprint panes. Drag `View` elements from the **Palette** pane to the design or blueprint pane to position them in the layout. In the figure above, the layout shows only one element: a `TextView` that displays "Hello World".
6.  **Attributes** tab. Click **Attributes** to display the **Attributes** pane for setting attributes for a `View` element.

## Layout editor toolbars
The layout editor toolbars provide buttons to configure your layout and change its appearance. The top toolbar lets you configure the appearance of the layout preview in the layout editor:![ Top toolbar of the layout editor](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_constraint_toolbar1_annot.png " Top toolbar of the layout editor")

The figure above shows the top toolbar of the layout editor:

1.  **Select Design Surface**: Select **Design** to display a color preview of the UI elements in your layout, or **Blueprint** to show only outlines of the elements. To see _both_ panes side by side, select **Design + Blueprint**.
2.  **Orientation in Editor**: Select **Portrait** or **Landscape** to show the preview in a vertical or horizontal orientation. The orientation setting lets you preview the layout orientations without running the app on an emulator or device. To create alternative layouts, select **Create Landscape Variation** or other variations.
3.  **Device in Editor**: Select the device type (phone/tablet, Android TV, or Android Wear).
4.  **API Version in Editor**: Select the version of Android to use to show the preview.
5.  **Theme in Editor**: Select a theme (such as **AppTheme**) to apply to the preview.
6.  **Locale in Editor**: Select the language and locale for the preview. This list displays only the languages available in the string resources (see the lesson on localization for details on how to add languages). You can also select **Preview as Right To Left** to see the layout as if an RTL language had been chosen.

The layout editor also offers a second toolbar that lets you configure the appearance of UI elements in a `ConstraintLayout` and zoom in and out of the preview:![ ConstraintLayout editing toolbar](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_constraint_toolbar2_annot.png " ConstraintLayout editing toolbar")

The figure above shows the `ConstraintLayout` editing toolbar:
1.  **Show**: Select **Show Constraints** and **Show Margins** to show them in the preview, or to stop showing them.
2.  **Autoconnect**: Enable or disable Autoconnect. With Autoconnect enabled, you can drag any element (such as a `Button`) to any part of a layout to generate constraints against the parent layout.
3.  **Clear All Constraints**: Clear all constraints in the entire layout.
4.  **Infer Constraints**: Create constraints by inference.
5.  **Default Margins**: Set the default margins.
6.  **Pack**: Pack or expand the selected elements.
7.  **Align**: Align the selected elements.
8.  **Guidelines**: Add vertical or horizontal guidelines.
9.  Zoom controls: Zoom in or out.