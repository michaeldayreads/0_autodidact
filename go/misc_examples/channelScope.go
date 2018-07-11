package main

import (
	"errors"
	"fmt"
)

type endpoint struct {
	ip   string
	port int
}

func sim(i int) (endpoint, error) {
	if i < 10 {
		return endpoint{}, errors.New("No endpoints found.")
	} else {
		return endpoint{"10.1.2.3", 443}, nil
	}
}

func main() {
	endpointChan := make(chan endpoint)

	go func() {
		i := 0
		for {
			ep, err := sim(i)
			if err != nil {
				fmt.Println("[Error] Unable to use", i, err)
				i++
				continue
			} else {
				endpointChan <- ep
				break
			}
		}
	}()

	ep := <-endpointChan
	fmt.Println(ep)
}
