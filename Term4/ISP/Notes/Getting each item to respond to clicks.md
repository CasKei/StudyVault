---
aliases: 
tags: 50.001
---
[[IS & Programming|ISP]]
[[Android 4]]

Since we extend [[RecyclerView]].ViewHolder, we have access to the parent class' methods.
One method is `getAdapterPosition()`, which displays the ViewHolder's position on the RecyclerView.
Use this method to display a [[Toast]] when each ViewHolder is clicked

## Option 1
Since a reference to the [[RecyclerView|CardView]] layout is passed to the ViewHolder class, then you may call `setOnClickListener` on this reference within the constructor, and pass it to an [[Anonymous class]] in the usual way.

## Option 2
`CharaViewHolder` class can implement `View.OnClickListener` [[Interfaces|interface]].
Then `onClick` has to be implemented as an instance method.
You still need to call `setOnClickListener` on the reference to the [[RecyclerView|CardView]] layout.
What object do you pass to `setOnClickListener`?