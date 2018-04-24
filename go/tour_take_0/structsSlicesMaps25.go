// Function closures
// the adder() refurns a closure
// main creates two adder()
// each bound to its own sum variable

package main

import "fmt"

func adder() func(int) int {
	fmt.Println("adder()") // visibliity
	sum := 0
	return func(x int) int {
		fmt.Println("Internal func") // visibility
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
