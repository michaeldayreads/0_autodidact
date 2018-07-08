package main

import "fmt"

// ping only accepts messages to send on a channel
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// pong accepts a pings channel to receive and a pongs channel to send.
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings // msg receives from pings
	pongs <- msg   // msg is sent to pongs
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	// Interestingly, we can print the contents of the channel
	fmt.Println(<-pongs)
}
