---
tags: #50.001
---
[[IS & Programming|ISP]]
[[W5]]

- Useful when you are interested in the state of an object and want to get notified whenever there is any change
- ==Subject== (publisher) maintains a list of its ==dependents== (observers/subscribers)
- Subjects notifies them automatically of any state changes

GoF: Define a one-to-many dependency between objects so that when one obj changes state, all its dependents are notified and updated automatically.

A behavioural pattern: form relationships between objects during execution at runtime.

![[Pasted image 20220221125249.png]]
- `Subject` and `Observer` are [[Interfaces]]
- Classes `ConcreteSubject` and `ConcreteObserver` *implement* the interfaces.

```java
public interface Subject {
	void register(Observer o);
	void unregister(Observer o);
	void notifyObservers();
}
```
```java
public interface Observer {
	void update(String msg);
}
```
E.g. message board: subject is a topic, observers can register to this topic
```java
public class Topic implements Subject {
	private ArrayList<Observer> observers = null;

	private String msg = null;

	Topic() {
		observers = new ArrayList<>();
	}

	@Override
	public void register(Observer o) {
		observers.add(o);
	}
	@Override
	public void unregister(Observer o) {
		observers.remove(o);
	}
	@Override
	public void notifyObservers() {
		for (Observer o : observers) {
			o.update(msg);
		}
	}

	public void postMessage(String msg) {
		this.msg = msg;
		notifyObservers();
	}
	
}
```
```java
public class Student implements Observer {

	private String id;
	private String msg;
	private Subject subject;

	public Student(String id, Subject subject) {
		this.id = id;
		this.subject = subject;
		this.subject.register(this);
	}

	public void update(String msg) {
		this.msg = msg;
		System.out.println(this.id + " receives : " + this.msg);
	}
}
```
```java
public class MyClass {
	public static void main(String[] args) {

		Topic topic50001 = newTopic;
		Student scott = new Student("scott", topic50001);
		Student norman = new Student("norman", topic50001);

		topic50001.postMessage("new semester starts");
		topic50001.unregister(norman);
	}
}
```
> scott receives : new semester starts
> normal receives : new semester starts

## Why Observer?
- Reduce coupling
- An object (Subject) needs to share its state with other objects, without knowing who those objects are