---
tags: #50.001
---
[[IS & Programming|ISP]]

# Lesson 1 - Random Images
## Objectives
- Modify the [[XML Syntax|XML]] layout file to specify [[Linear Layout]], [[Views#^0d549a|TextView]] and [[Responding to View clicks|Button]] widgets, their [[Editing XML directly|id attributes and layout attributes]]
- Describe nested classes and anonymous classes in java
- Use the instance method `findViewById()`
- Describe the R class in android
- Explain what is meant by inflating the layout
- Write java code in `onCreate()` 
- Write java code to modify the text attribute of a widget
- Write java code to implement a callback

[[Linear Layout]]

## Stuff to know
### Layout
[[The layout editor]]
[[Linear Layout]]
[[TextView]]
[[Button]]
[[Sizing and aligning a widget]]

### Java stuff
[[Random class]]
[[Nested class]]
[[Inner class]]
[[Static Nested Classes]]
[[Nested interface]]

## Further Reading
- [Nested classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
- [Anonymous classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html)
- Bloch, Effective Java, Item 22.

## The Android Programming you Need to Know
[[onCreate]]
[[R class]]

# Making our App
What it should do:
- Store all images in the res/drawables folder. Put the Image IDs in an [[ArrayList, LinkedList, Generics|ArrayList]]
- When `Button` is clicked, retrieve the image ID from the `ArrayList` in sequence.
- Use the image ID to retrieve the image and place it in the `ImageView` widget

## Code stump for MainActivity.java
Obtain started code from Github.
Has `MainActivity.java` and a folder with some images.
Copy the code below the **package** statement and paste it in the `MainActivity.java` in the project that you generated in Lesson 0 (again, below your own **package** statement). Import any needed classes.