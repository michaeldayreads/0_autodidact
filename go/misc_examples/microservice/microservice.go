package main

import (
	"fmt"
	"math/rand"
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
		default:
			log("...well, lets not deadlock now okay?")
			time.Sleep(1 * time.Second)
		}
	}
}
