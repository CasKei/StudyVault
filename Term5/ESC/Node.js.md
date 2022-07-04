---
tags: 50.003
---
[[50.003 Elements of Software Construction|50.003]]
[[Basic web app architecture]]
[[JavaScript]]

## Node.js
- Open-source, cross-platform, backend runtime environment that executes JS outside a web browser.
- Allows server-side scripts to run to produce dynamic web page content before the page is sent to the user's browser.
- Represents "JavaScript everywhere" paradigm for web app dev
- Event-driven architecture capable of asynchronous IO
- Allows the creation of Web servers and relies on a collection of "modules" that handle various core functionalities

https://www.youtube.com/watch?v=Oe421EPjeBE&ab_channel=freeCodeCamp.org

## Installation
[nodejs.org](nodejs.org)
After setup, open cmd. Check with `node --version`

## Evaluate code: REPL
In cmd, type `node`
Now can execute short codes.
`ctrl + c` to leave
## Evaluate code: CLI
Write js file, cd to this file.
Type `node app.js`
## 2 global vars to know
- `__dirname` : path to current dir
- `__filename` : name of the file

## Node modules
- Node modules allow you to extend the default functionality available to Node.js scripts and to share variables, functions, objects, etc. with other files.  
- Every JS file is a module.  
- Some modules are installed by default but some modules need to be installed. 
- You can also create your own modules.  
- `console.log(module)` gives you access to all the properties of the current module.  
- The `exports` property indicates what variables from the module are exported. By default, none!

```js
const mum = "Sara";
const my_secret_lover = "Dewi";
module.exports = {mum}
```
- You can specify variables and functions allowed for export by setting the `module.exports` object accordingly.  
- In the example, note that `my_secret_lover` is not shared, and its value cannot be accessed outside of the file.

```js
const sayHi = (name) => {
	console.log(`Hello ${name}!`);
}
module.exports = sayHi;
```
```js
const names = require("./2-firstModule");
const sayHi = require("./3-secondModule");
sayHi("Sergey");
sayHi(names.my_name);
sayHi(names.bro);
sayHi(names.my_secret_lover);
```
- If more than one variable is shared by module A, the export variables are stored in an object.  
- To make use of module A variables into file B, you can assign to a const variable the shared object of A using the `require()` function.  
- The argument of `require()` is a path to module A.  
- To access the value of a single shared variable, you just need to use the name of the `const` variable (e.g., `sayHi` in `4-testModules.js`).  
- If an object was exported, you need to use the syntax: `object_name_of_B.shared_variable_of_A`
- It returns `undefined` if a variable is not exported or does not exist in module A.

![[Pasted image 20220630205909.png]]

### Built-in Modules
![[Pasted image 20220630205949.png]]

## Asynchronous execution
```js
const fs = require('fs');
fs.mkdir('testfolder2', function (arr) {
	if (arr) {
		throw(err);
	} else {
		console.log('Directory created');
	}
});
console.log('Likely displayed first!');
```
The second arg is a function executed once the folder creation has completed.
- By default, node runs asynchronously: code can continue doing other things while waiting for an action to complete.

Node is [[Types of system calls|non-blocking]]: allows other code to run while a specific op that could take time is executing
- advantage: this 'long' operation will not block the rest of the code
- when complete, in general, a callback function (e.g. this second function) is executed

## Synchronous execution
```js
const fs = require('fs');
fs.mkdirSync('testfolder3');
console.log(`Displayed after creation!`);
```
- node offers synchronised versions of most functions though it is not considered best practice as it slows down the program execution among other issues

## NPM
- Node Package Manager
- Allows
	- reuse code in other projects
	- use code from other developers
	- share solutions
- NPM project is hosted at www.npmjs.com  
- Well-known and useful frameworks are hosted there: React, Express, etc.  
- To check your npm version, just execute `npm --version` in the console and update it with `npm install npm@latest -g`

### Local and global dependencies
- install package locally: `npm i packagename`
- install package globally: `npm install -g packagename`
- install package in the local `node_modules` folder: `npm install packagename`
- uninstall package: `npm uninstall packagename`

### Example with Express package
```shell
npm install express
```
```js
const express = require("express");
let http = express();
console.log(http);
```
- Install Express within project folder
- Make use of it with `require()`

