/* 
// annonymous method

http.createServer( (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.write('Hello world arrow function!');
  response.end();
}).listen(7777);
*/

/* 
// named function method

function start() {

  function cl(whatToLog){
    console.log(whatToLog)
  }

  function onRequest(request, response) {
    cl("Request received");
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.write('Hello world: named function!');
    response.end();
  }

  http.createServer(onRequest).listen(7777);
  cl("Server has started.");
}

exports.start = start;

*/

/* 
// asyncronous method callback example

const fs = require('fs');

fs.readFile('a file that does not exist', (err, data) => {
	if (err) {
		console.error('There was an error reading the file!', err);
		return;
	}
	// otherwise handle data
});

*/
/*
// asynchronous method on an EventEmitter

const net = require('net');
const connection = net.connect('localhost');

// adding an 'error' event handler to a stream:
connection.on('error', (err) => {
	console.error(err.message);
});

connection.pipe(process.stdout);
*/
/*
// no error event handler

const EventEmitter = require('events');
const ee = new EventEmitter();

setImmediate(() => {
	// designed to crash because no 'error' event handler
	ee.emit('error', new Error('This will crash'));
});
*/

// A -- potentially dangerous -- uncaughtException event handler

const fs = require('fs');

process.on('uncaughtException', (err) => {
	fs.writeSync(1, `Caught exception: ${err}`);
});

setTimeout(() => {
	console.log('This will still run');
}, 500);

// intentional, uncaught, exception
nonexistentFunc();
consol.log('This will not run.');

