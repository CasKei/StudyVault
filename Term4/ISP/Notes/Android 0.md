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
# Make one simple modification


# Quiz


# Read about XML