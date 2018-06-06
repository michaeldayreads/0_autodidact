package foo

import "fmt"

// Bar - stuff
func Bar() {
	fmt.Println("Func Bar in bar.go")
}

// Bazifyer prints out the things in the baz
func Bazifyer(b baz) {
	fmt.Println("The properties of the baz are:")
	fmt.Println(b.thing3, b.thing4)
}
