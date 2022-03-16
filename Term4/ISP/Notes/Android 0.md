---
tags: #50.001
---
[[IS & Programming|ISP]]

# Objectives
Ensure you have the necessary tools to build android apps.
Introduction to the components and coding necessary for an android app.

# Setup a "Hello World" app
## Create a "Hello World" app
### Start a new android studio project
Launch android studio and select **Start a New Android Studio Project**
### Start with an Activity
The android [documentation](https://developer.android.com/reference/android/app/Activity) defines an **Activity** as:
> An activity is a single, focused thing that the user can do

In other words, it is a screen where the UI resides on, for the user to interact with.
Make sure **Empty Activity** is selected, as it is the option with the least amount of code. Other options come pre-loaded with some features, and are useful when you are more familiar with android app programming.
### Give you project a name
Give your project an **Application name** and state where you want it to be saved in the **Project location**.
- Select **Java** as the language
- Ensure the **Use androidx,\*artifacts** box is checked.
- The **API level** is the version of the Android OS. As of Nov 2019, latest API level is 29, but it is safe to leave it as 15 as default.

### Examine the User Interface
#### Different views
Should be in **Android view**.
There are 2 folders [[#app]] and [[#res]].

When an **activity** is created, you get 2 files:
- an `xml` file named `activity_main.xml`
- a java class in a file named `MainActivity.java`

The `xml` file specifies the user interface layout and the java class is where you write code to provide interactivity to your UI.

#### app
Contains the java code.
`MainActivity.java` is found in the package founder within the java folder.

#### res
Contains resources for the app.
This includes xml files, images and icons.
Expand the res folder and look for `activity_main.xml` file under the *layout* subfolder.

#### Config
Ensure that **APP** is shown without a red cross. If you do not see this, you may have a buggy installation and the first thing you could try is to update your installation.
Windows: Help -> Check for Updates

#### Available emulators
Available emulators are shown here.
If your android phone is connected, you will see it here as will.
If you see "missing system image" then you need to install the emulator for the device that you are interested in.
If you don't, the emulator has been installed.

#### Run button
Once you have an android phone connected or an emulator ready, you press this button to deploy your app.

### Test your app
It is recommended to get an android phone.
Enable USB debugging mode. [Instructions](https://developer.android.com/studio/run/device).
Connect your phone to the device and you should see i at the [[#Available emulators]].
Then press the run button to see your app appear.

[1.1 - Introduction to Android](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-1-build-your-first-app/1-0-c-introduction-to-android/1-0-c-introduction-to-android.html)
[1.1 - Your first Android app](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-1-build-your-first-app/1-1-c-your-first-android-app/1-1-c-your-first-android-app.html)

## Summary (dev android tutorial)
- To see the app's Android hierarchy in the Project pane, click the **Project** tab in the vertical tab column, and then choose **Android** in the popup menu at the top.
- Edit the `build.gradle(Module:app)` file when you need to add new libraries to your project or change library versions.
- All code and resources for the app are located in the `app` and `res` folders. The `java` folder includes activities, tests, and other components in Java source code. The `res` folder holds resources, such as layouts, strings, and images.
- Edit the `AndroidManifest.xml` file to add feature components and permissions to your Android app. All components for an app, such as multiple activities, must be declared in this XML file.
- Use the AVD manager to create a emulator for your app
- Add `Log` statements to your app, which display messages in the Logcat pane as a basic tool for debugging
- To run your app on a physical Android device, turn on USB Debugging on the device. Open **Settings > About phone** and tap **Build number** 7 times. Return to the previous screen (**Settings**), and tap **Developer Options**. Choose **USB Debugging**.
# Make one simple modification
Change the xml tag in xml file from `<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android">`
to
`<LinearLayout>`

# Further reading
[[XML Syntax]]
[Documentation on Linear Layout](https://developer.android.com/guide/topics/ui/layout/linear)
[[Linear Layout]]
