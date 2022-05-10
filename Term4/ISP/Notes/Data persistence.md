---
aliases: SharedPreferences, saving data
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 2]]

## Data Persistence with SharedPreferences
As user interacts with your app, they may
- close the app and restart it
- rotate the screen (if you allow it)

In such situations, data entered by your user is not stored.

There are [many ways of storing data](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-4-saving-user-data/lesson-9-preferences-and-settings/9-0-c-data-storage/9-0-c-data-storage.html), which is called **Data Persistence**.\
One way of enabling data persistence is through the `SharedPreferences` [[Interfaces|interface]].\
Information you would like to store is done using **key-value pairs**.

The code recipe is:
1. Declare filename of your `SharedReferences` object as as a final string instance variable. Also declare a final string variable as a key.
2. In `onCreate()`, get an instance of the `SharedPreferences` object
3. In `onPause()`, get an instance of the `SharedPreferences.Editor` object and store your key-value pairs. Commit your changes using apply.
4. In `onCreate()`, retrieve your data using the key. Don't forget to also assign a default value for the situation when no data is stored.

```java
private final String sharedPrefFile =
"com.example.android.mainsharedprefs";
public static final String KEY = "MyKey";
SharedPreferences mPreferences;

@Override
protected void onCreate(Bundle savedInstanceState) {
	//other code not shown
	mPreferences = getSharedPreferences(sharedPrefFile, MODE_PRIVATE);
	String Rate_text = mPreferences.getString(KEY, defaultValue);
}
@Override
protected void onPause() {
	super.onPause();
	SharedPreferences.Editor preferencesEditor = mPreferences.edit();
	preferencesEditor.putString(KEY, value);
	preferencesEditor.apply();
}
```