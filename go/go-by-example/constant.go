package main

import (
	"fmt"
	"math"
)

const s string = "constant"

func main() {
	fmt.Println(s)

	const n = 500000000

	const d = 3e20 / n
	// this constant has no type, thus
	fmt.Println(d)
	// > 6e+11

	// but we can cast it
	fmt.Println(int64(d))
	// > 600000000000

	// similarly, type can be provided by context
	// math.Sin expects a float64
	fmt.Println(math.Sin(n))
}
