---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Basic web app architecture]]
[[JavaScript]]
[[Node.js]]

![[Pasted image 20220702091732.png]]
![[Pasted image 20220702092626.png]]
## Limitations of [[Node.js#http module]] and Express
- Becomes messy as app becomes complex
- Need to setup path of every resource server-side
- Hence propted the use of Express to ease development
## Express: basics
```js
// import and invoke express module
const express = require('express');
const app = express();

// methods that can be used on app: get, post, put, delete, use, all, listen

// get: define what happens when user tries to get info from some route
app.get('/', (req, res) =>{
	console.log("User reaches the server");
	res.send("This is my home page");
});

// all('*', callback) : used to handle all other paths
app.all('*', (req,res) => {
	res.status(404).send('<h1>Resource not found</h1>');
});

// listen: tells the app which port to listen and what to do when listening
app.listen(5000, () => {
	console.log("Server is listening.");
});
```
It is good practice to send the status code of the requests by inserting the `.status(code)` between `res` and `.send()`

## Middleware
- Middleware functions are functions that have access to the `req` and the `res` objects, and to the next middelware function in the appliction's request-response cycle.
- The next middleware function is commonly denoted by a variable named `next`
https://expressjs.com/en/guide/using-middleware.html

Example: log for each req on server the method used by users, url they tried to access and the weekday
- troublesome to define in each `app.get()` block
- create a `logger()` middelware with unputs `req`, `res`, `next` and add it to each `get()`

```js
const express = require('express');
const app = express();
const logger(req, res, next) => {
	const method = req.method;
	const url = req.url;
	const time = new Date().getDay();
	console.log(method, url, time);
	next();
}
app.get('/', logger, (req, res) =>{
	res.send("Home page");
});
app.get('/about', logger, (req, res) =>{
	res.send("About page");
});
app.listen(5000, () => {
	console.log("Server is listening.");
});
```
- Middleware function must pass to next one or terminate cycle using `res.send()`
- This still needs to add logger manually in each `get()` method. Logger-like functions might be long
- Preferable to store logger function in external file

### `app.use()`
```js
const express = require('express');
const app = express();
const logger = require('./logger'); // create a logger folder and require it

app.use(logger);
// app.use('/about', logger); // if add path, logger called only if user tries to access a resource from this path
// now logger does not have to be there for all the get methods
app.get('/', (req, res) =>{
	res.send("Home page");
});
app.get('/about', (req, res) =>{
	res.send("About page");
});
app.listen(5000, () => {
	console.log("Server is listening.");
});
```
### Multiple middlewares
- possible to define multiple middelwares and call them all in `app.use()`
- arg of `app.use()` must then be an array of middlewares
- middlewares are executed sequentially, from first to last indices
![[Pasted image 20220702094056.png]]
![[Pasted image 20220702094104.png]]
### Queries in middlewares
![[Pasted image 20220702094150.png]]
![[Pasted image 20220702094203.png]]
![[Pasted image 20220702094212.png]]
## HTTP request methods (introduction)
-  [[HTTP]] works as request-response protocol between a client and a server
- defines methods to indicate the desired action to be performed on the identified resource
- GET: request and read data sent from a source
- POST: send/insert data to a server to create/update a resource
- PUT: send data to a server to create/update a resource
- DELETE: deletes the specified resource

### GET
```js
const books = [
	{
		id: 1,
		title: 'Memoirs of Hadrian'
	},
	{
		id: 2,
		title: 'To Kill a Mockingbird' 
	}
]
const user = [
	{id: 1, name: 'Alice'},
	{id: 2, name: 'Bob'}
]
module.exports = { books, user };
```
- Send back data in JSON format
- `res.json()` function sends a JSON response. This method sends a response (with the correct content-type) that is the parameter converted to a JSOn string using the `JSON.stringify()` method
```js
const express = require('express');
const app = express();
let { user } = require('./library');

app.get('./api/user', (req, res) => {
	res.status(200).json({success: true, library:user})
});
app.listen(5000, ()=> {
	console.log('Server is listening at port 5000');
});
```
### POST
![[Pasted image 20220702095340.png]]
![[Pasted image 20220702095351.png]]
![[Pasted image 20220702095358.png]]
## Routers
### Motivation
![[Pasted image 20220702095445.png]]
### Example
![[Pasted image 20220702095459.png]]

## Express generator
http://expressjs.com/en/starter/generator.html