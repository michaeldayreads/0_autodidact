package main

import (
	"fmt"
	"math/rand"
	"os"
	"sync/atomic"
	"time"
)

var health bool

func log(msg string) {
	fmt.Println(msg)
}

func chaosMonkey(r *rand.Rand) {
	if r.Intn(100) > 90 {
		health = false
	} else {
		health = true
	}
}

func main() {
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	log("Start main.")

	var metric uint64

	workChan := make(chan string)
	healthChan := make(chan string)
	metricChan := make(chan string)
	done := make(chan struct{})

	// This goroutine simulates doing the main task.
	go func() {
		for {
			time.Sleep(1 * time.Second)
			atomic.AddUint64(&metric, 1)
			workChan <- "Do'n work..."
			chaosMonkey(r1)
		}
	}()

	// This simulates checking the health.
	go func() {
		for {
			time.Sleep(2 * time.Second)
			if r1.Intn(100) > 75 {
				healthChan <- "requst health"
			}
		}
	}()

	// This goroutine simulates checking the metrics.
	go func() {
		for {
			time.Sleep(2 * time.Second)
			if r1.Intn(100) > 75 {
				metricChan <- "request metrics"
			}
		}
	}()

	// This goroutine waits for an interrupt.
	// It could just as easily be a different kind of signal
	// Using the blocking case below, responding to that signal is real time
	//   but without consuming significant resources.
	go func() {
		fmt.Scanln()
		log("..welp, looks like yer all done here. See ya!")
		done <- struct{}{}
	}()

	for {
		select {
		case work := <-workChan:
			log(work)
		case healthCheck := <-healthChan:
			log(healthCheck)
			log(fmt.Sprintf("%t", health))
		case metricsCheck := <-metricChan:
			log(metricsCheck)
			log(fmt.Sprintf("%d", metric))
		case <-done:
			os.Exit(0)
		}
	}
}
