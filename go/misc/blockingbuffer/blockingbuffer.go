package main

import "fmt"

func main() {
	msgs := make(chan string, 2)

	go func() {
		msgs <- "one"
		msgs <- "two"
		msgs <- "three"
		close(msgs)
	}()

	for msg := range msgs {
		fmt.Println(msg)
	}
}
