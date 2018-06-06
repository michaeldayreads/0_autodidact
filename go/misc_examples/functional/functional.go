package main

import "fmt"

type myStruct struct {
	value string
}

func wrapper(ms *myStruct) func(string) {
	return func(msg string) {
		fullMsg := ""
		fullMsg = fullMsg + ms.value + " -- " + msg
		fmt.Println(fullMsg)
	}
}

func main() {
	fmt.Println("sanity")

	var ms = myStruct{"42"}

	logger := wrapper(&ms)
	logger("test")

	fmt.Println(ms)

}
