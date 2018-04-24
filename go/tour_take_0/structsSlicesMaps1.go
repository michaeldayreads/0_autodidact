package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i
	// point to i
	fmt.Printf(" p w/%%p: %p (This is a memory address for i.)\n", p)
	fmt.Printf("*p w/%%p: %p (This appears to be literal\ndescription of the pointer.)\n\n", *p)
	fmt.Printf("*p w/%%v: %v (This is the underlying value p\npoints to at that address.)\n\n", *p)
	fmt.Printf(" p w/%%T: %T (This is the type of pointer itself.)\n", p)
	fmt.Printf("*p w/%%T: %T (This is the type of the underlying value.)\n", *p)

	*p = 21
	fmt.Printf("i: %v\n", i)

	p = &j
	*p = *p / 37
	fmt.Printf("j: %v\n", j)
	fmt.Printf("i: %v\n", i)
}
