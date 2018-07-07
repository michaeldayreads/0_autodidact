package main

import "os"

import "strings"
import "fmt"

func main() {
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	myEnv := os.Getenv("FOO")
	fmt.Println(myEnv)

	// Modified from example to better grok the blank identifier.
	for qux, e := range os.Environ() {
		pair := strings.Split(e, "=")
		fmt.Println(pair[0], qux)
	}
}
