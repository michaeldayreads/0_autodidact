package main

import "fmt"

func main() {
	messages := make(chan string)
	signals := make(chan bool)

	select {
	// This sets up a receiver *if* there is a message. There is not one yet, so the default is chosen.
	case msg := <-messages:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	msg := "hi"

	select {
	// Since there is no buffer, there is no place for the message, and the default case is chosen.
	case messages <- msg:
		fmt.Println("message sent")
	default:
		fmt.Println("no message sent")
	}

	select {
	// Since the default was chosen above, there is no message.
	// We have done nothing with the signals channel, so again the default is chosen.
	case msg := <-messages:
		fmt.Println("received message", msg)
	case sig := <-signals:
		fmt.Println("received signal", sig)
	default:
		fmt.Println("crickets...")
	}
}
