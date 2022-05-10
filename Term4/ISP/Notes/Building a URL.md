---
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 3]]
[[Using the xkcd.com web API]]

A URL is a URI that refers to a particular website. The parts of a URL are:
| Component | Example                  |
| --------- | ------------------------ |
| Scheme    | https                    |
| Authority | xkcd.com                 |
| Path      | info.0.json <br> or <br> 614/info.0.json|

To prevent parsing errors you may use the `Uri` builder before creating a URL object.
Using such a [[Builder design pattern]] helps to eliminate coding errors.
The string constants may be placed in the `strings.xml` file instead.

After you create the `Uri` object, use it the make a `URL` object.
The constructor of the URL class throws a `MalformedURLException`.
As this is a **checked** [[Exception]], you have to put the code in a **try-catch** block.

```java
final String scheme = "https";  
final String authority = "xkcd.com";  
final String back = "info.0.json";  
URL url = null;  
Uri.Builder builder = new Uri.Builder();  
builder.scheme(scheme)  
	.authority(authority)  
	.appendPath(back);  

Uri uri = builder.build();  

try {  
	url = new URL(uri.toString());  
} catch(MalformedURLException ex) {  
	Log.i(TAG, "malformed URL: " + url.toString());  
}
```