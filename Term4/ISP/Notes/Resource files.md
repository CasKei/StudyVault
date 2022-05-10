---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

[[Android 2]]
## res/values folder
Stores constants that appear throughout the app, such as 
- Strings
- Style definitions
- Color definitions
- Dimensions

Useful because
- Different parts of app can use same constants
- Changes can be made in one place instead of trawling through your code

## Modifying res/values/strings.xml
**strings.xml** is where you place string constrants used throughout the app, e.g.
- Name of app and activities
- Text of buttons or other widgets
- Messages in Toasts

Might look like
```xml
<string name="app_name">Exchange Rate </string>  
<string name="action_settings">Settings</string>  
<string name="set_exchange_rate">Set Exchange Rate</string>  
<string name="main_activity_name">Convert Currency</string>
```
As you code your app, you are free to modify or add to this list.
An example of how constants are accessed by the **R** class is
**R.string.set_exchange_rate** (note how string is spelt)

## Google cont.

Resource files are a way of separating static values from code so that you don't have to change the code itself to change the values. You can store all the strings, layouts, dimensions, colors, styles, and menu text separately in resource files.

Resource files are stored in folders located in the `res` folder when viewing the Project > Android pane. These folders include:
-   `drawable`: For images and icons
-   `layout`: For layout resource files
-   `menu`: For menu items
-   `mipmap`: For pre-calculated, optimized collections of app icons used by the Launcher
-   `values`: For colors, dimensions, strings, and styles (theme attributes)

The syntax to reference a resource in an XML layout is as follows:

`@`_package_name_`:`_resource_type_`/`_resource_name_

