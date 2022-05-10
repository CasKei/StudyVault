---
aliases: Executor, Runnable, Container, Looper, Handler
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]
[[Concurrent Programming]]

# The Executor class
In Java, we gain access to the executor/scheduler service via the `Executor` class.
Through the executor, we are able to acces the pool of threads for a program.

## The Runnable interface
An instance of the Runnable [[Interfaces|interface]] denotes a sequence of instructions to be executed in a thread.
[[Static factory method]]
[[Android 1#Anonymous Class]]
```java
// main thread (i.e. UI thread)
ExecutorService executor = Executors.newSingleThreadExecutor(); // static fac meth
executor.execute(new Runnable(){ // anonymous class
	@Override
	public void run() {
	// a new thread
	// some instructions to be exec in the new thread
	}
});
```

`Executors.newSingleThreadExecutor()`: instantiates a single thread executor service.
Other construction methods are available, e.g. `newFixedThreadPool(int nThreads)`
[More details](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html)

`run()`: an *abstract method* defined in the `Runnable` [[Interfaces|interface]]. An intance of `Runnable` interface must implement/override this method.

What happens if the `Runnable` / the sub-routine running in the thread needs to  
exchange information with the main thread (UI thread)?

## Immutable Variable
Instructions in the child thread can only access variables from the main thread if they are immutable (i.e. final)

This will have compilation error.
```java
//main thread (i.e. UI thread)
String s = ...;  
ExecutorService executor = Executors.newSingleThreadExecutor();  
executor.execute(new Runnable() {  
	@Override  
	public void run() {  
		// a new thread  
		System.out.println(s); // illegal access  
	}  
});
```

This is ok
```java
// main thread (i.e. UI thread)  
final String s = ...;  
ExecutorService executor = Executors.newSingleThreadExecutor();  
executor.execute(new Runnable() {  
	@Override  
	public void run() {  
		// a new thread  
		System.out.println(s); // legal access  
	}  
});
```

> This implies that shared data cannot be modified in the child thread.

## Container
To work around this, use a [[ArrayList, LinkedList, Generics|generic]] class `Container`.
```java
// a container class  
class Container<T> {  
	T value;         // data type and field
	Container(T v) {  // constructor
		this.value = v; 
	}  
	void set(T v) { //getter and setter
		this.value = v; 
	}  
	T get() { 
		return this.value; 
	}  
}
```

Data to be exchanged is put between the main and child threads in a `Container` object.

```java
// main thread (i.e. UI thread)
String s = ...;
final container<String> cs = new Container<>(s);
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.execute(new Runnable() {
	@Override
	public void run() {
		// a new thread
		String s1 = cs.get() + "!";
		cs.set(s1);
	}
});
```

Question: How can we inform the UI thread when the child thread is done asynchronously?  
In other words, without having the UI thread to constantly check whether the child thread is  done.

## Looper and Handler
In the Android multithreading library, each thread is associated with a message queue.
A message queue is created for the purpose of asynchronous communication.

There are 2 additional classes created for the purpose of reading and updating the message queues: `Looper` and `Handler` class.

```java
// main thread (i.e. UI thread)  
ExecutorService executor = Executors.newSingleThreadExecutor();  
Looper uiLooper = Looper.getMainLooper(); // get the main looper  
Handler handler = new Handler(uiLooper); // get the handler for the main thread  
executor.execute(new Runnable() {  
	@Override  
	public void run() {  
		// a new thread  
		// instructions performed in the child thread  
		// ...  
		handler.post(new Runnable() {  
			@Override  
			public void run() {  
				//UI Thread will receive and run this  
			}  
		});  
	}  
});
```

## Using Executor and Runnable in your Android App
### 1. Prevent Activity from changing orientation
1. App layout is destroyed and re-created if screen is rotated in the [[Android Activity Lifecycle]].
2. If child thread is running in background during this process, it will not be able to display the result on the re-created activity.
3. Hence, you need to constrain your activity so that it is always in your desired orientation.
4. This is done in [[Android Manifest]].

### 2. Define a generic class in MainActivity or some util package which serves as a container
Make the following decisions to help you decide the [[ArrayList, LinkedList, Generics|generic]] types:
1. What information launches the background task (the child thread)?
2. What information do I want to give the user as the task proceeds?
3. What information does the background task provide?
4. When the background task is completed, how shall the UI be updated?

### 3. Decide what jobs are to be run in the two Runnable instances
1. `run()` in the outer **Runnable** always carries out the background task (child thread), e.g. downloading the image data from a URL.
2. `run()` in the inner **Runnable** carries out the job to be performed (in the UI thread) after the background task is complete. Suppose the task is to download an image given a URL, this is where you write code to display the image on the UI.

### 4. Define a method getComic() which implements the background task as well as the handler task (task to be performed upon completion of the background task)
One possible code stump is
```java
void getComic(final String userInput) {
	ExecutorService executor = Executors.newSingleThreadExecutor();
	final Handler handler = new Handler(Looper.getMainLooper());

	executor.execute(new Runnable() {
		@Override
		public void run() {
			// Bg
			final Container<Bitmap> cBitmap = new Container<>();
			// retrieve the bitmap from xkcd and store it in cBitmap
			handler.post(new Runnable() {
				@Override
				public void run() {
					// UI
					if (cBitmap.get != null) {
						// retrieve the bitmap and display it
					}
				}
			});
		
		}
	});
}
```

### 5. Decide how the user is to execute the background task
Let's say your user will download the image with a button click. Then you put the following code in the anonymous class within `setOnClickListener()`
```java
getComic(userInput);
```

## Alternative: use an abstract class
`AsyncTask` could be bad and deprecated. Can we define our own? Can we extract the reusable part from the `getComic()` code?
```java
abstract class BackgroundTask<I, O> {  
    ExecutorService executor;  
    final Handler handler = new Handler(Looper.getMainLooper());  
    public BackgroundTask() {  
        this.executor = Executors.newSingleThreadExecutor();  
    }    abstract public O runInBackground(I i);  
    abstract public void whenDone(O o);  
  
    public void run(final I i) {  
        final Container<O> co = new Container<>();  
        this.executor.execute(new Runnable() {  
            @Override  
            public void run() {  
                co.set(BackgroundTask.this.runInBackground(i));  
                handler.post(new Runnable() {  
                    @Override  
                    public void run() {  
                        if (co.get() != null) {  
                            whenDone(co.get()); 
                        }
                    }                
                });            
            }       
        });    
    }
}
```
We may now define a nested class to replace `getComic()` by extending the `BackgroundTask` class.
```java
void getComic2 (final String userInput) {  
	(new BackGroundTask<String, Bitmap>() {  
		@Override  
		public Bitmap runInBackground(String userInput) {  
			Bitmap bitmap = null;  
			// background task here  
			return bitmap;  
		}  
		@Override  
		public void whenDone(Bitmap bitmap) {  
			if (bitmap != null) {  
			// UI thread job here  
			}  
		}  
	}).run(userInput);  
}
```