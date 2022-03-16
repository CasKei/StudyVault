---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

You can preview an app's layout with a horizontal orientation, and with different devices, without having to run the app on an emulator or device.

To preview the layout for a different orientation, click the **Orientation in Editor** button ![ Orientation in Editor button](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/ic_orientation_in_editor_button.png " Orientation in Editor button") in the top toolbar. To show the layout in a horizontal orientation, select **Switch to Landscape**. To return to vertical orientation, select **Switch to Portrait**.

You can also preview the layout for different devices. Click the **Device in Editor** button ![ Device in Editor button](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/ic_device_in_editor_button.png " Device in Editor button") in the top toolbar, and select a different device in the drop-down menu. For example, select **Nexus 4**, **Nexus 5**, and then **Pixel** to see differences in the previews.

To create a variant of the layout strictly for the horizontal orientation, leaving the vertical orientation layout alone: click the **Orientation in Editor** button and select **Create Landscape Variation**. A new editor window opens with the **land/activity_main.xml** tab showing the layout for the landscape (horizontal) orientation. You can change this layout, which is specifically for horizontal orientation, without changing the original portrait (vertical) orientation.

In the **Project > Android** pane, look inside the **res > layout** directory. You see that Android Studio automatically creates the variant for you, called `activity_main.xml (land)`.![ The file for the layout variant in the layout directory](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_layout_landscape_xml.png " The file for the layout variant in the layout directory")

To create a layout variant for tablet-sized screens, click the **Orientation in Editor** button and select **Create layout x-large Variation**. A new editor window opens with the **xlarge/activity_main.xml** tab showing the layout for a tablet-sized device. The editor also picks a tablet device, such as the Nexus 9 or Nexus 10, for the preview. In the **Project > Android** pane, look inside the **res > layout** directory. You see that Android Studio automatically creates the variant for you, called `activity_main.xml (xlarge)`. You can change this layout, which is specifically for tablets, without changing the other layouts.