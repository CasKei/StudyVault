---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]

With a [[Building a URL|URL]] object, you are ready to download data from the internet.
In the starter code, you are provided with a **Utils** class.

There are 3 static methods for you to use. You do not need to worry about how they are implemented, though if you are querying an API for your 1D you should find the code useful.
You should see that some of these methods print data to the [[Logcat]].

## getImageURLFromXkcdApi
Takes in comic number, queries xkcd API, returns image URL for that comic.
Please note the [[Exception]]s thrown by this method.
```java
static String getImageURLFromXkcdApi(String comicNo)
```

## getBitmap
Takes in a URL for an image and returns the image as a Bitmap object.
Note the [[Exception]]s
```java
static Bitmap getBitmap(URL url)
```

## isNetworkAvailable
Takes in a Context object and checks if a network connection is available. Return boolean.
Context is superclass of AppCompatActivity
```java
static boolean isNetworkAvailable(Context context)
```