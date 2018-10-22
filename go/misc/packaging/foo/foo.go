package foo

import "fmt"

// Baz - stuff
func Baz() {
	fmt.Println("Func Baz in foo.go")
}

// Qux - Exported struct
type Qux struct {
	thing1, thing2 string
}

type baz struct {
	thing3, thing4 string
}
