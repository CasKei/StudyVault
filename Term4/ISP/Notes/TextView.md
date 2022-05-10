---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

## Overview
Basic widget:
```xml
<TextView
	android:id="@+id/myTextView"
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:layout_gravity="center"
	android:gravity="end"
	android:text="second"/>
```
- **id attribute** enables you to give a unique ID to each widget in the XML layout file. Allows you to access the widget through the java code
- **text attribute** specifies the text that the widget should contain

## TextView
One `View` subclass you may use often is the [`TextView`](https://developer.android.com/reference/android/widget/TextView.html) class, which displays text on the screen. You can use `TextView` for a `View` of any size, from a single character or word to a full screen of text. You can add a resource `id` to the `TextView` in the layout, and control how the text appears using attributes in the layout file.

You can refer to a `TextView` in your Java code by using its resource `id` in order to update the text or its attributes from your code. If you want to allow users to edit the text, use [`EditText`](https://developer.android.com/reference/android/widget/EditText.html), a subclass of `TextView` that allows text input and editing. You learn all about `EditText` in another lesson.

### TextView attributes
You can use XML attributes for a `TextView` to control:
-   Where the `TextView` is positioned in a layout (like any other view)
-   How the `TextView` itself appears, such as with a background color
-   What the text looks like within the `TextView`, such as the initial text and its style, size, and color

For example, to set the width, height, and initial text value of the view:
```xml
<TextView
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:text="Hello World!"
   <!-- more attributes -->
/>
```
You can extract the text string into a string resource (perhaps called `hello_world`) that's easier to maintain for multiple-language versions of the app, or if you need to change the string in the future. After extracting the string, use the string resource name with `@string/` to specify the text:
```xml
<TextView
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:text="@string/hello_world"
   <!-- more attributes -->
/>
```
In addition to `android:layout_width` and `android:layout_height` (which are required for a `TextView`), the most often used attributes with `TextView` are the following:
-   [`android:text`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:text): Set the text to display.
-   [`android:textColor`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textColor): Set the color of the text. You can set the attribute to a color value, a predefined resource, or a theme. Color resources and themes are described in other chapters.
-   [`android:textAppearance`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textAppearance): The appearance of the text, including its color, typeface, style, and size. You set this attribute to a predefined style resource or theme that already defines these values.
-   [`android:textSize`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textSize): Set the text size (if not already set by `android:textAppearance`). Use `sp` (scaled-pixel) sizes such as `20sp` or `14.5sp`, or set the attribute to a predefined resource or theme.
-   [`android:textStyle`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:textStyle): Set the text style (if not already set by `android:textAppearance`). Use `normal`, `bold`, `italic`, or `bold`|`italic`.
-   [`android:typeface`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:typeface): Set the text typeface (if not already set by `android:textAppearance`). Use `normal`, `sans`, `serif`, or `monospace`.
-   [`android:lineSpacingExtra`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:lineSpacingExtra): Set extra spacing between lines of text. Use `sp` (scaled-pixel) or dp (device-independent pixel) sizes, or set the attribute to a predefined resource or theme.
-   [`android:autoLink`](https://developer.android.com/reference/android/widget/TextView.html#attr_android:autoLink): Controls whether links such as URLs and email addresses are automatically found and converted to clickable (touchable) links.

Use one of the following with `android:autoLink`:
-   `none`: Match no patterns (default).
-   `web`: Match web URLs.
-   `email`: Match email addresses.
-   `phone`: Match phone numbers.
-   `map`: Match map addresses.
-   `all`: Match all patterns (equivalent to web|email|phone|map).

For example, to set the attribute to match web URLs, use `android:autoLink="web"`.

### Using embedded tags in text
In an app that accesses magazine or newspaper articles, the articles that appear would probably come from an online source or might be saved in advance in a database on the device. You can also create text as a single long string in the strings.xml resource.

In either case, the text may contain embedded HTML tags or other text formatting codes. To properly display in a text view, text must be formatted following these rules:

-   Enter **\n** to represent the end of a line, and another **\n** to represent a blank line. You need to add end-of-line characters to keep paragraphs from running into each other.
-   If you have an apostrophe (`'`) in your text, you must _escape_ it by preceding it with a backslash (**\'**). If you have a double-quote in your text, you must also escape it (**\"**). You must also escape any other non-ASCII characters. See the "[Formatting and Styling](https://developer.android.com/guide/topics/resources/string-resource.html#FormattingAndStyling)" section of String Resources for more details.
-   Enter the HTML and **</b>** tags around words that should be in bold.
-   Enter the HTML and **</i>** tags around words that should be in italics. Note, however, that if you use curled apostrophes within an italic phrase, you should replace them with straight apostrophes.
-   You can combine bold and italics by combining the tags, as in ****_..._**** words...**</i></b>**. Other HTML tags are ignored.
-   To create a long string of text in the `strings.xml` file, enclose the entire text within `<string name="`_your_string_name_`"></string>` (_your_string_name_ is the name you provide the string resource, such as `article_text`).
-   As you enter or paste text in the `strings.xml` file, the text lines don't wrap around to the next line—they extend beyond the right margin. This is the correct behavior—each new line of text starting at the left margin represents an entire paragraph.

**Tip:** If you want to see the text wrapped in strings.xml, you can press Return to enter hard line endings, or format the text first in a text editor with hard line endings. The endings will not be displayed on the screen.

### Referring to a TextView in code
To refer to a `TextView` in your Java code, use its resource `id`. For example, to update a `TextView` with new text, you would:

1.  Find the `TextView` and assign it to a variable. You use the [`findViewById()`](https://developer.android.com/reference/android/view/View.html#findViewById(int)) method of the `View` class, and refer to the view you want to find using this format:
    ```xml
     R.id.view_id
    ```
    
    In which _view_id_ is the resource identifier for the view (such as `show_count`) :
    ```xml
    mShowCount = (TextView) findViewById(R.id.show_count);
    ```
    
2.  After retrieving the `View` as a `TextView` member variable, you can then set the text to new text (in this case, `mCount_text`) using the [`setText()`](https://developer.android.com/reference/android/widget/TextView.html#setText(java.lang.CharSequence)) method of the `TextView` class:
    
    ```xml
     mShowCount.setText(mCount_text);
    ```