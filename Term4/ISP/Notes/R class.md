---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 1]]

## The R class contains resource IDs to the [[Resource files|resources]] in the res folder
When [[Running the app|app]] is compiled, an **R class** is generated that contains IDs to the resources in the **res** folder.

Since **`activity_main.xml`** is stored in the [[The layout editor|layout]] folder, its R class reference is `R.layout.activity_main`.

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
The R class contains [[Nested class]]. T/F?

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

