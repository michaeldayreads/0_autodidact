package main

import (
	"fmt"
	"math"
)

type vertex struct {
	X, Y float64
}

func (v vertex) absMethod() float64 {
	// The "receiver" is the type between the func keyword and the function name.
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func absFunc(v vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func methods() {
	v := vertex{3, 4}
	fmt.Println(v.absMethod())
	fmt.Println(absFunc(v))
}

type myFloat float64

func (f myFloat) absMyFloat() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func methodsContinued() {
	// The receiver for the Method must be in the same package as the Method using it.
	// Thus, built in types cannot have their Methods overridden.
	f := myFloat(-math.Sqrt2)
	fmt.Println(f.absMyFloat())
}

func (v *vertex) scale(f float64) {
	// Note there is NO return statement, and no declared type we are returning.
	// We are modifying the underlying Type through pointer to the dereferenced receiver.
	v.X = v.X * f
	v.Y = v.Y * f
}

func pointerReceivers() {
	v := vertex{3, 4}
	v.scale(10)
	fmt.Println(v.absMethod())
}

func scaleFunc(v *vertex, f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func pointerIndirection() {
	v := vertex{3, 4}
	v.scale(2)
	scaleFunc(&v, 10)

	p := &vertex{4, 3}
	p.scale(3)
	scaleFunc(p, 8)

	fmt.Println(v, p)
	// The important difference between these two methods is what you have at the end; value or pointer?
}

func pointerIndirection2() {
	fmt.Println("Values:")
	v := vertex{3, 4}
	fmt.Println(v.absMethod())
	fmt.Println(absFunc(v))

	fmt.Println("\nPointers")
	p := &vertex{4, 3}
	fmt.Println(p.absMethod())
	fmt.Println(absFunc(*p))

	fmt.Println("\nNote that in this case, contrary to the last, all of the results are of type int.\nThis is due to the use of the absolute value Method and Function, which return a type float64 in all cases.")
}

func (f myFloat) absInterface() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func (v *vertex) absInterface() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

type absoluteValueInterface interface {
	absInterface() float64
}

func interfaces() {
	var a absoluteValueInterface
	f := myFloat(-math.Sqrt2)
	v := vertex{3, 4}

	a = f
	fmt.Println(a.absInterface())
	a = &v

	fmt.Println(a.absInterface())
}

func main() {
	// methods()
	// methodsContinued()
	// pointerReceivers()
	// pointerIndirection()
	// pointerIndirection2()
	interfaces()
}
