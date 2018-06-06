package main

import (
	"fmt"

	"github.com/recursivelycurious/zz-autodidact/go/misc_examples/pkg_test/foo"
	"gitswarm.f5net.com/blue/loglib" // TODO: substitute https://github.com/felix/logger
)

func main() {

	fmt.Println("Main func in main.go")
	foo.Bar()
	foo.Baz()
	// b := foo.Qux
	loglib.Info("Basic Logging.")
}
