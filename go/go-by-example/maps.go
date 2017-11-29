package main

import "fmt"

func main() {

	// make(map[key-type]val-type)
	m := make(map[string]int)

	m["k1"] = 7
	m["k2"] = 13

	fmt.Println("map:", m)

	v1 := m["k1"]
	fmt.Println(" v1:", v1)

	fmt.Println("len:", len(m))

	delete(m, "k2")
	fmt.Println("map:", m)

	// The blank identifyer `_` tells go to *discard* that value
	// We use it here because we know that the value was just deleted
	// and we are only interested in the optional second return value
	// that indicates if the key was present.

	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// oneline declaration
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}
