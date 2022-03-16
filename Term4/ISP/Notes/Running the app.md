---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

With virtual device emulators, you can test an app on different devices such as tablets or smartphones—with different API levels for different Android versions—to make sure it looks good and works for most users. You don't have to depend on having a physical device available for app development.

The [Android Virtual Device (AVD) manager](http://developer.android.com/tools/devices/managing-avds.html) creates a virtual device or emulator that simulates the configuration for a particular type of Android-powered device. Use the AVD Manager to define the hardware characteristics of a device and its API level, and to save it as a virtual device configuration. When you start the Android emulator, it reads a specified configuration and creates an emulated device on your computer that behaves exactly like a physical version of that device.

## Creating a virtual device
To run an emulator on your computer, use the AVD Manager to create a configuration that describes the virtual device. Select **Tools > Android > AVD Manager**, or click the **AVD Manager** icon ![ AVD Manager icon](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-1-c-your-first-android-app/ic_avd_manager.png " AVD Manager icon") in the toolbar.

The **Your Virtual Devices** screen appears showing all of the virtual devices created previously. Click the **+Create Virtual Device** button to create a new virtual device.

You can select a device from a list of predefined hardware devices. For each device, the table provides a column for its diagonal display size (**Size**), screen resolution in pixels (**Resolution**), and pixel density (**Density**). For example, the pixel density of the Nexus 5 device is `xxhdpi`, which means the app uses the icons in the `xxhdpi` folder of the `mipmap` folder. Likewise, the app uses layouts and drawables from folders defined for that density.

After you click **Next**, the **System Image** screen appears for choosing the version of the Android system for the device. The **Recommended** tab shows the recommended systems for the device. More versions are available under the **x86 Images** and **Other Images** tabs. If a **Download** link is visible next to a system image version, it is not installed yet. Click the link to start the download, and click **Finish** when it's done.

## Running the app on the virtual device

To run the app on the virtual device you created in the previous section, follow these steps:
1.  In Android Studio, select **Run > Run app** or click the ![ Android Studio Run icon](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-1-c-your-first-android-app/ic_run.png " Android Studio Run icon") **Run icon** in the toolbar.
    
2.  In the Select Deployment Target window, under Available Emulators, select the virtual device you created, and click **OK**.
    
The emulator starts and boots just like a physical device. Depending on the speed of your computer, the startup process might take a while. The app builds, and once the emulator is ready, Android Studio uploads the app to the emulator and runs it.

You should see the app created from the Empty Activity template ("Hello World") as shown in the following figure, which also shows Android Studio's **Run** pane that displays the actions performed to run the app on the emulator.

**Tip**: When testing on a virtual device, it is a good practice to start it up once, at the very beginning of your session. Do not close it until you are done testing your app, so that your app doesn't have to go through the device startup process again. To close the virtual device, select **Quit** from the menu or press **Control-Q** in Windows or **Command-Q** in macOS.

The figure above shows the emulator and the run log:
1.  The Emulator running the app.
2.  The **Run** pane, which shows the actions taken to install and run the app.
3.  The **Run** tab, which you click to open or close the **Run** pane.

## Running the app on a physical device
Always test your apps on a physical device. While emulators are useful, they can't show all possible device states, such as what happens if an incoming call occurs while the app is running. To run the app on a physical device, you need the following:
-   An Android-powered device such as a phone or tablet.
-   A data cable to connect your Android-powered device to your computer via the USB port.
-   If you are using a Linux or Windows system, you may need to perform additional steps to run on a hardware device. Check the [Using Hardware Devices](http://developer.android.com/tools/device.html) documentation. You may also need to install the appropriate USB driver for your device. See [OEM USB Drivers](http://developer.android.com/tools/extras/oem-usb.html).

To let Android Studio communicate with your Android-powered device, you must turn on USB Debugging on the device. You enable USB Debugging in the device's **Developer options** settings. (Note that enabling USB Debugging is not the same as rooting your device.)

On Android 4.2 and higher, the **Developer options** screen is hidden by default. To show developer options and enable USB Debugging:

1.  On your device, open **Settings > About phone** and tap **Build number** seven times.
2.  Return to the previous screen (**Settings**). **Developer options** appears at the bottom of the list. Tap **Developer options**.
3.  Select **USB Debugging**.
4.  Connect the device and run the app from Android Studio.