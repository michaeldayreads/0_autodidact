package foo

import "fmt"

// We are importing the qux package to give ourselves the option of
//   a) import foo and get what we have included of qux
//   b) import qux to only have qux
import "github.com/recursivelycurious/zz-autodidact/go/misc_examples/packaging/inception/foo/qux"

func FooA() {
	fmt.Println("FooA")
}

func Qux() {
	qux.Qux()
}
