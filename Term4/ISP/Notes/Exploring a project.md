---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

![[Pasted image 20220311122413.png]]
1.  Toolbar: Provides a wide range of actions, including running the Android app and launching Android tools.
2.  Navigation bar: Navigate through the project and open files for editing.
3.  **Project** pane: Displays project files in a hierarchy. The selected hierarchy in the figure above is **Android**.
4.  Editor: The contents of a selected file in the project. For example, after you select a layout (as shown in the figure above), the editor pane shows the layout editor with tools to edit the layout. After you select a Java code file, the editor pane shows the Java code with tools for editing the code.
5.  Tabs along the left, right, and bottom of the window: You can click tabs to open other panes, such as **Logcat** to open the **Logcat** pane with log messages, or **TODO** to manage tasks.

## Gradle files
When you first create an app project, the **Project > Android** pane appears with the `Gradle Scripts` folder expanded as shown below. If the `Gradle Scripts` folder is not expanded, click the triangle to expand it. This folder contains all the files needed by the build system.

The `build.gradle(Module:app)` file specifies additional libraries and the module's build configuration. The `Activity` template that you select creates this file. The file includes the `minSdkVersion` attribute that declares the minimum version for the app, and the `targetSdkVersion` attribute that declares the highest (newest) version for which the app has been optimized.

This file also includes a list of _dependencies_, which are libraries required by the code—such as the `AppCompat` library for supporting a wide range of Android versions.

## App code
To view and edit the Java code, expand the `app` folder, the `java` folder, and the `com.example.android.helloworld` folder. Double-click the `MainActivity` `java` file to open it in the code editor.

The `java` folder includes Java class files. Each [`Activity`](https://developer.android.com/reference/android/app/Activity.html), [`Service`](https://developer.android.com/reference/android/app/Service.html), or other component (such as a [`Fragment`](https://developer.android.com/reference/android/app/Fragment.html)) is defined as a Java class, usually in its own file. Tests and other Java class files are also located here.

The `java` folder contains three subfolders:

-   `com.example.hello.helloworld` (or the domain name you have specified)**:** All the files for a package are in a folder named after the package. For your Hello World app, there is one package, and it contains only `MainActivity.java`. The first `Activity` (screen) that the user sees, which also initializes app-wide resources, is customarily called `MainActivity`. (The file extension is omitted in the **Project > Android** pane.)
-   `com.example.hello.helloworld(androidTest)`: This folder is for your instrumented tests, and starts out with a skeleton test file.
-   `com.example.hello.helloworld(test)`: This folder is for your unit tests and starts out with an automatically created skeleton unit test file.

## Layout files
To view and edit a layout file, expand the `res` folder and the `layout` folder to see the layout file. In the figure below, the layout file is called `activity_main.xml`.

Double-click the file to open it in the layout editor. Layout files are written in XML.

## Resource files
The `res` folder holds resources, such as layouts, strings, and images. An `Activity` is usually associated with a layout of UI views that are defined as an XML file. This XML file is usually named after its `Activity`. The `res` folder includes these subfolders:
-   `drawable`: Store all your app's images in this folder.
-   `layout`: Every `Activity` has at least one XML layout file that describes the UI. For Hello World, this folder contains `activity_main.xml`.
-   `mipmap`: The launcher icons are stored in this folder. There is a subfolder for each supported screen density. Android uses the screen density (the number of pixels per inch) to determine the required image resolution. Android groups all actual screen densities into generalized densities, such as medium (mdpi), high (hdpi), or extra-extra-extra-high (xxxhdpi). The `ic_launcher.png` folder contains the default launcher icons for all the densities supported by your app.
-   `values`: Instead of hardcoding values like strings, dimensions, and colors in your XML and Java files, it is best practice to define them in their respective `values` files. This practice makes it easier to change the values and keep the values consistent across your app.

The `values` subfolder includes these subfolders:
-   `colors.xml`: Shows the default colors for your chosen theme. You can add your own colors or change the colors based on your app's requirements.
-   `dimens.xml`: Store the sizes of views and objects for different resolutions.
-   `strings.xml`: Create resources for all your strings. Doing this makes it easy to translate the strings to other languages.
-   `styles.xml`**:** All the styles for your app and theme go here. Styles help give your app a consistent look for all UI elements.