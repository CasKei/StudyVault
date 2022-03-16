---
tags: #50.001
---
[[IS & Programming|ISP]]
[[Google Developer Training]]

## Scrolling views

If the information you want to show in your app is larger than the device's display, you can create a _scrolling view_ that the user can scroll vertically by swiping up or down, or horizontally by swiping right or left.

You would typically use a scrolling view for news stories, articles, or any lengthy text that doesn't completely fit on the display. You can also use a scrolling view to combine views (such as a `TextView` and a `Button`) within a scrolling view.

### Creating a layout with a ScrollView
The [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView.html) class provides the layout for a vertical scrolling view. (For horizontal scrolling, you would use [`HorizontalScrollView`](https://developer.android.com/reference/android/widget/HorizontalScrollView.html).) `ScrollView` is a subclass of [`FrameLayout`](https://developer.android.com/reference/android/widget/FrameLayout.html), which means that you can place only _one_ `View` as a child within it; that child contains the entire contents to scroll.![ A ScrollView with one child View](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-3-c-text-and-scrolling-views/dg_scrollview_layout_diagram.png " A ScrollView with one child View")

Even though you can place only one child `View` inside a `ScrollView`, the child `View` can be a [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup.html) with a hierarchy of child `View` elements, such as a [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout.html). A good choice for a `View` within a `ScrollView` is a `LinearLayout` that is arranged in a vertical orientation.![ A ScrollView with a LinearLayout](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-3-c-text-and-scrolling-views/dg_scrollview_linearlayout_diagram.png " A ScrollView with a LinearLayout")

### ScrollView and performance
All of the contents of a `ScrollView` (such as a `ViewGroup` with `View` elements) occupy memory and the view hierarchy even if portions are not displayed on screen. This makes `ScrollView` useful for smoothly scrolling pages of free-form text, because the text is already in memory. However, a ScrollView with a `ViewGroup` with `View` elements can use up a lot of memory, which can affect the performance of the rest of your app.

Using nested instances of `LinearLayout` can also lead to an excessively deep view hierarchy, which can slow down performance. Nesting several instances of `LinearLayout` that use the `android:layout_weight` attribute can be especially expensive as each child `View` needs to be measured twice. Consider using flatter layouts such as [`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout.html) or [`GridLayout`](https://developer.android.com/reference/android/widget/GridLayout.html) to improve performance.

Complex layouts with `ScrollView` may suffer performance issues, especially with images. We recommend that you _not_ use images within a `ScrollView`. To display long lists of items, or images, consider using a [`RecyclerView`](https://developer.android.com/reference/android/support/v7/widget/RecyclerView.html), which is covered in another lesson.

### ScrollView with a [[TextView]]
To display a scrollable magazine article on the screen, you might use a [`RelativeLayout`](https://developer.android.com/reference/android/widget/RelativeLayout.html) that includes a separate `TextView` for the article heading, another for the article subheading, and a third `TextView` for the scrolling article text (see the figure below), set within a `ScrollView`. The only part of the screen that would scroll would be the `ScrollView` with the article text.![ The layout with a ScrollView](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-3-c-text-and-scrolling-views/dg_layout_diagram1.png " The layout with a ScrollView")

### ScrollView with a [[Linear Layout]]
A `ScrollView` can contain only one child `View`; however, that `View` can be a [`ViewGroup`](https://developer.android.com/reference/android/view/ViewGroup.html) that contains several `View` elements, such as [`LinearLayout`](https://developer.android.com/reference/android/widget/LinearLayout.html). You can _nest_ a `ViewGroup` such as `LinearLayout` _within_ the `ScrollView`, thereby scrolling everything that is inside the `LinearLayout`.

For example, if you want the subheading of an article to scroll along with the article even if they are separate `TextView` elements, add a `LinearLayout` to the `ScrollView` as a single child `View` as shown in the figure below, and then move the `TextView` subheading and article elements into the `LinearLayout`. The user scrolls the entire `LinearLayout` which includes the subheading and the article.![ A LinearLayout Inside the ScrollView](https://google-developer-training.github.io/android-developer-fundamentals-course-concepts-v2/images/1-3-c-text-and-scrolling-views/dg_layout_diagram2.png " A LinearLayout Inside the ScrollView")

When adding a `LinearLayout` inside a `ScrollView`, use `match_parent` for the `LinearLayout` `android:layout_width` attribute to match the width of the parent `ScrollView`, and use `wrap_content` for the `LinearLayout` `android:layout_height` attribute to make it only large enough to enclose its contents.

Since `ScrollView` only supports vertical scrolling, you must set the `LinearLayout` orientation attribute to vertical (`android:orientation="vertical"`), so that the entire `LinearLayout` will scroll vertically. For example, the following XML layout scrolls the `article` `TextView` along with the `article_subheading` `TextView`:
```xml
<ScrollView
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:layout_below="@id/article_heading">

   <LinearLayout
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:orientation="vertical">

      <TextView
         android:id="@+id/article_subheading"
         android:layout_width="match_parent"
         android:layout_height="wrap_content"
         android:padding="@dimen/padding_regular"
         android:text="@string/article_subtitle"
         android:textAppearance=
                       "@android:style/TextAppearance.DeviceDefault" />

      <TextView
         android:id="@+id/article"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:autoLink="web"
         android:lineSpacingExtra="@dimen/line_spacing"
         android:padding="@dimen/padding_regular"
         android:text="@string/article_text" />
   </LinearLayout>

</ScrollView>
```