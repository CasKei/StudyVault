---
aliases: CardView
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 4]]

## What is a RecyclerView
Suppose you have a collection of similar data e.g.
- images with descriptions
- chat messages with sender's name

And you want to display them in your app.

The `RecyclerView` widget allows the user to scroll through the data.
This is done by loading each data item onto its own item in `RecyclerView`.
A typical display is `CardView`.

## CardView
A useful widget that can display data in RecyclerView is the CardView widget.
To use CardView, ensure that you have the following dependency in your module-level  
[[Gradle and Configuration Files]]:
```groovy
implementation 'com.google.android.material:material:1.0.0'
```

CardView gives the "card look" to each item.
- You can change attributes to tweak the look of the cards
- You then specify the layout of the widgets within a CardView

The following is an overview of an [[XML Syntax|XML]] file specifying a CardView and the layout within.
Details have been removed from most widgets.
```xml
<androidx.cardview.widget.CardView  
	android:id="@+id/cardViewItem"  
	app:cardPreventCornerOverlap="false"  
	cardCornerRadius="5dp"  
	cardMaxElevation="1dp"  
	cardElevation="1dp"  
	cardUseCompatPadding="true"  
	android:layout_width="match_parent"  
	android:layout_height="100dp"  
	android:layout_margin="16dp">  
	
	<RelativeLayout  
		android:id="@+id/ard"  
		android:layout_width="match_parent"  
		android:layout_height="match_parent">  
		
		<ImageView />  
		<TextView />  
	</RelativeLayout>  

</androidx.cardview.widget.CardView>
```

## How to implement RecyclerView
### Step 1
Ensure that you have the following dependency in your module-level [[Understanding the build process|gradle]] file.
```groovy
implementation 'androidx.recyclerview:recyclerview:1.0.0'
```

### Step 2
Include the following widget tag in the Activity layout where you want to have the recyclerView
```xml
<androidx.recyclerview.widget.RecyclerView  
	android:id="@+id/charaRecyclerView"  
	android:layout_width="match_parent"  
	android:layout_height="match_parent" />
```

### Step 3
In [[Android Manifest]], add the attribute `android:exported="true"` to the Activity elment in which the RecyclerView is used.

### Step 4
Assuming each data item is stored in a CardView, design the layout of each data item.

### Step 5
Decide the source of your data:
- Stored in the res folder
- SQLiteDatabase
- Cloud Database
- etc

This lesson uses a local SQLiteDatabase.
You would have written a Database Helper class.

### Step 6
Write an Adapter class that extends `RecyclerView.Adapter<VH>` class.
This class takes in your data source and is called by the Android runtime to display the data on the RecyclerView widget. This class also references the data item that you designed in step 3.

### Step 7
In the java file for your activity, write code for the following
- get a reference to the recyclerView widget by using [[R class#Use findViewById method to assign a widget to a variable|findViewById()]]
- get an instance of an object that points to your dataSource
- instantiate your Adapter
- Attach adapter to your recyclerView widget
- attach Layout manager to your recyclerView widget. A LayoutManager governs how your widgets are going to be displayed. Since we scrolling up and down, we just need a LinearLayoutManager

```java
recyclerView = findViewById(R.id.charaRecyclerView);  
dataSource = ??? ;  
charaAdapter = new CharaAdapter(this, dataSource );  
recyclerView.setAdapter(charaAdapter);  
recyclerView.setLayoutManager(new LinearLayoutManager(this));
```

This way of coding shows how [[Delegation]] is performed.
[[Delegation]] is the transferring of tasks from one object to a related object.

The `RecyclerView` object delegates:
- the role of retireving data to the `RecyclerView.Adapter` object
- the role of managingthe layout to the `LinearLayoutManager` object

Thus the RecyclerView object makes use of the [[Strategy design pattern]].

A `GridLayoutManager` is also available.

## Writing the RecyclerView Adapter - Static Inner Class
[[Static inner classes to model data]]
[[Inner class]]
[[Adapter design pattern]]
The `RecyclerView` adapter class is the adapter class between ==the `RecyclerView` widget and the object containing your source of data.==

Extend the `RecyclerView.Adapter<VH>` class.
`VH` is a [[ArrayList, LinkedList, Generics|generic]] class that subclasses `RecyclerView.ViewHolder`.
This is an [[Abstract Class]] without any abstract methods.
Hence Android is forcing you to subclass this class to use its methods.

This class is meant to hold references to the widgets in each data item layout.
Typically, we will write such a class as an [[Inner class]] within the recyclerView adapter.

Hence, the classes are declared in the follwoing way:
```java
public class CharaAdapter extends RecyclerView.Adapter<CharaAdapter.CharaViewHolder>{  
	//code not shown  
	static class CharaViewHolder extends RecyclerView.ViewHolder{  
		//code not shown  
	}  
}
```

Having designed your CardView layout for each data item, `CharaViewHolder` will contain instance variables that are meant to hold references to the widgets on the layout.
The references are obtained by [[R class#Use findViewById method to assign a widget to a variable|findViewById()]] within the [[Week 2 - Constructors|constructor]].

## Writing the RecyclerView Adapter - write the constructor and override 3 methods
The cosntructor should take in
- a Context object
- Object for your data source

Context object is used to get a layout inflator object to be used in `onCreateViewHolder()`

`RecyclerView.Adapter<VH>` is an [[Abstract Class]] and you have to override 3 abstract methods. [[Adapter design pattern]]

`onCreateViewHolder()` is called by the run-time each time a new data item is added.
In the code recipe below:
- the CardView layout is inflated
- a reference to the layout in memory is returned `itemView`
- this reference is passed to the constructor of `CharaViewHolder`
- `CharaViewholder` uses thsi reference to get references to the individual widgets in the layout

```java
public CharaViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {  
	View itemView = mInflater.inflate(R.layout.layout, viewGroup, false);  
	return new CharaViewHolder(itemView);  
}
```

`onBindViewHolder()`
- get the appropriate data from data source
- attach it to the widgets on each data item, according to adapter position

Hence the data on row 0 of a table goes on position 0 on the adapter and so on.

`getItemCount()` is meant to return the total numberof data items. Hence, if you return 0, nothing can be seen on the RecyclerView.

