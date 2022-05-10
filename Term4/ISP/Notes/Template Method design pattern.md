---
tags: 50.001
---
[[IS & Programming|ISP]]
[[W5|design pattern]]
[[Abstract Class]]

One application of an [[Abstract Class]] is this Template Method [[W5|design pattern]].

## What 
There is an algorithm with a fixed structure, but the implementation of some steps are left to the subclasses.

## Example
Taken from "Heads First Design Patterns - A brain-friendly guide".

We have a fixed way of brewing caffeine beverages, but you'll agree that how to brew it and what condiments to add depends on the beverage.

- The algorithm to make the beverage, `prepareRecipe()` is declared `final` to prevent subclasses from altering the algorithm
- The steps in the algorithm that are common to all beverages are implemented
- The steps that can vary are declared `abstract`.

Abstract class
```java
public abstract class CaffeineBeverage {
	final void prepareRecipe() {
		boilWater();
		brew();
		addCondiments();
		pourInCup();
	}

	abstract void brew();

	abstract void addCondiments();

	void boilWater() {
		System.out.println("Boiling Water");
	}

	void pourInCup() {
		System.out.println("Pouring in Cup");
	}
}
```

Subclasses
```java
class GourmetCoffee extends CaffeineBeverage {
	@Override
	void brew() {
		System.out.println("Put in Coffee Maker");
	}

	@Override
	void addCondiments() {
		System.out.println("Adding nothing, because gOuRmEt");
	}
}
```

Then brew coffee
```java
CaffeineBeverage caffeineBeverage = new GourmetCoffee();
caffeineBeverage.prepareRecipe();
```