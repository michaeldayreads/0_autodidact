function say(text) {
	console.log(text);
}

function execute(someFunction, value) {
	someFunction(value);
}

execute(say, "Well, yes, that is pretty damn cool.");

function execute_0(anotherFunction, value) {
	anotherFunction(value);
}

execute_0(function(text) { console.log(text) }, "This is also cool, but harder to read. When would I actually want to use this?");

execute_0( (text) => { console.log(text)  }, "I'll be pretty stoked if this works. I'll be even more stoked when I fully understand it");
