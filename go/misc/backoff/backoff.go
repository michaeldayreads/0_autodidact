package main

import (
	"fmt"
	"time"
)

func main() {
	i := 1
	factor := 2
	for {
		fmt.Println(i)
		i = i * factor
		time.Sleep(time.Duration(i) * time.Second)
		if i > 10 {
			break
		}
	}
	fmt.Println("And we're out...")
}
