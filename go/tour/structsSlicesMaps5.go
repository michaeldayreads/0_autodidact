package main

import "fmt"

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}
	v2 = Vertex{X: 1}
	v3 = Vertex{}
	p  = &Vertex{3, 4}
	p2 = &v2

	v4 = Vertex{Y: 10, X: 1} // order of :name unimportant
)

func main() {
	//fmt.Println(v1, p, v2, v3, v4)
	fmt.Printf("v1: %v\n\n", v1)
	fmt.Printf("v2: %v\n\n", v2)
	fmt.Printf("v3: %v\n\n", v3)
	fmt.Printf(" p: %v\n\n", *p)
	fmt.Printf("p2: %v\n\n", *p2)
	p.X, p.Y = 1, 2
	fmt.Printf(" p: %v\n\n", *p)
}
