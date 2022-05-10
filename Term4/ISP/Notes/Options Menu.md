---
aliases: 
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Options Menu
When you start a new Android Studio project, one option is the **Basic Activity** template.
In this template, code for the following UI elements are automatically provided:
- Options menu
- Floating Action Bar [[Android 4]]

The Options menu is a one-stop location for your user to navigate between the activities of the app.

You should see some additional xml tags in the xml files that specify your layout.\
You should see the following lines of code in your `MainActivity.java`:
In `onCreate()`, this makes the toolbar containing the options menu appear. Don't delete.
```java
Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
setSupportActionBar(toolbar);
```
The `onCreateOptionsMenu()` method is added to inflate the menu layout and make it appear in the toolbar. Usually you do not add code to this method. The xml file is found in **res/menu/menu_main.xml**

The `onOptionsItemSelected()` method is also added. This is where you need to add code to specify what happens when each menu item is clicked. You do this after modifying **menu_main.xml**

## Steps in customising options menu
- Add your menu items here in **res/menu/menu_main.xml** and remember to give each item a unique ID
- Modify `onOptionsItemSelected()` to specify what happens when each menu item is clicked. Very often, you will need to write an [[Intents|intent]] to bring your user to the other activities in your app.