// per the go proverb on dependency
// this is a partial re-implementation from
// https://github.com/cenkalti/backoff

package main

import (
	"errors"
	"fmt"
	"time"
)

type backoffTimer interface {
	sleepFor() time.Duration
}

type trueTimer struct {
	// the actual backoff
	ceiling time.Duration
	current time.Duration
}

func (tt *trueTimer) sleepFor() time.Duration {
	if 2*tt.current > tt.ceiling {
		fmt.Printf("returning ceiling: %v\n", tt.ceiling)
		return tt.ceiling
	}
	if tt.current < time.Second {
		tt.current = time.Second
		fmt.Printf("returning current: %v\n", tt.current)
		return tt.current
	}
	tt.current = tt.current * 2
	fmt.Printf("returning current: %v\n", tt.current)
	return tt.current
}

type testTimer struct {
	// test version
}

func (t *testTimer) sleepFor() time.Duration {
	return 1 * time.Microsecond
}

func backoff(bt backoffTimer) time.Duration {
	return bt.sleepFor()
}

func waitForIt(i int) error {
	if i < 5 {
		return errors.New("No resource available yet")
	}
	return nil
}

func main() {
	fmt.Printf("TrueTimer:\n")
	actual := trueTimer{ceiling: (5 * time.Second)}
	for i := 0; i < 10; i++ {
		err := waitForIt(i)
		if err != nil {
			fmt.Println("true backoff...")
			time.Sleep(backoff(&actual))
			// fmt.Printf("should have slept for %v seconds", actual.nextSleep)
			continue
		}
		break
	}
	fmt.Println("We have what we came for")

	fmt.Printf("\n\nTestTimer:\n")

	tester := testTimer{}
	for i := 0; i < 10; i++ {
		err := waitForIt(i)
		if err != nil {
			fmt.Println("test backoff...")
			time.Sleep(backoff(&tester))
			continue
		}
		break
	}
	fmt.Println("We have what we came for")
}
