package main

import "fmt"

func main() {
	queue := make(chan string, 2)
	queue <- "zero"
	queue <- "one"
	// If we try to push another value onto the channel, the code compiles...
	// But does not run:
	//     fatal error: all goroutines are asleep - deadlock!
	// queue <- "qux"
	temp := <-queue
	fmt.Println(temp)
	queue <- "two"
	// We can close this channel, and the vaulues in the buffer will be retained.
	close(queue)

	for elem := range queue {
		// In this case, the range receives without using the <- notation
		fmt.Println(elem)
	}
}
