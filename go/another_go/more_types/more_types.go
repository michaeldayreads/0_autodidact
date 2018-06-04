package main

import (
	"fmt"
	"math"
	"reflect"
	"strings"
)

func pointers() {
	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer (aka dereference)
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see new value of j
}

type vertex struct {
	X int
	Y int
}

func structs() {
	fmt.Println(vertex{1, 2})
}

func structFields() {
	v := vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}

func pointersToStructs() {
	v := vertex{1, 2}
	p := &v
	(*p).Y = 42 // This is the full notation.
	p.X = 1e9   // This is the permitted shorthand.
	fmt.Println(v)
}

// vars for structLiterals()

var (
	v1 = vertex{1, 2}
	v2 = vertex{X: 1}  // The default value for Y, which is an int, is 0
	v3 = vertex{}      // Defaults for both X and Y.
	p0 = &vertex{3, 4} // This pointer has type *vertex
)

func structLiterals() {
	fmt.Println(v1, v2, v3, p0, *p0)
}

func arrays() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println("Each indexed item: ", a[0], a[1])
	fmt.Println("  The whole array: ", a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}

func slices() {
	primes := [6]int{2, 3, 5, 7, 11, 13}

	var s = primes[1:4] // Note that the more explicit `var s []int = primes[1:4]` generates a warning from vs code?
	fmt.Println(s)
}

func aSliceIsLikeARef() {
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}

func sliceLiterals() {
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)
	fmt.Println("Note that r is of the type: ", reflect.TypeOf(r))

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
	fmt.Println(s[0])
	fmt.Println(s[1])
	fmt.Println("    Type of s: ", reflect.TypeOf(s))
	fmt.Println("it's elements: ", reflect.TypeOf(s[4]))
}

func sliceDefaults() {
	s := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(len(s))
	printSlice(s)

	s = s[1:4]
	fmt.Println(len(s))
	printSlice(s)

	s = s[:2]
	fmt.Println(len(s))
	printSlice(s)

	s = s[1:]
	fmt.Println(len(s))
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len: %d  cap: %d  %v\n", len(s), cap(s), s)
}

func lengthAndCapacity() {
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	s = s[:0]
	printSlice(s)

	s = s[:4]
	printSlice(s)

	s2 := s[2:3] // bring back the full capacity
	printSlice(s2)
	printSlice(s)

	s = append(s, 11, 13, 17)
	// The size of the underlying array is doubled if there is not enough capacity.
	printSlice(s)

	s = s[1:]
	// Slice from the bottom reduces length AND capacity
	printSlice(s)

	s = s[:3]
	printSlice(s)
}

func nilSlices() {
	var s []int
	printSlice(s)
	if s == nil {
		fmt.Println("This is a nil slice.")
	}
}

func makeSlice() {
	a := make([]int, 5)
	printSlice(a)

	b := make([]int, 0, 5)
	printSlice(b)

	c := b[:2]
	printSlice(c)

	d := c[2:5]
	printSlice(d)
}

func sliceOfSlices() {
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

func appendingSlices() {
	var s []int
	printSlice(s)

	s = append(s, 0)
	printSlice(s)

	s = append(s, 1)
	printSlice(s)

	s = append(s, 2)
	printSlice(s)

	s = append(s, 3, 4, 5)
	printSlice(s)
}

func rangeClause() {
	var pow = []int{1, 2, 4, 8, 16, 64, 128}

	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}

func rangeContinued() {
	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(i)
	}
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}
}

type mapVertex struct {
	Lat, Long float64
}

// var m map[string]mapVertex

func maps() {
	m := make(map[string]mapVertex)
	m["Bell Labs"] = mapVertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

func mapLiterals() {
	var m2 = map[string]mapVertex{
		"foo": mapVertex{
			1, 2,
		},
		"bar": mapVertex{
			-3, -4,
		},
	}
	fmt.Println(m2)
}

func mapLiteralsContinued() {
	// When the top level type is just a type name, it may be omitted.
	// ?? When would it be something more than or other than a type name?
	var m3 = map[string]mapVertex{
		"baz": {0, 1},
		"qux": {1, 0},
	}
	fmt.Println(m3)
}

func printAnswer(v int) {
	fmt.Println("The value:", v)
}

func mutatingMaps() {
	m := make(map[string]int)

	m["Answer"] = 42
	printAnswer(m["Answer"])

	m["Answer"] = (42 / 2) + 7
	printAnswer(m["Answer"])

	delete(m, "Answer")
	// The default value lets us use either of the next two methods.
	// fmt.Println("The value:", m["Answer"])
	printAnswer(m["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}

func compute(fn func(float64, float64) float64) float64 {
	// The param for this function is:
	//  - a function that itself takes two float64s and
	//  - returns a float64
	// And the compute function returns a float64 as well.
	return fn(3, 4)
}

func functionValues() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))
	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}

func adder() func(int) int {
	// The adder function has no parameters and returns
	// a function that takes an int and returns an int.
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func closure() {
	// A closure is a function value that references variables outside its body.
	// Another way to think of it is that a closure has variables bound to it.
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}

func main() {
	// pointers()
	// structs()
	// structFields()
	// pointersToStructs()
	// structLiterals()
	// arrays()
	// slices()
	// aSliceIsLikeARef()
	// sliceLiterals()
	// sliceDefaults()
	// lengthAndCapacity()
	// nilSlices()
	// makeSlice()
	// sliceOfSlices()
	// appendingSlices()
	// rangeClause()
	// rangeContinued()
	// maps()
	// mapLiterals()
	// mapLiteralsContinued()
	// mutatingMaps()
	// functionValues()
	closure()
}
