package main

import "fmt"

func f(intro, from string) {
	fmt.Println(intro)
	for i := 0; i < 3; i++ {
		fmt.Println(from, ":", i)
	}
}

func main() {

	f("Calling Direct, that is to say, synchronously.", "direct")

	go f("Calling in a goroutine, which means asynchronous.", "goroutine")

	go func(msg string) {
		fmt.Println(msg)
	}("And this sentance is the one argument passed to the anonymous function by the goroutine...")

	fmt.Scanln()
	fmt.Println("done")
}
