package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
		fmt.Printf("intermitent value: %v; and in binary: %b\n", sum, sum)
	}
	fmt.Printf("\nFinal value: %v\n", sum)
}
