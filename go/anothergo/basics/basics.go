package main

// Numeric Constants

import (
	"fmt"
)

const (
	big   = 1 << 100
	small = big >> 99
)

func needInt(x int) int { return x*10 + 1 }
func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(small))
	fmt.Println(needFloat(small))
	fmt.Println(needFloat(big))
}

// Constants

// import "fmt"

// const pi = 3.14

// func main() {
// 	const world = "World"
// 	fmt.Println("Hello", world)
//  fmt.Println(pi)
// }

// type inference

// import "fmt"

// func main() {
// 	v := 0.867 + 0.5i // Change the right hand side to values that require various types
// 	fmt.Printf("v is of type %T\n", v)
// }

// Type conversions

// import (
// 	"fmt"
// 	"math"
// )

// func main() {
// 	var x, y int = 3, 4
// 	var f = math.Sqrt(float64(x*x + y*y))
// 	var z = uint(f)
// 	fmt.Println(x, y, z)
// }

// Zero values

// import "fmt"

// func main() {
// 	var i int
// 	var f float64
// 	var b bool
// 	var s string
// 	fmt.Printf("%v %v %v %q\n", i, f, b, s)
// }

// types

// import (
// 	"fmt"
// 	"math/cmplx"
// )

// // VS code gives a warning that the explicit declaration of toBe and z should be inferred from the right side.
// // The vars here are lower case to avoid a warning that an exported var should have a comment explaining it.
// var (
// 	toBe          = false
// 	maxInt uint64 = 1<<64 - 1
// 	z             = cmplx.Sqrt(-5 + 12i)
// )

// func main() {
// 	fmt.Printf("Type: %T Value: %v\n", toBe, toBe)
// 	fmt.Printf("Type: %T Value: %v\n", maxInt, maxInt)
// 	fmt.Printf("Type: %T Value: %v\n", z, z)
// }

// Short var declarations

// import "fmt"

// func main() {
// 	var i, j int = 1, 2
// 	k := 3
// 	c, python, java := true, false, "Nope."

// 	fmt.Println(i, j, k, c, python, java)
// }

// Variables

// import "fmt"

// var c, python, java bool

// func main() {
// 	var i int
// 	fmt.Println(i, c, python, java)
// }

// Named vs Naked return. Don't do this. It does not help readability.

// import "fmt"

// func split(sum int) (x, y int) {
// 	x = sum * 4 / 9
// 	y = sum - x
// 	return
// }

// func main() {
// 	fmt.Println(split(17))
// }

// Return Multiple Results

// import (
// 	"fmt"
// )

// func swap(x, y string) (string, string) {
// 	return y, x
// }

// func main() {
// 	a, b := swap("This was first.", "And this was second.")
// 	fmt.Println(a, b)
// }

// Functions Continued

// import "fmt"

// func add(x, y int) int {
// 	return x + y
// }

// func main() {
// 	fmt.Println(add(42, 13))
// }

// Functions

// import "fmt"

// func add(x int, y int) int {
// 	return x + y
// }

// func main() {
// 	fmt.Println(add(42, 13))
// }

// Exported names must be capitalized.

// import (
// 	"fmt"
// 	"math"
// )

// func main() {
// 	fmt.Println(math.Pi)
// }

// Imports

// import (
// 	"fmt"
// 	"math"
// )

// func main() {
// 	fmt.Printf("Now you have %g problems\n", math.Sqrt(7))
// }

// Packages

// import (
// 	"fmt"
// 	"math/rand"
// 	"time"
// )

// func main() {
// 	fmt.Println("A random number is", rand.Intn(10))
// 	fmt.Println("\nAnd my favorite number is the empty set :P")
// }

// func init() {
// 	rand.Seed(time.Now().UTC().UnixNano())
// 	fmt.Println("\nSeeding...")
// }
