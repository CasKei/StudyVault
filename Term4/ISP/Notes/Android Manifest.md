---
aliases:
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

Before the Android system can start an app component such as an `Activity`, the system must know that the `Activity` exists. It does so by reading the app's `AndroidManifest.xml` file, which describes all of the components of your Android app. Each `Activity` must be listed in this XML file, along with all components for the app.

To view and edit the `AndroidManifest.xml` file, expand the `manifests` folder in the **Project > Android** pane, and double-click `AndroidManifest.xml`. Its contents appear in the editing pane:
```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.helloworld">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
               <action android:name="android.intent.action.MAIN" />

               <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
```

## Android namespace and application tag
The Android Manifest is coded in [[XML Syntax|XML]] and always uses the Android namespace:
```xml
xmlns:android="http://schemas.android.com/apk/res/android"
   package="com.example.android.helloworld">
```
The `package` expression shows the unique package name of the new app. Do not change the package expression after the app is published.

The `<application>` tag, with its closing `</application>` tag, defines the manifest settings for the entire app.

## Automatic backup
The `android:allowBackup` attribute enables automatic app data backup:
```xml
android:allowBackup="true"
```
Setting the `android:allowBackup` attribute to `true` enables the app to be backed up automatically and restored as needed. Users invest time and effort to configure apps. Switching to a new device can cancel out all that careful configuration. The system performs this automatic backup for nearly all app data by default, and does so without the developer having to write any additional app code.

For apps whose target SDK version is Android 6.0 (API level 23) and higher, devices running Android 6.0 and higher automatically create backups of app data to the cloud because the `android:allowBackup` attribute defaults to `true` if omitted. For apps < API level 22 you have to explicitly add the `android:allowBackup` attribute and set it to `true`.

**Tip**: To learn more about the automatic backup for apps, see [Configuring Auto Backup for Apps](https://developer.android.com/training/backup/autosyncapi.html).

## The app icon
The `android:icon` attribute sets the icon for the app:

```xml
android:allowBackup="true"
android:icon="@mipmap/ic_launcher"
```

The `android:icon` attribute assigns to the app an icon in the `mipmap` folder (inside the `res` folder in the **Project > Android** pane). The icon appears on the home screen or in the Search Apps screen for launching the app. The icon is also used as the default icon for app components.

## App label and string resources
The `android:label` attribute shows the string `"Hello World"` highlighted. If you click the string, it changes to show the string resource `@string/app_name`:

```
android:label="@string/app_name"
```

**Tip**: To see the context menu, ctrl-click or right-click `app_name` in the editor pane. Select **Go To > Declaration** to see where the string resource is declared: in the `strings.xml` file. When you select **Go To > Declaration** or open the file by double-clicking `strings.xml` inside the `values` folder in the **Project > Android** pane, the file's contents appear in the editor pane.

After opening the `strings.xml` file, you can see that the string name `app_name` is set to `Hello World`. You can change the app name by changing the `Hello World` string to something else. String resources are described in a separate lesson.

## App theme
The `android:theme` attribute sets the app's theme, which defines the appearance of UI elements such as text:

```
android:theme="@style/AppTheme">
```

The `theme` attribute is set to the standard theme `AppTheme`. Themes are described in a separate lesson.

## Declaring the Android version
Different devices may run different versions of the Android system, such as Android 4.0 or Android 4.4. Each successive version can add new APIs not available in the previous version. To indicate which set of APIs are available, each version specifies an API level. For instance, Android 1.0 is API level 1 and Android 4.4 is API level 19.

The API level allows a developer to declare the minimum version with which the app is compatible, using the `<uses-sdk>` manifest tag and its `minSdkVersion` attribute. For example, the Calendar Provider APIs were added in Android 4.0 (API level 14). If your app can't function without these APIs, declare API level 14 as the app's minimum supported version like this:
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android.helloworld">
    <uses-sdk android:minSdkVersion="14" android:targetSdkVersion="19" />
    // ... Rest of manifest information
</manifest>
```
The `minSdkVersion` attribute declares the minimum version for the app, and the `targetSdkVersion` attribute declares the highest (newest) version which has been optimized within the app. Each successive version of Android provides compatibility for apps that were built using the APIs from previous versions, so the app should _always_ be compatible with future versions of Android while using the documented Android APIs.

The `targetSdkVersion` attribute does _not_ prevent an app from being installed on Android versions that are higher (newer) than the specified value. Even so, the target attribute is important, because it indicates to the system whether the app should inherit behavior changes in newer versions.

If you don't update the `targetSdkVersion` to the latest version, the system assumes that your app requires backward-compatible behaviors when it runs on the latest version. For example, among the behavior changes in Android 4.4, alarms created with the `AlarmManager` APIs are now inexact by default so that the system can batch app alarms and preserve system power. If your target API level is lower than `"19"`, the system retains the previous API's behavior for your app.