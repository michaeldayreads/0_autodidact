// methods are functions

package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

// the method immplementation
func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// a standard function for comparison
// notice no receiver
func plus(a int, b int) int {
	return a + b
}

// and as a plain function
func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println("The method method, called using 'v.Abs():'", v.Abs())
	fmt.Println("The function method, called using 'Abs(v)':", Abs(v))
	fmt.Println("Sanity function:", plus(3, 4))
}
