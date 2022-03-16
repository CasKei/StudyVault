---
tags: #50.001, button, widget, TextView
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

## Explaining the XML Layout File
[[The layout editor]]

### [[Linear Layout]]
Edit the XML file generated for you by replacing `ConstraintLayout` with `LinearLayout`.
In LinearLayout:
- Widgets are stacked in sequence according to orientation
- Two possible orientations: **horizontal** and **vertical**
- If no orientation attribute is specified, the default orientationis horizontal.

```xml
<LinearLayout
	android:orientation = "vertical"
>
```
```xml
<LinearLayout
	android:orientation = "horizontal"
>
```

## [[TextView]] Widget
Basic widget:
```xml
<TextView
	android:id="@+id/myTextView"
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:layout_gravity="center"
	android:gravity="end"
	android:text="second"/>
```
- **id attribute** enables you to give a unique ID to each widget in the XML layout file. Allows you to access the widget through the java code
- **text attribute** specifies the text that the widget should contain

## Button Widget
Basic widget:
```xml
<Button
	android:id="@+id/myButton"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:text="Click Me"/>

```
Some attributes are removed, this is the minimum necessary to specify a widget.

`Button` is a sub-class of `TextView`.

[Button Doc](https://developer.android.com/reference/android/widget/Button)

## Sizing a widget
For **layout_width** and **layout_height** attributes:
- **wrap_content**: widget fits content
- **match_parent**: widget fits screen size
```xml
<TextView
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:text="AA"/>
<TextView
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:text="AA"/>
```

## Alignment
Note the difference between the two: 
- To align a widget **within a layout**, use the **`layout_gravity`** attribute (*child to parent*)
	- `android:layout_gravity="center"`
- To align the contents of a widget **within itself**, use the **`gravity`** attribute (*parent to child*)
	- `android:gravity="center"`

`gravity` will have no effect when: layout wrap content\
`layout_gravity` will have no effect when: layout match parent

## Random Class
In many applications it is useful to generate random numbers. 

In Java, you do it by getting an instance of the Random class. In this class there are three useful methods
- **`nextInt()`** gives you an integer between $-2^{32}$ and $2^{32}$ (exclusive) 
- **`nextInt(n)`** gives you an integer between $0$ and $n$ (exclusive)
- **`nextDouble()`** gives you a double between $0.0$ and $1.0$

```java
Random r = new Random(); 
r.nextInt(); 
r.nextInt(100); 
r.nextDouble();
```

Random number generators usually need to be initialized with a seed. \
If you need the sequence of random numbers to be the same, you use the same seed. \
If not, one way to get a changing seed is to use the `Date` object.

```java
Date d = new Date(); 
Random r = new Random(d.getTime());
```

## Nested Classes
A class definition can contain class definitions. We call these classes nested classes

```java
public class OuterClass {
	// code not shown 
	class InnerClass{
	 //code not shown 
	} 
}
```
This is typically done when you have classes that logically depend on the outer class and are used together with the outer class.

## Inner Class
A nested class that is not declared static is called an **Inner Class**. 
- To instantiate an inner class, you need an instance of the outer class, which is usually called the **enclosing class**. 
- The inner class can access all methods and variables of the enclosing outer class.

```java
public class OuterClass {
	int a;
	OuterClass() { a = 10; }
	void outerPrintA() { System.out.println(a); }

	class InnerClass {
		int c;
		InnerClass() { c = 100; }
		void innerPrintA() { System.out.println(a); }
		OuterClass giveBackOuter() { return OuterClass.this; }
	}
}
```
==Activity==. For **OuterClass**, complete the main function below to illustrate the following properties.
```java
public class TestOuterClass {
	public static void main(String[] args) {
		// Instantiate OuterClass
		OuterClass outerClass = new OuterClass();
		//Instantiate InnerClass
		OuterClass.InnerClass innerClass = outerClass.new InnerClass();

		// Show that InnerClass can access variables in OuterClass
		
		// Show that InnerClass stores a reference to OuterClass
	
	}
}
```

## [[Week 2 - Instance and static variables or methods|Static]] Nested Classes
By declaring a [[#Nested Classes|nested class]] as static, it is known as **static nested class**.
- It can only access static variables and methods in the outer class
- It can only be instantiated without an instance of the outer class

A static nested class behaves like a top-level class and is a way to organise classes that are used only by some other classes.

==Activity==
- Modify **`OuterClass.java`** by declaring **`InnerClass`** as static and adjusting other parts of the class accordingly e.g. which other variables must be static? Which methods do not work anymore?
- Write code to show that you can instantiate **`OuterClass`** and **`InnerClass`** separately.

## Nested [[Interfaces]] & Anonymous Classes
Recall that [[Interfaces]] makes your code reusable. We may nest interfaces as well.\
Recall also that interfaces are inherently [[Week 2 - Instance and static variables or methods|static]].\
In the following code, any object that implements **Foo.Bar** interface can be passed to **thirsty()**.
```java
public class Foo {
	interface Bar {
		void drink();
	}

	Foo() {
	}

	void thirsty(Bar bar) {
		bar.drink();	
	}
}
```

The [[#Inner Class]] **C** implements **Foo.Bar** and an instance is passed to **thirsty()**. The inner class is declared **static** becaise it is invoked from **main()**.
```java
public class TestFoo {

	public static void main(String[] argv) {
		Foo f = new Foo();
		f.thirsty( new C() );
	}

	static class C implements Foo.Bar {
		@Override
		public void drink() {
			System.out.println("gulp");
		}
	}
}
```

## Anonymous Class
Often, if the [[#Inner Class]] is only used once, an laternative is an **Anonymous Inner Class**, to avoid declaring too many classes. You may not want to have too many inner classes that are practically only used once.\
The following code shows how the **TestFoo** example above can be implemented using an anonymous inner class.
```java
public class TestFool {
	public static void main(String[] argv){
		Foo f = new Foo();
		f.thirsty( new Foo.Bar(){
			@Override
			public void drink() {
				System.out.println("Gulp");
			}
		});
	}
}
```
The **new** keyword is used to instantiate an object that implements **Foo.bar**. Because **Foo.Bar** is an interface, the implementation os then specified immediately.

As you can see, we have an **anonymous class** because
- We do not name the class that implements the [[Interfaces|interface]]
- We do not assign a variable name to the class that implements the interface

*We see nested interfaces, nester static classes and anonymous classes in Android programming frequently.*

## Delegation
We go back to the **Foo** class and notice that what happens when **thirsty()** is executed depends on objects implementing the **Foo.Bar** that are passed to it.

In other words, the behaviour of **thirsty()** is ***delegated*** to objects that implement **Foo.Bar**.

This illustrates 2 design principles:
- **Program to a supertype**
	- Because the input to *thirsty()* is an interface, it can accept any object that implements **Foo.Bar**
- **Favour composition over [[Inheritance]]
	- Since *thirsty()* can accept any object that implements **Foo.Bar**, the objects of the **Foo** class become more flexible and its behaviour can change at runtime.

```java
public class Foo {
	interface Bar{
		void drink();
	}

	Foo() {
	}

	void thirsty(Bar bar) {
		bar.drink();
	}
}
```
## Further Reading
- [Nested classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
- [Anonymous classes doc](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html)
- Bloch, Effective Java, Item 22.

# The Android Programming you Need to Know
## onCreate is called when the Activity is first launched
Within the **MainActivity** class, you would see this code

```java
@Override
protected void onCreate(Bunble savedInstanceState) {
	super.onCreate(savedInstanceState);
	setContentView(R.layout.activity_main);
}
```
The **onCreate** method is called whenever your Activity is first launched e.g. when user clicks your app icon.

This method is part of the methods in the **Android activity life cycle**, which will be discussed in the [[Android 2|next lesson]].

You write code in **onCreate** to implement what you want the user to see when the activity is launched.

## The R class contains resource IDs to the [[Resource files|resources]] in the res folder
When [[Running the app|app]] is compiled, an **R class** is generated that contains IDs to the resources in the **res** folder.

Since **`activity_main.xml`** is stored in the [[The layout editor|layout]] folder, its R class reference is `R.layout.activity_main`.

## In OnCreate, the [[The layout editor|layout]] is first inflated
`R.layout.activity_main` is passed to the `setContentView` method to **inflate the layout**.\
In this process, Android reads to [[Editing XML directly|XML]] code in the layout file and instantiates objects in the memory that represent each of the widgets on the Activity.

## More examples of Resource IDs
### Widget ID
If your widget has the following attribute
```groovy
android:id ="@+id/myWidget"
```
then it can be accessed by `R.id.myWidget`

### Images in drawables
If you have an image stored in the drawable folder named **pikachu.png**, then it can be **R.drawable.pikachu**

***Note that File-based resource names
- ***Must contain only lowercase a-z, 0-9, or underscore
- ***Must start with a letter

==Clicker Question - What type of class is the R class?==
The R class contains [[#Nested Classes]]. T/F?

### Seeing the R class (optional)
**Before Android Studio 3.6**
The R class is generated for you but you may view it in your project as follows:
- Change to Project View
- Access the folder path: `app/build/generated/source/r/debug/<your.package.name>`

In general, we don't actually have to do anything to this file.

**Android Studio 3.6 and later**
The R class is generated and directly compiled into bytecodes. We can't see it unless we decompile `R.jar`

## Use findViewById() method to assign a widget to a variable
If a widget has an id attribute `myTextView`, then the corresponding reference in the R class is `R.id.myTextView`.

This reference is then passed to `findViewById()`, which returns a reference to the widget.\
This can then be assigned to a variable. A sample code is as follows.
```java
TextView textView = findViewById(R.id.myTextView);
```
Alt+Enter to import the necessary library.

## Use the dot operator to see  what methods are available for that widget
Once you have a variable, use the dot operator to see what methods are avaliable, you can see that the `setText` method is an [[Method Overloading & Overriding|overloaded]] method, it can take in another resource ID or another character array.
![[Pasted image 20220311223625.png]]

## Control a widget's properties in Java
Some methods, like the `setText` method, enable you to control a widget's properties programmatically in Java.\
For example:
```java
textView.setText("My New String")
```
This action thus replaces what is written in the [[Editing XML directly|XML layout file]].

## setOnClickListener()
When a [[Views|View]] object is clicked, what happens next is specified by calling `setOnClickListener()`

Typically, we want `Button` to be clicked, but it is also possible to have other widgets clicked, including [[TextView]], [[Linear Layout]], etc.

The input to `setOnClickListener` is an object of a class that implements the `View.OnClickListener` [[Interfaces|interface]]. There is one method to implement, called `onClick`. You may implement this in several ways, here 3 ways are listed.

**1. As a [[#Inner Class]] in `MainActivity`**.
This method shows you clearly what you are doing. But it may cause your `MainActivity.java` to become bloated with inner classes that you only use once.
```java
public class MainActivity extends AppCompaActivity {
	Button button;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		button = findViewById(R.id.myButton1);
		button.setOnClickListener( new ClickMe() );
	}
	// this is an inner class
	class ClickMe implements View.OnClickListener{
		@Override
		public void onClick(View v) {
			// code...
		}
	}
}
```

**2. (Recommended) As an [[#Anonymous Class]] that is defined in the input to `setOnClickListener()`**.
This is recommended because it is used very frequently, and in many other situations.
```java
public class MainActivity extends AppCompatActivity {

	Button button;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
			
		button = findViewById(R.id.myButton1);

		button.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				//code...
			}	
		});
	}
}
```

**3. Define an instance method in `MainActivity` specifying what is to be done. Then specify it as an attribute in the widget.**
Although it looks straightforward and easy, I don't recommend this choice, for the following reasons.
- Many code examples used in teaching android use [[#Anonymous Class]] instead
- This does not work in many other situatoins.

Define an instance method in `MainActivity` with any name you like and the following signature.
```java
public class MainActivity extends AppCompatActivity {

	Button button;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		button = findViewById(R.id.myButton1);)
	}
	// this method is what myButton1 will do
	public void whenClick(View view) {
		// code...
	}
}
```

Then in the XML file, the button widget will have the `onClick` attribute.
```xml
<Button
	android:id="@+id/myButton1"
	android:layout_width="match_parent"
	android:layout_height="wrap_content"
	android:onClick="whenClick"
	android:text="Click Me"
/>
```

# Making our App
What it should do:
- Store all images in the res/drawables folder. Put the Image IDs in an [[Week 1 - ArrayList, LinkedList, Generics|ArrayList]]
- When `Button` is clicked, retrieve the image ID from the `ArrayList` in sequence.
- Use the image ID to retrieve the image and place it in the `ImageView` widget

## Code stump for MainActivity.java
Obtain started code from Github.
Has `MainActivity.java` and a folder with some images.
Copy the code below the **package** statement and paste it in the `MainActivity.java` in the project that you generated in Lesson 0 (again, below your own **package** statement). Import any needed classes.