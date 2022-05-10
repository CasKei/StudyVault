---
aliases: intent
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Intent
An **intent** is a message object that makes a request to the Android runtime system
- to start another specific activity (an [[#Explicit intent]]) or
- start some other general component in the phone e.g. a Map app (an [[#Implicit intent]])

Usign an intent, you are also able to pass data between the components.

## Explicit intent
### No Data being passed
If you are not passing data between activities, a typical explicit intent is written as follows using the `Intent` class.
```java
Intent intent = new Intent(MainActivity.this, SubActivity.class);
startActivity(intent);
```

Constructor of the intent object takes in two inputs
- `Context` object specifying current activity
- `Class` object specifying the activity to be started

The intent is then launched by invoking the `startActivity()` instance method.
You do not need to write any code in the receiving activity.

### Data to pass
If there is data to be passed, we put the `putExtra()` method of the intent object as well. Data is stored as key-value pairs.

*Step 1*: in `MainActivity`
```java
Intent intent = new Intent(MainActivity.this, SubActivity.class);
intent.putExtra(KEY, value);
startActivity(intent);
```
The `putExtra()` method takes in 2 inputs:
- a final string variable as key
- the data to be stored as value

*Step 2*: in `SubActivity`
You need to obtain the intent object using `getIntent()` and retrieve the data using the key using one of the `get` methods attached to the intent object.
Hence:
```java
Intent intent = getIntent();
double value = intent.getDoubleExtra(MainActivity.KEY, defaultValue);
```
You invoke the appropriate method according to the datatype that you want to receive.

In this case we want a double value, so we invoke `getDoubleExtra()`.
This method has 2 inputs:
- key to retrieve value
- Default value when nothing to be retrieved

## Implicit intent
Recall that in [[#Explicit intent]], you specify exactly which activity you user is brought to.

A more general way of using intents is implicit.
Rather than a specific Activity, specify the type of action wanted, provide just enough info, and let android run-time decide.

To illustrate, code recipe for launching Map App is shown
### Step 1
Build the [[Universal Resource Identifier|URI]] to specify the location that you want your map app to be. Using this builder helps avoid errors when hardcoding a URI string.
```java
String location = getStrong(R.string.default_location);
Uri.Builder builder = new Uri.Builder();
builder.scheme("geo").opaquePart("0.0").appendQueryParameter("q", location);
Uri geoLocation = builder.build();
```
### Step 2
Specify implicit intent by
- Specify general action, in this case to view data, hence `Intent.ACTION_VIEW` is passed to the constructor
- Specify the data that you wish to view, in this case it is the location [[Universal Resource Identifier|URI]] that you build in step 1

```java
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setData(geoLocation);
```


## Step 3
Check that the intent is able to be carried out before calling `startActivity()`
```java
if ( intent.resolveActivity(getPackageManager()) != null) {
	startActivity(intent);
}
```

### In Android SDK API ver. 30+
The following declarations in [[Android Manifest]] are required for the implicit intent to work:
```xml
<queries>  
	<!-- Browser -->  
	<intent>  
		<action android:name="android.intent.action.VIEW" />  
		<data android:scheme="http" />  
	</intent>  
	<!-- Camera -->  
	<intent>  
		<action android:name="android.media.action.IMAGE_CAPTURE"/>  
	</intent>  
	<!-- Gallery -->  
	<intent>  
		<action android:name="android.intent.action.GET_CONTENT"/>  
	</intent>  
	<!-- Map -->  
	<intent>  
		<action android:name="android.intent.action.VIEW"/>  
		<data android:scheme="geo"/>  
	</intent>  
</queries>
```
For details:
[Android 11 package visibility](https://developer.android.com/about/versions/11/privacy/package-visibility)
[Medium article](https://medium.com/androiddevelopers/package-visibility-in-android-11-cc857f221cd9)

## Other intents
[Other intents docs](https://developer.android.com/guide/components/intents-common)