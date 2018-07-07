package main

import "fmt"
import "time"

// worker is a function accepts a channel of booleans named "done"
// and it sends a true when its work is complete.
func worker(done chan bool) {
	fmt.Println("Working...")
	time.Sleep(time.Second)
	time.Sleep(time.Second)
	time.Sleep(time.Second)
	fmt.Println("done.")

	done <- true
}

func main() {
	// create a channel to give to the worker
	done := make(chan bool, 1)
	fmt.Println("Start the worker.")
	go worker(done)
	time.Sleep(time.Second)
	fmt.Println("Since the worker is off doing its thing, we have to block to make sure we don't exit before its completed.")
	// block until we recieve a notifiaction. The main program is done, but waiting for the worker.
	<-done
}
