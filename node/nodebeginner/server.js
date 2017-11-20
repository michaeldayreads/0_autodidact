
// annonymous method
/*
http.createServer( (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.write('Hello world arrow function!');
  response.end();
}).listen(7777);
*/

var http = require("http");
var url = require("url");

// named function method

function start(route) {

  function cl(whatToLog){
    console.log(whatToLog)
  }

  function onRequest(request, response) {
    cl("Request received");
    var pathname = url.parse(request.url).pathname;
    cl("Request for " + pathname + " received.");
    route(pathname);
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.write('Hello world: named function!');
    response.end();
  }

  http.createServer(onRequest).listen(7777);
  cl("Server has started.");
}

exports.start = start;
