function say(word) {
	console.log(word);
}

function execute(someFunction, value) {
	someFunction(value);
}

execute(say, "Well, yes, that is pretty damn cool");
