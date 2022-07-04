---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Basic web app architecture]]

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

## Comments
```js
// inline
/* multi 
line*/
```
## Declaring variables and assigning values
```js
var x;
var y = 10;
var w, z = 2, 5;
```
Variable names: combi of letters, nums, underscore, dollar
but cannot start with num or use other special characters
## Variable types
number, string, boolean, object, undefined, null
`typeof()`
## Strings
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

## Functions
```js
function name(x) {
	var y = 2 + x;
	return y;
}
```
```js
var output = name(3);
```

## Global and local variables
Defined outside functions. Use `var`.
```js
var food = "chicken rice";
function foodiwant() {
	var food = "fried rice";
	console.log(food)
}
console.log(food)
```
```
fried rice
chicken rice
```
## Scope/Context basics
[[Complete Process Context|context]]
### Global context
Code that is not within a function
### Function context
A function creates a new context. Any variable declared inside a function with var is not available outside the function.
### Block context
Created for variables defined using `let` rather than `var`.
- Functions, conditionals, loops provide a block context between {}
- In function context, `let` and `var` are similar. But advantage comes with the possibility to create a block scope for a variable.

E.g. 1: myname var is overwritten in `if` block
```js
var myname = "Peter Parker";
if (myname === "Peter Parker") {
	var myname = "Spiderman";
}
```
E.g. 2: not overwritten
```js
let myname = "Peter Parker";
if (myname === "Peter Parker") {
	let myname = "Spiderman";
}
```
E.g. 3: Error: cannot declare a global var with the same name than a var declared by `let` in the scope of this `let`
```js
let myname = "Peter Parker";
if (myname === "Peter Parker") {
	var myname = "Spiderman";
}
// ERROR
```
## Const
Error if you try to update the value of a const. Also uses block scope.
Try to use `let` and `const` since scope is clearer.

## Operators
- Arithmetic: `+ - * / `
	- ![[Pasted image 20220630140836.png]]
- Assignment `=`
	- ![[Pasted image 20220630141415.png]]
- Comparison `>` `<` `>=` `<=` `===`
	- ![[Pasted image 20220630141443.png]]
- Logic `&& ||`
	- ![[Pasted image 20220630141512.png]]
- Bitwise `^ & |`
	- ![[Pasted image 20220630141520.png]]
- Special
	- ![[Pasted image 20220630141531.png]]

![[Pasted image 20220630141558.png]]

## if else
```js
let x = 5;
if (x > 3) {
	console.log(`Yeet`);
} else {
	console.log(`Nah`);
}
```
Can be nested
`else if` for additional
## Switch
```js
let name = "Galois";
switch (name) {
	case "Galois":
		console.log("Duel");
		break;
	case "Godel":
		console.log("American");
		break;
	default:
		console.log("Who?");
}
```
## Conditional Operator
```js
let num = 8;
guess = (num === 8) ? "You win" : "You lose";
```
## User input
```js
let username = window.prompt("Name?", "");
if ((usename === null) || (username === "")) {
	console.log("Kek");
} else {
	console.log("Hi " + username);
}
```
## While
```js
let x = 1;
while (x < 10) {
	console.log(x);
	x++;
}
```
`break` statement can get out.
`do-while` do first
## For
```js
for (let k = 5; k > -4; k-=2) {
	console.log(k);
}
```
`continue` allows to stop current iteration
## Arrays
2 ways to create arrays: `new` and `[]`
```js
let arr = new Array(); // empty
let arr2 = new Array(4); // length 4, all entries undefined
let arr3 = new Array(3, 'Bob', true); // [3, 'Bob', true]
console.log(arr3.length) // 3
```
```js
let arr = [];
let arr2 = [4]; // NOT LENGTH, but [4]
let arr3 = [3, 'Bob', true];
```
Properties:
- `constructor`, `index`, `input`, `prototype`
Methods:
- `join()` , `pop()`, `push()`, `shift()`, `unshift()`, `reverse()`, `sort()`, `concat()`, `slice(start, [stop])`, `splice(start, num_items, add_items)`, `indexOf()`, `lastIndexOf()`, `every()`, `some()`, `map()`, `filter()`, `forEach()`, `reduce()`, `reduceRight()`, `includes()`, `flat()`, `flatMap()`, `isArray()`, `from()`, `of()`

### Sort
- converts el into string then sort by ascii
- numbers < uppercase < lowercase
- Sorting numeric arrays
	- define a comparison function
	- given 2 args, return a + num, - or 0 based on result
	- then sort using this funciton as an argument of `sort()` method
```js
function mysort(v1, v2) {
	if (v1 > v2) {return 1;}
	else if (v2 > v1) {return -1;}
	else {return 0;}
}
function mysortsq(v1, v2) {
	if (v1**2 > v2**2) {return 1;}
	else if (v2**2 > v1**2) {return -1;}
	else {return 0;}
}
let arr = [7, 3, -6];
numbers.sort(mysort);
```

### Every, some, map
- The argument of these methods is a function returning a Boolean that will run on each item of the array
- Function must receive 3 args
- every(): true if function is true for all items of array
- some(): true if function is true for at least one item in array
- map(): return an array with result of each function call on initial array

### Filter, forEach
filter: executes a provided function with boolean returns  for every array item and returns an array of items for which the function returns true

forEach: runs the function for each item in the array, does not return anything

### reduce, reduceRight
![[Pasted image 20220630155236.png]]
### includes
![[Pasted image 20220630155250.png]]

### Nested
![[Pasted image 20220630155321.png]]
### flat
![[Pasted image 20220630155335.png]]
### flatMap
![[Pasted image 20220630155346.png]]

### Array.isArray/from/of()
![[Pasted image 20220630155411.png]]

## Memory Management
| Identifier | Mem Addr    | Mem Value |
| ---------- | ----------- | --------- |
| x1         | 00172CHRK80 | 10        |

When var created, a box is assigned for the var and its value stored in the box. Var name refers to the address of the box.

### Aliasing
JS saves space by having 2 names point to the same memory address if they ahve the same value.

### Memory management in arrays
![[Pasted image 20220630190836.png]]
![[Pasted image 20220630190857.png]]
![[Pasted image 20220630190927.png]]
- If an element of an array is an array, then shallow copy will not copy the subarays to different locations of memory
- Changing a subarray element then affects both arrays, even though these are shallow copies.

![[Pasted image 20220630191032.png]]
![[Pasted image 20220630191050.png]]
