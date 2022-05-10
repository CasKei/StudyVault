---
tags: 50.001
---
[[IS & Programming|ISP]]

## Lesson 4.1 - Pokedex
## Objectives
- Calling [[Intents|intent]]s using `startActivityForResult()` in android
- Implement a [[RecyclerView]]
- Describe the use of static nested classes
- Describe Delegation and Strategy Design Pattern
- Describe Adapter Design Pattern

## Recall
[[Android 2]]
[[Android 3]]

## Java/Android to know
[[Static Nested Classes]]
[[Singleton design pattern]]
[[Static inner classes to model data]]
[[startActivityForResult]]
[[Gradle and Configuration Files]]
[[W5|design pattern]]
[[Strategy design pattern]]
[[Adapter design pattern]]
[[RecyclerView]]

[[Ways of storing data]]

[[Getting each item to respond to clicks]]

[[Swiping to delete]]

## Building the app
First build a [[RecyclerView]] using images in drawables.
With this, we are not able to add images to the [[RecyclerView]]

Then add images to the [[RecyclerView]] by using images selected from the camera gallery. Information is stored in the app's internal file storage.

MainActivity shows the [[RecyclerView]], ImageView, and a FloatingActionButton.

ImageView is used to display the newest image added to the RecyclerView.
When button clicked, brings user to DataEntryActivity, where user can enter name of image, and select an image from gallery by clicking select image button.

![[Pasted image 20220502213958.png]]