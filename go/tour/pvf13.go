package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	fmt.Println(x, y, z)
	var f2 float64 = f / 2
	var i2 int = int(f2)
	fmt.Println(f2, i2)
}