## Event loop
[nodejs event loop](https://nodejs.dev/learn/the-nodejs-event-loop "https://nodejs.dev/learn/the-nodejs-event-loop")
[event loop timers and nexttick](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/ "https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/")
- allows node to perform [[Types of system calls|non-blocking]] IO despite JS being single-[[Week 4 - Processes and Thread management|thread]]ed, by offloading operations to kernel whenever possible

### Call stack
![[Pasted image 20220701191953.png]]
`setTimeout`: makes call to a function, executes it after a timer in ms has expired...but only after other functions in the call stack has executed
![[Pasted image 20220701192023.png]]

- ES6 introed job queues used notably by promises
- job queue offers a way to execute the result of an async function asap, rather than being put at the end of the call stack
- promises that resolve before the current function ends will be executed right after the current function and before the callbacks

![[Pasted image 20220701192146.png]]
![[Pasted image 20220701192203.png]]
![[Pasted image 20220701192229.png]]
![[Pasted image 20220701192248.png]]

## Event-driven programming
Browser side:
- actions of users are handled through `events`: mouse, buttons, etc

Server side:
- listen for specific events and execute callbck functions in response of these events

### Event emitter
```js
const EventEmitter = require('events');
const instEvEmitter = new EventEmitter();
instEvEmitter.on('start', () => {
	console.log('Data received');
});
instEvEmitter.on('start', (a, b) => {
	console.log(`a + b = ${a+b}`);
});
instEvEmitter.emit('start', 3, 4);
```
- You can pass arguments in emit and the event handlers
- You can also trigger several actions at once after listening for a specific event
- impt: emit must be after the `on` methods: cant emit and action if you haven't listened

## http module
[[HTTP]] is a client-server communication protocol used by browsers to view webpages.
- http server is a software that understands [[Building a URL|URL]] addresses
- http module is used to create a http server
- `http.createServer()`

```js
const http = require('http');
const server = http.createServer((req, res) => {
	res.write("welcome to our webpage!");
	res.end();
});
const port = server.listen(5000);
```
![[Pasted image 20220701223300.png]]

### Create a server using Event Emitter API
```js
const http = require('http');
//alt: use event emitter api
const server = http.createServer();
server.on('request', (req, res) => {
	res.end("Welcome to our new webpage!");
});
const port = server.listen(5000);
```
- A server has `on` method and can listen for `request` event
- Once `request` event occurs, the callback of the `on` method is triggered as previously
- Servers can always listen a `request` event
- Even if we did not set up an event, the class `http.Server` extends the class `EventEmitter`

## HTTP
[[HTTP]]
### Messages
![[Pasted image 20220702073845.png]]
URL to browser -request-> server
server -response-> browser

These req and res are called HTTP messages
Nodejs is used to build web servers
Expressjs (a node framework) can create web servers

### Port numbers
[Port (computer networking)](https://en.wikipedia.org/wiki/Port_(computer_networking))
- Ports are communication endpoints in networking
- Used to identify specific process and type of network service
- 0 to 65535
- Associated with [[Mac and IP|IP]] address of a host and the type of transport protocol used for communication
- 0 to 1023 reserved for common [[Transport Control (TCP UDP)|TCP/IP]] applications and are called well-known ports
- Default: HTTP: port 80, HTTPS: port 443
- For deployment, can use value between 1024 and 49151

### about `end()`
- No exiting in these programs. The server stays on, waiting for requests.
- Everytime you refresh, request is sent.
- Browser side, nothing happens as response `end()` method is missing
- Response `end()` method signals to the server that all response headers and body have been sent, and server should consider this message complete.
- Response `end()` must be called on each response 

### HTTP headers
```js
const http = require('http');
const server = http.createServer((req,res) => {
	res.writeHead(200, { 'content-type' : 'text/plain'});
	//res.writeHead(200, { 'content-type' : 'text/html'});
	res.write('<h1>Home Page</h1>');
	res.end();
});
server.listen(5000);
```
- send back metadata using `res.writeHead()`  method
- fetch `writeHead()` with 2 args: a status code (200 == success) and a header
- headers are sent as object of key-value pairs
### Status code
- Indicates if specific HTTP request has been successfully completed
- In previous program, status code informed the browser whether the request was successful or not.
### html file
![[Pasted image 20220702091405.png]]
