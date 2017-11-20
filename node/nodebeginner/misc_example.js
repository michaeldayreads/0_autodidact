function say(word) {
	console.log(word);
}

function execute(someFunction, value) {
	someFunction(value);
}

execute(say, "Well, yes, that is pretty damn cool");

execute(function(word) { console.log(word)  }, "...this, too, is pretty damn cool."  );

