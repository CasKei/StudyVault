---
tags: #50.001
---
[[IS & Programming|ISP]]

# Lesson 2 - Exchange Rate App
## Objectives
- Describe the *static factory method* and *builder design pattern* in java
- Use `BigDecimal` class for financial calculations
- From an `EditText` widget, extact data and specify input settings
- Use the logcat to display messages to track the behaviour of an app
- Describe what a Toast is and write code to display toasts
- Explain what is *Explicit Intent* and write code to implement it
- Explain what is *Implicit Intent* and write code to implement it
- Modify the [[Android Manifest]] to change the app name and to specify a parent activity
- Describe the android activity life cycle
- Describe and modify the code needed for an Options Menu
- Save app data uing the `SharedPreferences` class
- Explain the purpose of Unit Testing and write code for unit tests using the JUnit framework

## Introduction
In this series of lessons, we will build an app that is handy for travelling. I often travel with people who want to know exactly how much an item would cost in their home currency.

## Design and Structure of the app
The diagram (which is overly simplified) below shows how the classes interact with each other. This shows how each file has its own responsibilities.
![[Pasted image 20220321121926.png]]
The calculation of an exchange rate could be easily integrated into `MainActivity.java`.  

However, I choose to encapsulate it in another class because of the  
**Single Responsibility Principle** - A class should have only one reason to change.  

Hence, applying this principle leads me to separate the job of calculating the exchange rate, from the job of interacting with the UI.

## Get Ready
Download starter code and open.
How many activities does the app contain? 2
How many activities can you see in the app currently? 1

## Java/Android to know

[[BigDecimal]]
[[Resource files]]/values folder
[[Android Manifest]]
[[EditText widget]]
[[Refactoring]]
[[Exception - Android]]
[[Static factory method]]
[[Toast]]
[[Logcat]]
[[Intents]]
[[Android Activity Lifecycle]]
[[Data persistence]]
[[Options Menu]]
[[Builder design pattern]] 
[[W5|design pattern]]
[[Universal Resource Identifier]]
[[Unit testing]]
Not tested:
[[Instrumented testing]]