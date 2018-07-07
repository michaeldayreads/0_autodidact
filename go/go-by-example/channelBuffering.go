package main

import "fmt"

func main() {

	messages := make(chan string, 2)

	messages <- "Buffered"
	messages <- "Channel"

	fmt.Println(<-messages)
	fmt.Println(<-messages)

}
