// methods on non structs

package main

import (
	"fmt"
	"math"
)

// type that we will use in a "class" like manner
// that is not a struct
type MyFloat float64

// "method" declared on that type
func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

// compare to the more class like...
type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	f := MyFloat(-math.Sqrt2)
	fmt.Println("methodish call of f.Abs():", f.Abs())
	fmt.Println("methodish call of v.Abs():", v.Abs())
}