-   _package_name_ is the name of the package in which the resource is located. The package name is not required when you reference resources that are stored in the `res` folder of your project, because these resources are from the same package.
-   _resource_type_ is the `R` subclass for the resource type. See [Resource Types](https://developer.android.com/guide/topics/resources/available-resources.html) for more about the resource types and how to reference them.
-   _resource_name_ is either the resource filename without the extension, or the `android:name` attribute value in the XML element.

For example, the following XML layout statement sets the `android:text` attribute to a `string` resource:
```xml
android:text="@string/button_label_toast"
```
-   No _package_name_ is included, because the resource is stored in the `strings.xml` file in the project.
-   The _resource_type_ is `string`.
-   The _resource_name_ is `button_label_toast.`

Another example: this XML layout statement sets the `android:background` attribute to a `color` resource, and since the resource is defined in the project (in the `colors.xml` file), the _package_name_ is not specified:
```xml
android:background="@color/colorPrimary"
```
In the following example, the XML layout statement sets the `android:textColor` attribute to a `color` resource. However, the resource is not defined in the project but supplied by Android, so you need to specify the _package_name_, which is `android`, followed by a colon:
```xml
android:textColor="@android:color/white"
```
**Tip**: For more about accessing resources from code, see [Accessing Resources](http://developer.android.com/guide/topics/resources/accessing-resources.html). For Android color constants, see the [Android standard R.color resources](http://developer.android.com/reference/android/R.color.html).

### Values resource files
Keeping values such as strings and colors in separate resource files makes it easier to manage them, especially if you use them more than once in your layouts.

For example, it is essential to keep strings in a separate resource file for translating and localizing your app, so that you can create a string resource file for each language without changing your code. Resource files for images, colors, dimensions, and other attributes are handy for developing an app for different device screen sizes and orientations.

### Strings
String resources are located in the `strings.xml` file (inside **res > values** in the **Project > Android** pane). You can edit this file directly by opening it in the editor pane:

```xml
<resources>
    <string name="app_name">Hello Toast</string>
    <string name="button_label_count">Count</string>
    <string name="button_label_toast">Toast</string>
    <string name="count_initial_value">0</string>
</resources>
```

The `name` (for example, `button_label_count`) is the resource name you use in your XML code, as in the following attribute:
```xml
android:text="@string/button_label_count"
```
The string value of this `name` is the word (`Count`) enclosed within the `<string></string>` tags. (You don't use quotation marks unless the quotation marks are part of the string value.)

### Extracting strings to resources
You should also _extract_ hard-coded strings in an XML layout file to string resources.![ Extracting a string resource](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_extract_string_resources.png " Extracting a string resource")

![ Naming the string resource](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_extract_string_resources2.png " Naming the string resource")

To extract a hard-coded string in an XML layout, follow these steps, as shown in the figure above:
1.  Click the hard-coded string and press **Alt-Enter** in Windows, or **Option-Return** in Mac OS X.
2.  Select **Extract string resource**.
3.  Edit the **Resource name** for the string value.

You can then use the resource name in your XML code. Use the expression `"@string/resource_name"` (including quotation marks) to refer to the string resource:
```xml
android:text="@string/button_label_count"
```

### Colors
Color resources are located in the `colors.xml` file (inside **res > values** in the **Project > Android** pane). You can edit this file directly in the editor pane:
```xml
<resources>
    <color name="colorPrimary">#3F51B5</color>
    <color name="colorPrimaryDark">#303F9F</color>
    <color name="colorAccent">#FF4081</color>
    <color name="myBackgroundColor">#FFF043</color>
</resources>
```

The `name` (for example, `colorPrimary`) is the resource name you use in your XML code:
```xml
android:textColor="@color/colorPrimary"
```

The color value of this `name` is the hexadecimal color value (`#3F51B5`) enclosed within the `<color></color>` tags. The hexadecimal value specifies red, green, and blue (RGB) values. The value always begins with a pound (`#`) character, followed by the Alpha-Red-Green-Blue information. For example, the hexadecimal value for black is #000000, while the hexadecimal value for a variant of sky blue is #559fe3. Base color values are listed in the [Color](https://developer.android.com/reference/android/graphics/Color.html) class documentation.

The `colorPrimary` color is one of the predefined base colors and is used for the app bar. In a production app, you could, for example, customize this to fit your brand. Using the base colors for other UI elements creates a uniform UI.

**Tip**: For the Material Design specification for Android colors, see [Style](https://material.google.com/style/color.html#) and [Using the Material Theme](https://developer.android.com/training/material/theme.html). For common color hexadecimal values, see [Color Hex Color Codes](http://www.color-hex.com/). For Android color constants, see the [Android standard R.color resources](http://developer.android.com/reference/android/R.color.html).

You can see a small block of the color choice in the left margin next to the color resource declaration in `colors.xml`, and also in the left margin next to the attribute that uses the resource name in the layout XML file.![ Color blocks in the resource file](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_color_block_in_colors_xml.png " Color blocks in the resource file")

![ Color block in the layout file](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-2-c-layouts-and-resources-for-the-ui/as_color_block_in_layout.png " Color block in the layout file")

**Tip**: To see the color in a popup, turn on the Autopopup documentation feature. Select **Preferences > Editor > General > Code Completion**, and select the "Autopopup documentation in (ms)" option. You can then hover your cursor over a color resource name to see the color.

### Dimensions
To make dimensions easier to manage, you should separate the dimensions from your code, especially if you need to adjust your layout for devices with different screen densities. Keeping dimensions separate from code also makes it easy to have consistent sizing for UI elements, and to change the size of multiple elements by changing one dimension resource.

Dimension resources are located in the `dimens.xml` file (inside **res > values** in the **Project > Android** pane). The `dimens.xml` file can actually be a folder holding more than one `dimens.xml` file—one for each device screen resolution. You can edit each `dimens.xml` file directly:
```xml
<resources>
    <!-- Default screen margins, per the Android Design guidelines. -->
    <dimen name="activity_horizontal_margin">16dp</dimen>
    <dimen name="activity_vertical_margin">16dp</dimen>
    <dimen name="my_view_width">300dp</dimen>
    <dimen name="count_text_size">200sp</dimen>
    <dimen name="counter_height">300dp</dimen>
</resources>
```

The `name` (for example, `activity_horizontal_margin`) is the resource name you use in the XML code:
```xml
android:paddingLeft="@dimen/activity_horizontal_margin"
```
The value of this `name` is the measurement (`16dp`) enclosed within the `<dimen></dimen>` tags.

You can extract dimensions in the same way as strings:
1.  Click the hard-coded dimension, and press **Alt-Enter** in Windows, or press **Option-Return** in Mac OS X.
2.  Select **Extract dimension resource**.
3.  Edit the **Resource name** for the dimension value.

[Density-independent pixels](https://developer.android.com/training/multiscreen/screendensities.html) (`dp`) are independent of screen resolution. For example, `10px` (10 fixed pixels) look a lot smaller on a higher resolution screen, but Android scales 1`0dp` (10 device-independent pixels) to look right on different resolution screens. Text sizes can also be set to look right on different resolution screens using _scaled-pixel_ (`sp`) sizes.

**Tip**: For more information about `dp` and `sp` units, see [Supporting Different Densities](http://developer.android.com/training/multiscreen/screendensities.html).

### Styles
A style is a resource that specifies common attributes such as height, padding, font color, font size, background color. Styles are meant for attributes that modify the look of the view.

Styles are defined in the `styles.xml` file (inside **res > values** in the **Project > Android** pane). You can edit this file directly. Styles are covered in a later chapter, along with the Material Design Specification.

### Other resource files
Android Studio defines other resources that are covered in other chapters:
-   Images and icons: The `drawable` folder provides icon and image resources. If your app does not have a `drawable` folder, you can manually create it inside the `res` folder. For more information about drawable resources, see [Drawable Resources](https://developer.android.com/guide/topics/resources/drawable-resource.html) in the App Resources section of the Android Developer's Guide.
-   Optimized icons: The `mipmap` folder typically contains pre-calculated, optimized collections of app icons used by the Launcher. Expand the folder to see that versions of icons are stored as resources for different screen densities.
-   Menus: You can use an XML resource file to define menu items and store them in your project in the `menu` folder. Menus are described in a later chapter.