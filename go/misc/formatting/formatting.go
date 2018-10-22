// Some different ways to print out a custom struct, for example to a log entry.

package main

import "fmt"

type endpoint struct {
	ip   string
	port int
}

func main() {
	ep := []endpoint{}

	ep = append(ep, endpoint{ip: "10.0.0.0", port: 80})
	ep = append(ep, endpoint{ip: "10.0.0.1", port: 8080})

	fmt.Println(ep)

	fmt.Println("and now we try and do it this way: ", ep)
	fmt.Println(fmt.Sprint("another... ", ep))
}
