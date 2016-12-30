var http = require("http");

// annonymous method
/*
http.createServer( (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.write('Hello world arrow function!');
  response.end();
}).listen(7777);
*/

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
