package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
		fmt.Printf("Intermitent sum: %v\n", sum)
	}
	fmt.Printf("Final total: %d", sum)
}
