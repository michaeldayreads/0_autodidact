turing = (name) => {
  return {
    hi: () => console.log(`hi ${name}!`),
    bye: () => console.log(`seeya ${name}!`)
  };
}

var greeter = turing('Patia');

greeter.hi();
greeter.bye();

//console.log(msg);
//console.log('standard');
//bar('special');
