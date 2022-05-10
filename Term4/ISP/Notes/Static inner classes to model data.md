---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 4]]

This example is from the app that you will build in the lesson.

[[Inner class]]

## DataSource
This is a class that is meant to contain data that will be displayed in the [[RecyclerView]].

A private [[ArrayList, LinkedList, Generics|ArrayList]] variable is declared to hold instances of **CardData**, a static [[Inner class]].

Each instance of **CardData** is meant to hold information for one image.
Bear in mind that such satic classes cannot access non-static variables of the enclosing class.

```java
public class DataSource {
	private ArrayList<CardData> dataArrayList;
	// rest of class not shown
	static class CardData {
		private String name;
		private String path;
		// constructors and getters not shown
	}
}
```