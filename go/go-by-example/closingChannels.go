package main

import "fmt"
import "time"

func main() {
	jobs := make(chan int, 5)
	done := make(chan bool)

	go func() {
		for {
			// This is a special 2 value form of receive.
			// The second value (more) will be false *if the channel is closed*.
			j, more := <-jobs
			if more {
				fmt.Println("received job", j)
			} else {
				fmt.Println("received all jobs")
				done <- true
				return
			}
		}
	}()

	for j := 1; j <= 3; j++ {
		jobs <- j
		fmt.Println("sent job", j)
		time.Sleep(1 * time.Second)
	}
	close(jobs)
	fmt.Println("sent all jobs")

	// Now we block until the done signal is sent.
	<-done
}
