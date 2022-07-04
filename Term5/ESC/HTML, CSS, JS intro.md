---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Basic web app architecture]]

## Overview
| HTML      | CSS   | JavaScript                 |
| --------- | ----- | -------------------------- |
| Structure | Style | Add dynamism and behaviour |

## HTML
### Tags
Keywords that define how web browser format and display content.
### Attributes
Like an opening tag and additional info placed inside
### Construction
`<!DOCTYPE html>`
Specifies the language
`<html>`
signals that from here on we will write html code
`<head>`
metadata
`<body>`
content

![[Pasted image 20220630125218.png]]

![[Pasted image 20220630125243.png]]

## CSS
Cascading Style Sheets
```css
selector {
	propertyname: value;
}
```
Inline, external

## JS
Inline
```html
<script>
	alert("I am an alert box");
</script>
```
External
```html
<script src="file.js"></script>
```
```js
alert("I am an alert box");
```

### Comments
```js
// inline
/* multi 
line*/
```
### Declaring variables and assigning values
```js
var x;
var y = 10;
var w, z = 2, 5;
```
Variable names: combi of letters, nums, underscore, dollar
but cannot start with num or use other special characters
### Variable types
number, string, boolean, object, undefined, null
`typeof()`
### Strings
`document.write()`
insert js into html
supports some tags

`+` to concatenate

#### Template literals
Use backticks instead
```js
var freq = `day`;
document.write(`I like playing every ${freq}.`);
```
