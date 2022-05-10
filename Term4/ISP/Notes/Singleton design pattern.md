---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W5]]
[[Android 4]]

## Singleton design pattern
> Allows only one instance of a class to exist. Done by:
> - Make [[Week 2 - Constructors|constructor]] private
> - The sole instance is stored in a private static variable
> - Using a [[Static factory method]] to return an instance

- Ensure there is only one instance of an object, available to a number of other classes

E.g. LogFile for a pool of applications
GoF: Ensure a class has only one instance and provide a global point of access to it

A creational pattern: it is used to construct objects

## General
```java
public class Singleton{  
	private static Singleton singleton;  
	
	private Singleton(){  
		//any tasks you need to do here  
	}  
	
	public static Singleton getInstance(){  
		if(singleton == null){  
			singleton = new Singleton();  
		}  
		return singleton;  
	}  
	
	//other methods in your class  
}

```

## Logfile
e.g.
```java
public class LogFile {

	private static LogFile instance = null;

	// private constructor: ppl cant create instance directly from new operator
	private LogFile(){
		
	}

	public static LogFile getInstance() {
		if (instance == null) {
			instance = new LogFile();
		}
		return instance;
	}
}

```


Now have a app use this logfile
```java
public class App1 {
	private static LogFile logfile;

	App1() {
		//logfile  new LogFile();     this cannot work
		logfile = LogFile.getInstance();
	}
}
```
```java
public class App2 {
	private static LogFile a = null;;

	App2() {
		//logfile  new LogFile();     this cannot work
		a = LogFile.getInstance();
	}
}
```


- Private constructor
- Lazy instantiation: create the instance only when it is used