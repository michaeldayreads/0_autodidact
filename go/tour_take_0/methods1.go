// methods
// Go does not have classes
// a method is a special kind of function,
// which can be defined on types (structs)

// notice the *receiver* argument
// such that the Abs method has a receiver
// of type Vertex nameed v

package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// a standard function for comparison
// notice no receiver
func plus(a int, b int) int {
	return a + b
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
	fmt.Println(plus(3, 4))
}
