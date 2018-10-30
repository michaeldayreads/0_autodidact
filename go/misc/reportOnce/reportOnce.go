// poc of sync.Once for a microservice event pattern where we want to log progress/failure locally and broadcast only one event rather than spam a metric aggregator
package main

import (
	"errors"
	"fmt"
	"sync"
	"time"
)

func mockUnreliableResource(i int) (int, error) {
	if i < 5 {
		return 0, errors.New("No resource available")
	} else {
		return i, nil
	}
}

func main() {
	var reportOnce sync.Once

	reportError := func() {
		fmt.Println("Broadcast error beyond microservice")
	}

	for i := 1; i < 10; i++ {
		_, err := mockUnreliableResource(i)
		if err != nil {
			fmt.Println("Log error within microservice")
			reportOnce.Do(reportError)
			time.Sleep(time.Second)
			continue
		}
		break
	}
	fmt.Println("We have the state we wanted. All is well.")
}
