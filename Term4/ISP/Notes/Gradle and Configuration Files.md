---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 4]]

[[Understanding the build process]]

Gradle is the software component that manages the build process for an android app.
The build process begins from source code and ends with the APK file.
The APK file can then be installed on any Android phone.

You may get the APK file in Android Studio using
**Build -> Build APK(s)**

More information on the build process here:  
https://developer.android.com/studio/build/

Settings for the build process are stored in 2 build.gradle files:
- project-level file
- module-level file

## Gradle module-level settings
Often the project level default settings are sufficient. Hence we usually have to modify the module-level settings only.

The first part shows information such as
- Minimum API level
- Compile API level
- Target API level

You may adjust these if you are aiming for certain API levels.

The next part shows the dependencies that your app has.
If you are upgrading the compileSdkVersion, your IDE might recommend you to upgrade the dependencies accordingly. Please use the [[Refactoring|refactor]] option.

