---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Android 4]]

Recall [[Intents]]:
- Explicit: bring you from one activity to another. Data can be passed during this process.
- Implicit: bring you from one activity to a component in your app. You specify the kind of component you want, and the android runtime fetches what is available.

In both cases you launched the "destination" by invoking `startActivity()`.

==By invoking `startActivityForResult()`, you expect the destintion component to return a result.==

## Explicit intent
### Step 1: Declare your request code
A final static integer variable containing a unique integer that identifies your particular intent.
This is necessary as your activity could have more than one call to `startActivityForResult()`.
```java
final int REQUEST_CODE_IMAGE = 1000;
```

### Step 2: Declare an explicit intent in the usual way
Then invoke the `startActivityForResult()` with 2 arguments:
- the intent
- the request code

```java
Intent intent = new Intent(MainActivity.this, DataEntry.class);
startActivityForResult(intent, REQUEST_CODE_IMAGE);
```

### Step 3
In the destination activity, the user should interact with it.

### Step 4: A user action (e.g. clicking a button) brings the user back to the origin activity
The following code initiates this process
```java
Intent returnIntent = new Intent();
returnIntent.putExtra(KEY, value); // optional
setResult(Activity.RESULT_OK, returnIntent);
finish();
```

The first argument of `setResult()` is either
- `Activity.RESULT_OK` if the user has completed the tasks
- `Activity.RESULT_CANCELLED` if the user has somehow backed out

Hence, this code may be written twice, one for each scenario described above.
If you have data to transfer, you are reminded that you can use `putExtra()` method above. [[Intents]]

### Step 5: Back in the origin activity
[[Method Overloading & Overriding|Override]] the callback `onActivityResult()` to listen out for the result and carry out the next task. Note the sequence of if-statements.
```java
@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {

	if (requestCode == REQUEST_CODE_IMAGE) {
		if (resultCode == Activity.RESULT_OK) {
			// if you use putExtra in step 4 then you need this step
			double value = data.getDoubleExtra(DataEntry.KEY, defaultValue);
			Toast.makeText(this, "Message", Toast.LENGTH_LONG).show();
		}
		if (resultCode == Activity.RESULT_CANCELLED) {
			// write code if there's no result
		}
	}
}
```

If you have data transferred from step 4, you may retrieve this data on the intent object passed to this callback using the `getDoubleExtra()` method or other suitable methods (Recall Lesson 2).

Further reading  
-  [Google: getting data back from activity](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/unit-1-get-started/lesson-2-activities-and-intents/2-1-c-activities-and-intents/2-1-c-activities-and-intents.html#gettingdatabackfromactivity)
- [Dev trng: intents/results](https://developer.android.com/training/basics/intents/result)

## Implicit intents - opening the image gallery
The implicit intents to write can be found here: [Common Intents](https://developer.android.com/guide/components/intents-common#java)

To get the example code to retrieve an image, go to **File storage -> Retrieve a Specific Type of File** section.

Sample code in case website not available:
Example intent to get a photo:
```java
static final int REQUEST_IMAGE_GET = 1;

public void selectImage() {
	Intent intent = new Intent(Intent.ACTION_GET_CONTENT);
	intent.setType("image/*");
	if (intent.resolveActivity(getPackageManager()) != null) {
		startActivityForResult(intent, REQUEST_IMAGE_GET);
	}
}

@Override
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
	if (requestCode == REQUEST_IMAGE_GET && requestCode == RESULT_OK) {
		Bitmap thumbnail = data.getParcelable("data");
		Uri fullPhotoUri = data.getData();
		// Do work with photo saved at fullPhotoUri
	}
}
```

![[Pasted image 20220502194156.png]]

For implicit intents and other contract templates, refer to  
https://developer.android.com/training/basics/intents/result  
https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts
